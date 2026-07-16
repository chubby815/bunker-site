with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Nav img: has class="nav-logo-img" — CSS targets .nav-logo img (descendant)
# The nav-logo-img class is orphaned. The descendant selector .nav-logo img WILL still work
# because the img is inside .nav-logo anchor. So nav logo IS correctly styled.
# But let's clean the orphan class anyway for hygiene — remove class attr since .nav-logo img covers it
html = html.replace(
    '<img src="logo.png" alt="Bunker logo" class="nav-logo-img" />',
    '<img src="logo.png" alt="Bunker logo" />'
)

# Hero img: currently has no class after our last fix (we replaced hero-logo-img with empty)
# CSS targets .hero-logo and .hero-logo-img — need to add class="hero-logo" to hero img
# Find the hero img (inside .hero-logo-wrap)
html = html.replace(
    '<img src="logo.png" alt="Bunker" />',
    '<img src="logo.png" alt="Bunker" class="hero-logo" />',
    1  # only first occurrence = hero (footer is the second)
)
# Footer img: leave without class — .footer-logo img descendant selector covers it

with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify final state
import re
imgs = re.findall(r'<img[^>]+logo\.png[^>]*>', html)
with open('C:/BunkerSite/final_verify.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total logo img tags: {len(imgs)}\n")
    for i, img in enumerate(imgs):
        f.write(f"  [{i}] {img}\n")
    f.write(f"\nmix-blend-mode count: {html.count('mix-blend-mode: lighten')}\n")
    f.write(f"logo.png count: {html.count('logo.png')}\n")

print("done")
