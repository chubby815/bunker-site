import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Count SVG trees before
svg_count_before = html.count('<svg xmlns="http://www.w3.org/2000/svg"')
print(f"SVG tags before: {svg_count_before}")

# Replace NAV svg (32x32 Bunker logo)
nav_pattern = r'<svg xmlns="http://www\.w3\.org/2000/svg" viewBox="0 0 64 64" width="32" height="32" aria-label="Bunker logo">[\s\S]*?</svg>'
nav_replacement = '<img src="logo.png" alt="Bunker logo" class="nav-logo-img" />'
html, nav_count = re.subn(nav_pattern, nav_replacement, html)
print(f"Nav SVG replacements: {nav_count}")

# Replace HERO svg (120x120 Bunker)
hero_pattern = r'<svg xmlns="http://www\.w3\.org/2000/svg" viewBox="0 0 64 64" width="120" height="120" aria-label="Bunker" class="hero-logo">[\s\S]*?</svg>'
hero_replacement = '<img src="logo.png" alt="Bunker" class="hero-logo-img" />'
html, hero_count = re.subn(hero_pattern, hero_replacement, html)
print(f"Hero SVG replacements: {hero_count}")

# Also catch footer logo (same 120x120 block that ended up there)
footer_pattern = r'<svg xmlns="http://www\.w3\.org/2000/svg" viewBox="0 0 64 64" width="120" height="120" aria-label="Bunker" class="hero-logo">[\s\S]*?</svg>'
html, footer_count = re.subn(footer_pattern, '<img src="logo.png" alt="Bunker" class="footer-logo-img" />', html)
print(f"Footer SVG replacements: {footer_count}")

svg_count_after = html.count('<svg xmlns="http://www.w3.org/2000/svg"')
print(f"SVG tags after: {svg_count_after}")

# Now update CSS for all three logo img classes
css_additions = """
  /* ─── LOGO IMG OVERRIDES ───────────────────────────────────────── */
  .nav-logo-img {
    width: 36px;
    height: 36px;
    object-fit: contain;
    mix-blend-mode: lighten;
    filter: drop-shadow(0 0 8px rgba(30,144,255,0.75))
            drop-shadow(0 0 2px rgba(0,191,255,0.5));
    vertical-align: middle;
  }

  .hero-logo-img {
    width: 140px;
    height: 140px;
    object-fit: contain;
    mix-blend-mode: lighten;
    filter: drop-shadow(0 0 24px rgba(30,144,255,0.8))
            drop-shadow(0 0 8px rgba(0,191,255,0.6));
    display: block;
  }

  .footer-logo-img {
    width: 24px;
    height: 24px;
    object-fit: contain;
    mix-blend-mode: lighten;
    filter: drop-shadow(0 0 5px rgba(30,144,255,0.6));
    vertical-align: middle;
  }
"""

# Inject before closing </style>
html = html.replace('</style>', css_additions + '</style>', 1)
print("CSS injected: OK")

with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("File written: OK")
print("ALL DONE")
