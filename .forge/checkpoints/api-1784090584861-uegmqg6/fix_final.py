import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. REMOVE any previously injected logo CSS blocks (between the old markers or .nav-logo-img blocks)
# Remove the stale injected block if it exists (it apparently didn't make it, but clean anyway)
html = re.sub(r'\s*/\* ={3,} LOGO IMG OVERRIDES.*?\*/', '', html, flags=re.DOTALL)
html = re.sub(r'\s*\.nav-logo-img\s*\{[^}]*\}', '', html, flags=re.DOTALL)
html = re.sub(r'\s*\.hero-logo-img\s*\{[^}]*\}', '', html, flags=re.DOTALL)
html = re.sub(r'\s*\.footer-logo-img\s*\{[^}]*\}', '', html, flags=re.DOTALL)

# ── 2. REPLACE the old .nav-logo img CSS with a clean version that has blend mode
old_nav_logo_img = r'\.nav-logo img \{[^}]*\}'
new_nav_logo_img = """.nav-logo img {
    width: 38px;
    height: 38px;
    object-fit: contain;
    mix-blend-mode: lighten;
    filter: drop-shadow(0 0 8px rgba(30,144,255,0.75));
    vertical-align: middle;
  }"""
html = re.sub(old_nav_logo_img, new_nav_logo_img, html, flags=re.DOTALL)

# ── 3. REPLACE .hero-logo CSS (it targets wrong class — img uses .hero-logo-img but CSS is .hero-logo)
# Fix: update the CSS to target .hero-logo-img AND add blend mode
old_hero_logo = r'\.hero-logo \{[^}]*\}'
new_hero_logo = """.hero-logo, .hero-logo-img {
    width: 100px;
    height: 100px;
    object-fit: contain;
    mix-blend-mode: lighten;
    filter: drop-shadow(0 0 24px rgba(30,144,255,0.85)) drop-shadow(0 0 8px rgba(0,191,255,0.5));
  }"""
html = re.sub(old_hero_logo, new_hero_logo, html, flags=re.DOTALL)

# ── 4. REPLACE .footer-logo img CSS with blend mode
old_footer_logo_img = r'\.footer-logo img \{[^}]*\}'
new_footer_logo_img = """.footer-logo img {
    width: 26px;
    height: 26px;
    object-fit: contain;
    mix-blend-mode: lighten;
    filter: drop-shadow(0 0 5px rgba(30,144,255,0.6));
  }"""
html = re.sub(old_footer_logo_img, new_footer_logo_img, html, flags=re.DOTALL)

# ── 5. FIX footer img — it has class="hero-logo-img" which is wrong, remove that class
html = html.replace(
    '<img src="logo.png" alt="Bunker" class="hero-logo-img" />',
    '<img src="logo.png" alt="Bunker" />'
)
# Also fix the hero img — it has class="hero-logo-img" but CSS now targets .hero-logo-img too so that's fine
# But let's also add class="hero-logo" to hero img so both selectors hit
html = html.replace(
    '<img src="logo.png" alt="Bunker" class="hero-logo-img" />',
    '<img src="logo.png" alt="Bunker" class="hero-logo-img hero-logo" />'
)

# ── 6. Verify counts
nav_count = html.count('logo.png')
blend_count = html.count('mix-blend-mode: lighten')

with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('C:/BunkerSite/fix_final_out.txt', 'w', encoding='utf-8') as f:
    f.write(f"logo.png references: {nav_count}\n")
    f.write(f"mix-blend-mode: lighten instances: {blend_count}\n")

    # Verify the 3 img tags
    imgs = re.findall(r'<img[^>]+logo\.png[^>]*>', html)
    f.write(f"\nAll logo img tags ({len(imgs)}):\n")
    for img in imgs:
        f.write(f"  {img}\n")

    # Show the 3 CSS blocks
    for pat in [r'\.nav-logo img \{[^}]*\}', r'\.hero-logo[^{]*\{[^}]*\}', r'\.footer-logo img \{[^}]*\}']:
        matches = re.findall(pat, html, flags=re.DOTALL)
        f.write(f"\nCSS match for {pat[:30]}...:\n")
        for m in matches:
            f.write(f"  {m.strip()}\n")

print("done")
