import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─── 1. PORT: localhost:3131 → 127.0.0.1:3847 ───────────────────────────────
content = content.replace('localhost:3131', '127.0.0.1:3847')
print(f"[PORT] replacements: {original.count('localhost:3131')}")

# ─── 2. COPYRIGHT: 2025 → 2026 ──────────────────────────────────────────────
content = content.replace('© 2025 Bunker', '© 2026 Bunker')
print(f"[COPYRIGHT] done")

# ─── 3. MODELS — hero sub text ───────────────────────────────────────────────
# Replace the "Claude, GPT-4o, Gemini, Grok…" sentence
old_model_text = 'Claude, GPT-4o, Gemini, Grok — or run Llama 3 free with Ollama locally.'
new_model_text = 'Claude Opus 4.8, Sonnet 5, GPT-5.6, Gemini 3.5 Flash, Gemini 3.1 Pro, Grok 4.5, Grok 4 — or run Qwen2.5-Coder, DeepSeek, or Llama locally with Ollama.'
content = content.replace(old_model_text, new_model_text)
print(f"[MODELS TEXT] replaced hero sub: {'done' if new_model_text in content else 'MISS'}")

# ─── 4. MODEL PILLS ──────────────────────────────────────────────────────────
# Replace each old pill with new ones
pill_replacements = [
    # Claude 3.5 Sonnet → Claude Sonnet 5
    (
        '<div class="model-pill"><span class="dot-m orange-dot"></span>Claude 3.5 Sonnet</div>',
        '<div class="model-pill"><span class="dot-m orange-dot"></span>Claude Sonnet 5</div>'
    ),
    # GPT-4o → GPT-5.6
    (
        '<div class="model-pill"><span class="dot-m green-dot"></span>GPT-4o</div>',
        '<div class="model-pill"><span class="dot-m green-dot"></span>GPT-5.6</div>'
    ),
    # Gemini 1.5 Pro → Gemini 3.5 Flash
    (
        '<div class="model-pill"><span class="dot-m blue-dot"></span>Gemini 1.5 Pro</div>',
        '<div class="model-pill"><span class="dot-m blue-dot"></span>Gemini 3.5 Flash</div>'
    ),
    # Grok 2 → Grok 4.5
    (
        '<div class="model-pill"><span class="dot-m pink-dot"></span>Grok 2</div>',
        '<div class="model-pill"><span class="dot-m pink-dot"></span>Grok 4.5</div>'
    ),
    # Llama 3 (Ollama) → keep but rename, and add extra pills after
    (
        '<div class="model-pill"><span class="dot-m purple-dot"></span>Llama 3 (Ollama)</div>',
        '<div class="model-pill"><span class="dot-m purple-dot"></span>Llama (Ollama)</div>'
    ),
    # DeepSeek R1 → DeepSeek (already has a pill, just verify name is right)
    (
        '<div class="model-pill"><span class="dot-m blue-dot"></span>DeepSeek R1</div>',
        '<div class="model-pill"><span class="dot-m blue-dot"></span>DeepSeek (Ollama)</div>'
    ),
]

for old, new in pill_replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"[PILL] replaced: {old[:50]}...")
    else:
        print(f"[PILL] MISS: {old[:50]}...")

# After the Llama pill, inject missing pills: Claude Opus 4.8, Gemini 3.1 Pro, Grok 4, Qwen2.5-Coder
llama_pill = '<div class="model-pill"><span class="dot-m purple-dot"></span>Llama (Ollama)</div>'
extra_pills = (
    '\n          <div class="model-pill"><span class="dot-m orange-dot"></span>Claude Opus 4.8</div>'
    '\n          <div class="model-pill"><span class="dot-m blue-dot"></span>Gemini 3.1 Pro</div>'
    '\n          <div class="model-pill"><span class="dot-m pink-dot"></span>Grok 4</div>'
    '\n          <div class="model-pill"><span class="dot-m purple-dot"></span>Qwen2.5-Coder (Ollama)</div>'
)
if llama_pill in content:
    content = content.replace(llama_pill, llama_pill + extra_pills)
    print("[PILLS] extra pills injected after Llama")

# Also update the claude-3-5-sonnet model ID in the editor window code block
content = content.replace('claude-3-5-sonnet-20241022', 'claude-sonnet-5')
print(f"[MODEL ID] claude sonnet updated")

# ─── 5. PRICING — BYOA $99 tier rewrite ──────────────────────────────────────
old_byoa_header = '''          <div class="plan">BYOA — One-time</div>
          <div class="price">$99 <span>/ once</span></div>
          <div class="desc">Includes Bailey, the pre-built agent. Plug in your API key and go.</div>'''

new_byoa_header = '''          <div class="plan">BYOA — One-time</div>
          <div class="price">$99 <span>/ once</span></div>
          <div class="desc">Unlock the Agent API. Connect any AI agent — Python, Node, anything — to drive your editor.</div>'''

content = content.replace(old_byoa_header, new_byoa_header)
print(f"[PRICING] header rewrite: {'done' if new_byoa_header in content else 'MISS'}")

