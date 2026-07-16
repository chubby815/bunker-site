import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ── 1. Hero logo: 100px → 160px ─────────────────────────────────────────────
content = re.sub(
    r'(\.hero-logo\s*\{[^}]*height:\s*)100px',
    r'\g<1>160px',
    content,
    flags=re.DOTALL
)

# ── 2. Footer logo img: 26px → 40px (both width/height declarations) ─────────
def fix_footer_img(m):
    block = m.group(0)
    block = re.sub(r'width:\s*26px', 'width: 40px', block)
    block = re.sub(r'height:\s*26px', 'height: 40px', block)
    return block

content = re.sub(
    r'\.footer-logo img\s*\{[^}]*\}',
    fix_footer_img,
    content,
    flags=re.DOTALL
)

# ── 3. Remove duplicate .nav-logo img block (keep first, remove second) ──────
nav_img_pattern = r'(\.nav-logo img\s*\{[^}]*\})'
all_nav_img = list(re.finditer(nav_img_pattern, content, re.DOTALL))
print(f"Found {len(all_nav_img)} .nav-logo img blocks")
if len(all_nav_img) > 1:
    # Remove all but the first
    for match in reversed(all_nav_img[1:]):
        content = content[:match.start()] + content[match.end():]
    print("Removed duplicate .nav-logo img blocks")

# ── Verify changes ────────────────────────────────────────────────────────────
hero_check = re.findall(r'\.hero-logo\s*\{[^}]*\}', content, re.DOTALL)
footer_check = re.findall(r'\.footer-logo img\s*\{[^}]*\}', content, re.DOTALL)

print('\n=== HERO LOGO CSS (after) ===')
for b in hero_check:
    print(b)

print('\n=== FOOTER LOGO CSS (after) ===')
for b in footer_check:
    print(b)

# ── Save ──────────────────────────────────────────────────────────────────────
if content != original:
    with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('\n✅ index.html saved')
else:
    print('\n⚠️  No changes detected — check regex patterns')
