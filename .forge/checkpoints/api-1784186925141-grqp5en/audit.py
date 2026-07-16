import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("=== PORT ===")
port_matches = [(m.start(), m.group()) for m in re.finditer(r'localhost:\d+', content)]
print(f"Found {len(port_matches)}:", port_matches[:10])

print("\n=== MODELS ===")
model_kw = ['Claude', 'GPT', 'Gemini', 'Grok', 'Ollama', 'DeepSeek', 'Llama', 'qwen', 'Opus', 'Sonnet']
for kw in model_kw:
    hits = re.findall(r'.{0,50}' + kw + r'.{0,50}', content, re.IGNORECASE)
    if hits:
        print(f"[{kw}]: {hits[:2]}")

print("\n=== COPYRIGHT ===")
copy_hits = re.findall(r'.{0,10}[©&copy;2025].{0,30}', content)
print(copy_hits[:5])
copy2 = re.findall(r'2025', content)
print(f"Raw '2025' count: {len(copy2)}")

print("\n=== PERCENTAGES / VOTES ===")
pct_hits = [(m.start(), content[max(0,m.start()-60):m.end()+60]) for m in re.finditer(r'\d+%', content)]
print(f"Found {len(pct_hits)} percentage hits:")
for pos, ctx in pct_hits[:10]:
    print(f"  pos {pos}: ...{ctx.strip()}...")

print("\n=== PRICING / BYOA / BAILEY ===")
pricing_hits = re.findall(r'.{0,80}(BYOA|byoa|\$99|Bailey|agent.api|Free tier|pricing|one.time).{0,80}', content, re.IGNORECASE)
for h in pricing_hits[:15]:
    print(f"  {repr(h[:120])}")
