with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Get context around port
idx = content.find('localhost:3131')
print("=== PORT CONTEXT ===")
print(content[idx-100:idx+100])

# Get context around 2025
idx2 = content.find('2025')
print("\n=== COPYRIGHT CONTEXT ===")
print(content[idx2-80:idx2+80])

# Get pricing section - find $99 and surrounding
import re
for m in re.finditer(r'\$99', content):
    print(f"\n=== $99 at pos {m.start()} ===")
    print(content[m.start()-400:m.end()+600])

# Get model pills section
idx3 = content.find('model-pill')
print(f"\n=== MODEL PILLS at pos {idx3} ===")
print(content[idx3-200:idx3+800])

# Get roadmap/vote section
for kw in ['roadmap', 'Roadmap', 'vote', 'Vote', 'Proposed', '%']:
    idx4 = content.find(kw)
    if idx4 > 0:
        ctx = content[idx4-50:idx4+200]
        if any(c.isdigit() for c in ctx) and '%' in ctx:
            print(f"\n=== VOTE/ROADMAP [{kw}] at {idx4} ===")
            print(ctx)
            break

# Search for vote percentages more carefully
vote_section = re.search(r'(roadmap|vote|feature).{0,2000}', content, re.IGNORECASE | re.DOTALL)
if vote_section:
    print("\n=== ROADMAP SECTION ===")
    print(vote_section.group()[:3000])
