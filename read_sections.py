import re, sys

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = []

# PORT context
idx = content.find('localhost:3131')
out.append("=== PORT CONTEXT ===")
out.append(content[idx-100:idx+100])

# COPYRIGHT context
idx2 = content.find('2025')
out.append("\n=== COPYRIGHT CONTEXT ===")
out.append(content[idx2-80:idx2+80])

# All $99 hits with context
for m in re.finditer(r'\$99', content):
    out.append(f"\n=== $99 at pos {m.start()} ===")
    out.append(content[m.start()-500:m.end()+800])

# Model pills
idx3 = content.find('model-pill')
out.append(f"\n=== MODEL PILLS at pos {idx3} ===")
out.append(content[max(0,idx3-200):idx3+1200])

# Roadmap section
for tag in ['roadmap', 'Roadmap', 'road-map', 'feature-vote', 'vote']:
    idx4 = content.find(tag)
    if idx4 > 0:
        out.append(f"\n=== ROADMAP [{tag}] at {idx4} ===")
        out.append(content[max(0,idx4-100):idx4+2000])
        break

# BYOA / Bailey / agent in pricing
for m in re.finditer(r'(byoa|BYOA|Bailey|agent api|agent-api)', content, re.IGNORECASE):
    out.append(f"\n=== BYOA/BAILEY at {m.start()} ===")
    out.append(content[max(0,m.start()-300):m.end()+300])

result = "\n".join(out)
with open('C:/BunkerSite/sections.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print("Done - written to sections.txt")