# Replace the "Bailey — pre-built BYOA agent" line with correct agent API copy
old_bailey_line = '          <div class="compare-item"><span class="check-blue">✓</span> <span>Bailey — pre-built BYOA agent</span></div>'
new_agent_line  = '          <div class="compare-item"><span class="check-blue">✓</span> <span>Agent API — connect any agent (Python, Node, anything)</span></div>'
content = content.replace(old_bailey_line, new_agent_line)
print(f"[PRICING] Bailey→Agent API line: {'done' if new_agent_line in content else 'MISS'}")

# Fix Free tier — remove the "Pre-built BYOA agent (Bailey)" crossed-out line, replace with clearer copy
old_free_bailey = '          <div class="compare-item"><span class="cross">✕</span> <span style="color:var(--muted)">Pre-built BYOA agent (Bailey)</span></div>'
new_free_no_api = '          <div class="compare-item"><span class="cross">✕</span> <span style="color:var(--muted)">Agent API (no external agent control)</span></div>'
content = content.replace(old_free_bailey, new_free_no_api)
print(f"[PRICING] Free tier Bailey line: {'done' if new_free_no_api in content else 'MISS'}")

# Add lifetime updates line clarity — already exists, but also add "persistent memory" context
# The $99 persistent memory line is already there, just confirm
if 'Persistent memory across sessions' in content:
    print("[PRICING] persistent memory line already present")

# ─── 6. VOTE PERCENTAGES — find and neutralise ───────────────────────────────
# Look for patterns like "73% want this" or bar fills with percentages near vote/roadmap
# Check if there's a roadmap section with percentages
roadmap_idx = content.find('id="roadmap"')
if roadmap_idx > 0:
    roadmap_chunk = content[roadmap_idx:roadmap_idx+5000]
    # Replace vote bar widths like style="width:73%" with "Vote when you join"
    # and any vote count text
    pct_in_roadmap = re.findall(r'\d+%', roadmap_chunk)
    print(f"[VOTES] percentages found in roadmap: {pct_in_roadmap}")
    # Replace vote bar style widths
    def replace_vote_bar(m):
        return m.group(0).replace(m.group(1), '0')
    roadmap_section = content[roadmap_idx:roadmap_idx+5000]
    # Replace "XX% want this" text
    fixed_roadmap = re.sub(r'\d+% want this', 'Vote when you join', roadmap_section)
    # Replace vote count numbers like "1,247 votes" 
    fixed_roadmap = re.sub(r'[\d,]+ votes?', 'Vote when you join', fixed_roadmap, flags=re.IGNORECASE)
    # Replace bar fill widths (style="width:73%") inside vote bars
    fixed_roadmap = re.sub(r'(style="[^"]*width:\s*)(\d+%)', lambda m: m.group(1) + '0%', fixed_roadmap)
    # Replace "Proposed" labels that have fake percentages nearby
    fixed_roadmap = re.sub(r'(\d+)%\s*(voted|of users|requested)', r'Proposed', fixed_roadmap, flags=re.IGNORECASE)
    content = content[:roadmap_idx] + fixed_roadmap + content[roadmap_idx+5000:]
    print("[VOTES] roadmap section processed")
else:
    print("[VOTES] no roadmap section found by id — checking for vote patterns anywhere")
    # Global sweep for vote-related percentages
    content = re.sub(r'\d+% want this', 'Vote when you join', content)
    content = re.sub(r'[\d,]+ votes?', 'Vote when you join', content, flags=re.IGNORECASE)
    print("[VOTES] global sweep done")

# ─── SAVE ────────────────────────────────────────────────────────────────────
with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n[DONE] index.html written.")

# ─── VERIFY ──────────────────────────────────────────────────────────────────
print("\n=== VERIFICATION ===")
print(f"localhost:3131 remaining:  {content.count('localhost:3131')}")
print(f"127.0.0.1:3847 count:      {content.count('127.0.0.1:3847')}")
print(f"© 2025 remaining:          {content.count('© 2025')}")
print(f"© 2026 count:              {content.count('© 2026')}")
print(f"Claude Sonnet 5:           {content.count('Claude Sonnet 5')}")
print(f"GPT-5.6:                   {content.count('GPT-5.6')}")
print(f"Gemini 3.5 Flash:          {content.count('Gemini 3.5 Flash')}")
print(f"Gemini 3.1 Pro:            {content.count('Gemini 3.1 Pro')}")
print(f"Grok 4.5:                  {content.count('Grok 4.5')}")
print(f"Grok 4 pill:               {'Grok 4</div>' in content}")
print(f"Claude Opus 4.8:           {content.count('Claude Opus 4.8')}")
print(f"Qwen2.5-Coder:             {content.count('Qwen2.5-Coder')}")
print(f"DeepSeek (Ollama):         {content.count('DeepSeek (Ollama)')}")
print(f"'includes Bailey' in $99:  {'Includes Bailey' in content}")
print(f"Agent API line present:    {'Agent API — connect any agent' in content}")
print(f"BYOA desc correct:         {'Connect any AI agent' in content}")
