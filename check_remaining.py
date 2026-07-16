import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = []

# Check Grok 4 pill - what's actually there
grok_hits = re.findall(r'[^\n]*[Gg]rok[^\n]*', content)
out.append("=== GROK LINES ===")
for h in grok_hits:
    out.append(h.strip())

# Check pricing compare-item lines
pricing_idx = content.find('id="pricing"')
pricing_chunk = content[pricing_idx:pricing_idx+3000]
out.append("\n=== PRICING COMPARE ITEMS ===")
items = re.findall(r'compare-item[^<]*>[^<]+<[^<]+</div>', pricing_chunk)
for item in items:
    out.append(item.strip())

# Full $99 tier block
byoa_idx = content.find('BYOA \u2014 One-time')
if byoa_idx < 0:
    byoa_idx = content.find('BYOA')
out.append(f"\n=== BYOA BLOCK at {byoa_idx} ===")
out.append(content[byoa_idx:byoa_idx+800])

with open('C:/BunkerSite/check.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done")
