# Carousel Scraper - Final

Professional carousel generator for real estate listings. Scrapes property data from URLs and generates Instagram carousel slides (8 slides, 1080x1350px).

## Features

- **URL Scraping**: Automatically fetch property data and images from any real estate website
- **Manual Mode**: Upload photos and manually enter property details
- **Multi-language**: Full English/Spanish support
- **Smart Copy**: Auto-generates marketing copy based on location and property type
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

2. **Open the carousel generator**:
   - Open `CDR-Carousel-2025-05-26-FINAL.html` in a browser
   
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

- **CDR-Carousel-2025-05-26-FINAL.html** - Main carousel generator (all-in-one HTML file)
- **scraper-proxy.py** - Local CORS proxy server (required for URL scraping)

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
- **Navy** (#1c2e45) - Under $500k
- **Camel** (#a07830) - $500k-$2M
- **Beige** (#f0e9d6) - $2M+

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

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "All proxies failed" | Start proxy: `python3 scraper-proxy.py 5001` |
| Port 5001 already in use | Kill process: `pkill -f scraper-proxy.py` |
| Images not loading | Check proxy is running, or use manual mode |
| Text overflowing | Text auto-wraps; check browser zoom is 100% |
| Can't download slides | Browser may block downloads; check permissions |

## Version History

- **Final (2025-05-26)**: Removed gradients, fixed text margins, local proxy on 5001, solid CTA background
- Previous versions: Experimented with external proxies (unstable)

---

**Made with ❤️ for Costa Dream Realty**
