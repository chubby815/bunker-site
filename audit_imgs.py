import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== ALL IMG TAGS ===")
for i, line in enumerate(lines):
    if '<img' in line or 'logo' in line.lower() or 'nav-logo' in line or 'btree' in line.lower():
        print(f"Line {i+1}: {line.rstrip()}")

print("\n=== NAV SECTION (lines 1-50 of body) ===")
in_nav = False
for i, line in enumerate(lines):
    if '<nav' in line:
        in_nav = True
    if in_nav:
        print(f"Line {i+1}: {line.rstrip()}")
    if in_nav and '</nav>' in line:
        break

print("\n=== LOGO CSS CLASSES ===")
for i, line in enumerate(lines):
    if 'nav-logo' in line or 'hero-logo' in line or 'footer-logo' in line or 'mix-blend' in line or 'drop-shadow' in line:
        print(f"Line {i+1}: {line.rstrip()}")
