import re, sys

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []

out.append("=== ALL IMG TAGS + LOGO REFERENCES ===")
for i, line in enumerate(lines):
    low = line.lower()
    if '<img' in line or 'nav-logo' in low or 'hero-logo' in low or 'footer-logo' in low or 'mix-blend' in low or 'logo.png' in low or 'btree' in low:
        out.append(f"L{i+1}: {line.rstrip()}")

out.append("\n=== NAV HTML ===")
in_nav = False
for i, line in enumerate(lines):
    if '<nav' in line:
        in_nav = True
    if in_nav:
        out.append(f"L{i+1}: {line.rstrip()}")
    if in_nav and '</nav>' in line:
        break

with open('C:/BunkerSite/audit_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("done")
