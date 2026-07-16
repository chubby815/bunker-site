import re
from PIL import Image

content = open('C:/BunkerSite/index.html', encoding='utf-8').read()

imgs = re.findall(r'<img[^>]*logo\.png[^>]*>', content)
print(f"Logo img tags found: {len(imgs)}")
for i, tag in enumerate(imgs):
    print(f"  [{i+1}] {tag}")

print(f"mix-blend-mode count: {content.count('mix-blend-mode')}")
print(f"nav-logo img CSS present: {'.nav-logo img' in content}")
print(f"hero-logo CSS present: {'.hero-logo' in content}")
print(f"footer-logo img CSS present: {'.footer-logo img' in content}")

img = Image.open('C:/BunkerSite/logo.png')
print(f"logo.png mode: {img.mode}")
print(f"Has alpha channel: {'A' in img.mode}")
print("ALL CHECKS PASSED" if len(imgs) == 3 and 'A' in img.mode and content.count('mix-blend-mode') == 0 else "SOME CHECKS FAILED")
