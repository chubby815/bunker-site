import re

path = "C:/BunkerSite/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

original_len = len(html)

# Remove the three logo CSS blocks that contain mix-blend-mode
# They are wrapped in /* NAV LOGO */ /* HERO LOGO */ /* FOOTER LOGO */ comments
html = re.sub(r'/\* NAV LOGO \*/.*?/\* END NAV LOGO \*/', '', html, flags=re.DOTALL)
html = re.sub(r'/\* HERO LOGO \*/.*?/\* END HERO LOGO \*/', '', html, flags=re.DOTALL)
html = re.sub(r'/\* FOOTER LOGO \*/.*?/\* END FOOTER LOGO \*/', '', html, flags=re.DOTALL)

# Also strip any standalone mix-blend-mode lines left anywhere
html = re.sub(r'\s*mix-blend-mode\s*:\s*lighten\s*;', '', html)

# Strip any filter: drop-shadow lines that were part of the blend hack
# (keep real drop-shadows that aren't on logo imgs)
# Target only the logo-specific filter lines with the blue glow
html = re.sub(r'\s*filter\s*:\s*drop-shadow\([^)]*1e90ff[^)]*\)\s*drop-shadow\([^)]*00bfff[^)]*\)\s*;', '', html)
html = re.sub(r'\s*filter\s*:\s*drop-shadow\([^)]*00bfff[^)]*\)\s*;', '', html)

# Now add clean simple CSS for the logo images — no blend, just sizing
# Find </style> and insert before it
clean_logo_css = """
  /* ─── LOGO IMAGES (transparent PNG — no blend needed) ─── */
  .nav-logo img {
    height: 36px;
    width: auto;
    vertical-align: middle;
    display: block;
  }
  .hero-logo {
    height: 100px;
    width: auto;
    display: block;
    margin: 0 auto 24px;
    filter: drop-shadow(0 0 18px rgba(0,191,255,0.5));
  }
  .footer-logo img {
    height: 26px;
    width: auto;
    display: block;
  }
"""

html = html.replace('</style>', clean_logo_css + '\n</style>', 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Original size: {original_len} bytes")
print(f"New size:      {len(html)} bytes")
print(f"mix-blend-mode remaining: {html.count('mix-blend-mode')}")
print(f"Logo CSS blocks injected: {'nav-logo img' in html and 'hero-logo' in html and 'footer-logo img' in html}")
print("DONE")
