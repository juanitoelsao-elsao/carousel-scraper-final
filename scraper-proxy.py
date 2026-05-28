#!/usr/bin/env python3
"""
Simple CORS proxy for scraping - run locally with: python3 scraper-proxy.py
Then use: http://localhost:5000/?url=https://example.com
"""
from flask import Flask, request, jsonify
import requests
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/', methods=['GET', 'OPTIONS'])
def proxy():
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }

    url = request.args.get('url', '').strip()

    if not url:
        return jsonify({'error': 'Missing ?url= parameter'}), 400

    try:
        # Fetch the URL with a proper user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        return response.text, 200, {
            'Content-Type': 'text/html; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
        }

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timeout'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection failed'}), 502
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(f"🚀 Proxy running at http://localhost:{port}")
    print(f"Usage: http://localhost:{port}/?url=https://example.com")
    app.run(debug=True, port=port)
