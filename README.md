# Carousel Scraper - Final

Professional carousel generator for Costa Dream Realty real estate listings. Scrapes property data from URLs and generates Instagram carousel slides (8 slides, 1080x1350px) with **unique, property-specific editorial copy**.

## Features

- **URL Scraping**: Automatically fetch property data and images from any real estate website
- **Dynamic Copy Generation**: Each slide displays unique copy specific to the property (beds/baths, size, amenities, location)
- **Manual Mode**: Upload photos and manually enter property details
- **Multi-language**: Full English/Spanish support with property-aware translations
- **Smart Copy**: Auto-generates marketing copy based on property type, size, and features
- **Canvas Rendering**: High-quality slides with professional typography
- **Bulk Download**: Export all 8 slides as PNG or ZIP

## What Finally Worked

### Dynamic Editorial Copy Generation

Each carousel now generates **unique, property-specific copy** for every slide based on actual scraped data:

**Copy varies by:**
- Property type (land, beachfront, villa, hotel, retreat, condo, house, hostal)
- Bed/bath count ("5 bedrooms. 3 baths. Real luxury." vs "Compact. Considered.")
- Square meters ("300+ m² = rare private space" vs "150-300 m² = efficient design")
- Key amenities (pool, ocean view, beachfront detected from features)
- Location (Mazunte, Zipolite, Huatulco, Puerto Escondido, etc.)

**Outcome:** No more repeated generic copy. Each property's carousel has editorial-specific content matching its actual features and size.

### Local Proxy Server (Port 5001)

The key to reliable scraping is running a local CORS proxy:

```bash
python3 scraper-proxy.py 5001
```

**Why this works:**
- Bypasses browser CORS restrictions
- More reliable than public proxy services (allorigins.win, cors-anywhere, etc. were inconsistent)
- Runs on port 5001 (port 5000 blocked by macOS AirPlay Receiver)
- Handles timeouts and retry logic gracefully

### Scraping Process

1. **Start the proxy** (required for URL scraping):
   ```bash
   python3 scraper-proxy.py 5001
   ```

2. **Open the carousel generator** (via HTTP server on port 8000):
   - Visit `http://localhost:8000/CDR-Carousel-FINAL-20260527-125001.html` in a browser
   
3. **Paste property URL**:
   - Works with any real estate site (costadreamrealty.com, EasyBroker, Airbnb, etc.)
   - Generator auto-detects: location, property type, price, beds, baths, photos
   
4. **Review & Edit Copy**:
   - Customize the generated marketing copy
   - Choose color tier (navy, camel, beige)
   - Adjust language (EN/ES)
   
5. **Render 8 Slides**:
   - Generates professional carousel automatically
   - Click individual slides to download as PNG

## Files

- **CDR-Carousel-FINAL-20260527-125001.html** - Main carousel generator (all-in-one HTML file with latest fixes)
- **scraper-proxy.py** - Local CORS proxy server with CORS headers (required for URL scraping)
  - Must be run on port 5001
  - Handles both GET and OPTIONS requests
  - Returns `Access-Control-Allow-Origin: *` header

## How to Use

### Mode 1: Scrape from URL (Recommended)
```
1. Start proxy: python3 scraper-proxy.py 5001
2. Paste URL → Click "Fetch & Preview Copy"
3. Review copy and colors
4. Click "Render 8 Slides →"
5. Download individual slides or full ZIP
```

### Mode 2: Manual Upload
```
1. Skip the URL step
2. Upload 8+ photos
3. Fill in: title, location, price, beds, baths, features
4. Choose property type (auto-detect or manual)
5. Review generated copy
6. Click "Render 8 Slides →"
```

## Slide Layout

1. **Hero** - Large title, subtitle
2. **Image** - Full-screen photo
3. **Features** - Headline + 4 key features
4. **Full Image** - Large photo
5. **Headline** - Call-to-action text
6. **Image** - Full-screen photo
7. **Features** - Location details
8. **CTA** - Call to action with Instagram caption

## Color Tiers

