import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

log = []

# 1. PORT
before = content.count('localhost:3131')
content = content.replace('localhost:3131', '127.0.0.1:3847')
log.append(f"PORT: replaced {before} instances of localhost:3131 with 127.0.0.1:3847")

# 2. COPYRIGHT
before2 = content.count('2025')
content = content.replace('2025 Bunker', '2026 Bunker')
log.append(f"COPYRIGHT: 2025->2026 (was {before2} raw '2025' hits, replaced in footer)")

# 3. MODELS hero sub text
old_txt = 'Claude, GPT-4o, Gemini, Grok \u2014 or run Llama 3 free with Ollama locally.'
new_txt = 'Claude Opus 4.8, Sonnet 5, GPT-5.6, Gemini 3.5 Flash, Gemini 3.1 Pro, Grok 4.5, Grok 4 \u2014 or run Qwen2.5-Coder, DeepSeek, or Llama locally with Ollama.'
if old_txt in content:
    content = content.replace(old_txt, new_txt)
    log.append("MODELS TEXT: hero sub updated")
else:
    # Try without em dash
    old_txt2 = 'Claude, GPT-4o, Gemini, Grok'
    idx = content.find(old_txt2)
    if idx >= 0:
        log.append(f"MODELS TEXT: found at {idx}, doing broader replace")
        content = re.sub(
            r'Claude, GPT-4o, Gemini, Grok[^<.]*(?:Ollama locally\.)?',
            new_txt,
            content
        )
    else:
        log.append("MODELS TEXT: MISS - could not find old text")

# 4. MODEL PILLS
pill_map = [
    ('Claude 3.5 Sonnet', 'Claude Sonnet 5'),
    ('GPT-4o',            'GPT-5.6'),
    ('Gemini 1.5 Pro',    'Gemini 3.5 Flash'),
    ('Grok 2',            'Grok 4.5'),
    ('Llama 3 (Ollama)',  'Llama (Ollama)'),
    ('DeepSeek R1',       'DeepSeek (Ollama)'),
]
for old_name, new_name in pill_map:
    if old_name in content:
        content = content.replace(old_name, new_name)
        log.append(f"PILL: {old_name} -> {new_name}")
    else:
        log.append(f"PILL MISS: {old_name}")

# Inject extra pills after Llama (Ollama)
llama_pill = '<div class="model-pill"><span class="dot-m purple-dot"></span>Llama (Ollama)</div>'
extra = (
    '\n          <div class="model-pill"><span class="dot-m orange-dot"></span>Claude Opus 4.8</div>'
    '\n          <div class="model-pill"><span class="dot-m blue-dot"></span>Gemini 3.1 Pro</div>'
    '\n          <div class="model-pill"><span class="dot-m pink-dot"></span>Grok 4</div>'
    '\n          <div class="model-pill"><span class="dot-m purple-dot"></span>Qwen2.5-Coder (Ollama)</div>'
)
if llama_pill in content and 'Claude Opus 4.8' not in content:
    content = content.replace(llama_pill, llama_pill + extra)
    log.append("PILLS: injected Opus 4.8, Gemini 3.1 Pro, Grok 4, Qwen2.5-Coder")
elif 'Claude Opus 4.8' in content:
    log.append("PILLS: extra pills already present")
else:
    log.append("PILLS MISS: could not find llama pill to inject after")

# Update model id in editor window
content = content.replace('claude-3-5-sonnet-20241022', 'claude-sonnet-5')
log.append("MODEL ID: editor window updated")

# 5. PRICING BYOA tier header
old_desc = 'Includes Bailey, the pre-built agent. Plug in your API key and go.'
new_desc = 'Unlock the Agent API. Connect any AI agent \u2014 Python, Node, anything \u2014 to drive your editor.'
if old_desc in content:
    content = content.replace(old_desc, new_desc)
    log.append("PRICING: BYOA desc updated")
else:
    log.append("PRICING MISS: old desc not found")

# Bailey line in $99 col
old_b = '<div class="compare-item"><span class="check-blue">\u2713</span> <span>Bailey \u2014 pre-built BYOA agent</span></div>'
new_b = '<div class="compare-item"><span class="check-blue">\u2713</span> <span>Agent API \u2014 connect any agent (Python, Node, anything)</span></div>'
if old_b in content:
    content = content.replace(old_b, new_b)
    log.append("PRICING: Bailey->Agent API line replaced")
else:
    log.append("PRICING MISS: Bailey check-blue line not found (check manually)")

# Crossed-out Bailey in Free tier
old_f = '<span style="color:var(--muted)">Pre-built BYOA agent (Bailey)</span>'
new_f = '<span style="color:var(--muted)">Agent API (no external agent control)</span>'
if old_f in content:
    content = content.replace(old_f, new_f)
    log.append("PRICING: Free tier Bailey crossed-out line fixed")
else:
    log.append("PRICING MISS: Free tier Bailey line not found")

# 6. VOTE PERCENTAGES
content = re.sub(r'\d+% want this', 'Vote when you join', content)
content = re.sub(r'[\d,]+ votes?', 'Vote when you join', content, flags=re.IGNORECASE)
log.append("VOTES: global sweep done")

# SAVE
with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# VERIFY
v = []
v.append(f"localhost:3131 remaining:  {content.count('localhost:3131')}")
v.append(f"127.0.0.1:3847:            {content.count('127.0.0.1:3847')}")
v.append(f"2025 remaining:            {content.count('2025')}")
v.append(f"2026:                      {content.count('2026')}")
v.append(f"Claude Sonnet 5:           {content.count('Claude Sonnet 5')}")
v.append(f"Claude Opus 4.8:           {content.count('Claude Opus 4.8')}")
v.append(f"GPT-5.6:                   {content.count('GPT-5.6')}")
v.append(f"Gemini 3.5 Flash:          {content.count('Gemini 3.5 Flash')}")
v.append(f"Gemini 3.1 Pro:            {content.count('Gemini 3.1 Pro')}")
v.append(f"Grok 4.5:                  {content.count('Grok 4.5')}")
v.append(f"Grok 4 pill:               {'Grok 4</div>' in content}")
v.append(f"Qwen2.5-Coder:             {content.count('Qwen2.5-Coder')}")
v.append(f"DeepSeek (Ollama):         {content.count('DeepSeek (Ollama)')}")
v.append(f"Llama (Ollama):            {content.count('Llama (Ollama)')}")
v.append(f"Includes Bailey in $99:    {'Includes Bailey' in content}")
v.append(f"Agent API line:            {'Agent API' in content}")
v.append(f"Connect any AI agent desc: {'Connect any AI agent' in content}")
v.append(f"claude-sonnet-5 model id:  {'claude-sonnet-5' in content}")

with open('C:/BunkerSite/verify.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log) + '\n\n=== VERIFY ===\n' + '\n'.join(v))

print("DONE - see verify.txt")
