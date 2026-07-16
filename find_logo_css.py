import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find hero-logo and footer-logo CSS blocks
hero = re.findall(r'\.hero-logo[\w\s]*\{[^}]*\}', content, re.DOTALL)
footer = re.findall(r'\.footer-logo[\w\s]*\{[^}]*\}', content, re.DOTALL)
nav = re.findall(r'\.nav-logo[\w\s]*\{[^}]*\}', content, re.DOTALL)

print('=== NAV LOGO CSS ===')
for b in nav:
    print(b)

print('\n=== HERO LOGO CSS ===')
for b in hero:
    print(b)

print('\n=== FOOTER LOGO CSS ===')
for b in footer:
    print(b)

# Also find the actual img tags
print('\n=== IMG TAGS ===')
imgs = re.findall(r'<img[^>]*logo[^>]*>', content)
for i in imgs:
    print(i)