Price automatically selects color scheme:
- **Navy** (#1c2e45) - $800K+ USD
- **Camel** (#a07830) - $500K–$800K USD
- **Beige** (#f0e9d6) - Under $500K USD

## Location-Specific Copy

Auto-detects and customizes copy for:
- Mazunte
- Zipolite
- Huatulco
- Puerto Escondido
- Puerto Ángel
- Default (generic Oaxaca coast)

## Property Type Detection

Automatically detects:
- Land/Terreno
- Beachfront/Oceanfront
- Villa
- Hotel/Hostal/Retreat
- Condo/Apartment
- House/Residencia
- Default

## Requirements

- Modern web browser (Chrome, Firefox, Safari)
- Python 3 (for proxy server)
- Flask: `pip install flask requests`

## Installation

1. Clone this repo
2. Install Python dependencies:
   ```bash
   pip install flask requests
   ```
3. Run proxy server:
   ```bash
   python3 scraper-proxy.py 5001
   ```
4. Open HTML file in browser

## Technical Notes

### Why Images Sometimes Fail

If images don't load from a URL:
1. Check the proxy is running: `lsof -i :5001`
2. Check site allows scraping (some block it)
3. Use manual upload mode instead

### Text Layout

- All text is centered within 72px margins on each side
- Small text automatically wraps to prevent overflow
- Font: Playfair Display (serif, elegant)

### Canvas Rendering

- **Resolution**: 1080x1350px (Instagram vertical)
- **Image Ratio**: 1.265:1 (landscape-friendly)
- **Colors**: Tier-based (navy/camel/beige)
- **Gradients**: Removed (solid colors only)
- **Notebook lines**: Removed (clean solid background)

## Proxy Server Setup Guide

The carousel **requires a local proxy server** to scrape URLs (due to browser CORS restrictions).

### Quick Start (Two Servers Required)

```bash
# 1. Install Python 3 (if not already installed)
# Check: python3 --version

# 2. Install Flask & Requests
pip install flask requests

# 3. Terminal Window #1 - Run the CORS proxy server (port 5001)
python3 scraper-proxy.py 5001

# Output should show:
# 🚀 Proxy running at http://localhost:5001

# 4. Terminal Window #2 - Run HTTP server for carousel (port 8000)
python3 -m http.server 8000

# 5. Open carousel in browser
# Visit: http://localhost:8000/CDR-Carousel-FINAL-20260527-125001.html
```

### Critical: Why Both Servers?

**DO NOT open the carousel as `file:///` from your computer.** This breaks all fetch requests due to browser security sandboxing.

- ❌ **WRONG**: `file:///Users/eontiveros/CDR-Carousel-FINAL-20260527-125001.html`
- ✅ **CORRECT**: `http://localhost:8000/CDR-Carousel-FINAL-20260527-125001.html`

### How It Works

When you paste a property URL in the carousel:
1. Browser (on `http://localhost:8000`) sends request to proxy at `http://localhost:5001`
2. Proxy MUST send CORS headers (`Access-Control-Allow-Origin: *`) for browser to accept response
3. Proxy fetches the actual website (bypasses CORS restrictions)
4. Carousel extracts title, price, bedrooms, images, etc.
5. Copy is generated based on scraped property data
6. 8 slides render with unique editorial copy

### Proxy CORS Headers (Critical Fix)

The `scraper-proxy.py` now includes proper CORS headers:
```python
# Handles browser preflight requests
@app.route('/', methods=['GET', 'OPTIONS'])
def proxy():
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    # ... fetch and return with CORS header
    return response.text, 200, {
        'Content-Type': 'text/html; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
    }
```

Without these headers, the browser blocks the proxy response even though the server is running. **This was the root cause of "Proxy failed" errors.**

### Why Port 5001?

- **Port 5000** is blocked by macOS AirPlay Receiver
- **Port 5001** is open and conflict-free
- Proxy script accepts custom ports: `python3 scraper-proxy.py 9999` (example)

### Keep Proxy Running

The proxy must **stay running** while you use the carousel:
- Open terminal, run `python3 scraper-proxy.py 5001`
- Keep terminal window open
- Open carousel in browser (same machine)
- Paste URLs and scrape

### Multiple Properties

You can scrape as many properties as you want in one session:
1. Start proxy once: `python3 scraper-proxy.py 5001`
2. Open carousel HTML
3. Paste first URL → generates slides
4. Paste second URL → generates new slides
5. (proxy runs continuously in background)

### Proxy Troubleshooting

| Problem | Solution |
|---------|----------|
| "Address already in use" | Kill existing proxy: `pkill -f scraper-proxy.py` |
| "Command not found: python3" | Install Python 3 from python.org |
| "No module named 'flask'" | Run: `pip install flask requests` |
| "Connection refused" | Make sure proxy is running in terminal |
| "All proxies failed" | Verify: `lsof -i :5001` should show the proxy running |

### Proxy File Location

Keep `scraper-proxy.py` in the same folder as your carousel HTML file (or any folder you can access).

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "All proxies failed" | Start proxy: `python3 scraper-proxy.py 5001` |
| Port 5001 already in use | Kill process: `pkill -f scraper-proxy.py` |
| Images not loading | Check proxy is running, or use manual mode |
| Text overflowing | Text auto-wraps; check browser zoom is 100% |
| Can't download slides | Browser may block downloads; check permissions |

## Version History

- **2026-05-27**: Fixed CORS proxy headers issue. Proxy now returns `Access-Control-Allow-Origin: *` header. Must serve carousel via HTTP server (port 8000) not file://. Added OPTIONS request handling for preflight.
- **2025-05-26**: Removed gradients, fixed text margins, local proxy on 5001, solid CTA background, unique property-specific editorial copy generation
- Previous versions: Experimented with external proxies (unstable)

---

**Made with ❤️ for Costa Dream Realty**
