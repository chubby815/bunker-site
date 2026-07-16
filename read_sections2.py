import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = []

# Get pricing section by id
m = re.search(r'id=["\']pricing["\']', content)
if m:
    out.append(f"=== PRICING SECTION at {m.start()} ===")
    out.append(content[m.start():m.start()+4000])

# Get models/hero text block with full model list
m2 = re.search(r'Claude.*?GPT.*?Gemini.*?Grok', content, re.DOTALL)
if m2:
    out.append(f"\n=== MODELS TEXT at {m2.start()} ===")
    out.append(content[max(0,m2.start()-50):m2.end()+200])

# Get all model-pill content
pills = re.findall(r'model-pill[^>]*>.*?</div>', content, re.DOTALL)
out.append("\n=== ALL MODEL PILLS ===")
for p in pills:
    out.append(p.strip())

# Roadmap section
m3 = re.search(r'id=["\']roadmap["\']', content)
if m3:
    out.append(f"\n=== ROADMAP SECTION at {m3.start()} ===")
    out.append(content[m3.start():m3.start()+3000])

# Look for any vote percentages in context
pct_items = re.finditer(r'(\d{1,3})%', content)
for m4 in pct_items:
    ctx = content[max(0,m4.start()-150):m4.end()+150]
    if any(w in ctx.lower() for w in ['vote', 'want', 'request', 'feature', 'road', 'poll']):
        out.append(f"\n=== VOTE PCT at {m4.start()} ===")
        out.append(ctx)

result = "\n".join(out)
with open('C:/BunkerSite/sections2.txt', 'w', encoding='utf-8') as f:
    f.write(result)
print("Done")
