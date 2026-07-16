import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

log = []

# 1. Add Grok 4 pill right after Grok 4.5 pill (it's missing)
grok45_pill = '<div class="model-pill"><span class="dot-m pink-dot"></span>Grok 4.5</div>'
grok4_pill  = '\n          <div class="model-pill"><span class="dot-m pink-dot"></span>Grok 4</div>'

if grok45_pill in content and 'Grok 4</div>' not in content:
    content = content.replace(grok45_pill, grok45_pill + grok4_pill)
    log.append("PATCH: Grok 4 pill injected after Grok 4.5")
elif 'Grok 4</div>' in content:
    log.append("Grok 4 pill already present")
else:
    log.append("MISS: Grok 4.5 pill not found")

# 2. Confirm Free tier crossed-out line is correct
free_chunk_idx = content.find('compare-col">')
if free_chunk_idx > 0:
    free_chunk = content[free_chunk_idx:free_chunk_idx+1500]
    if 'Agent API (no external agent control)' in free_chunk:
        log.append("Free tier: Agent API crossed-out line OK")
    elif 'Pre-built BYOA agent (Bailey)' in free_chunk:
        # Still old, fix it
        content = content.replace(
            '<span style="color:var(--muted)">Pre-built BYOA agent (Bailey)</span>',
            '<span style="color:var(--muted)">Agent API (no external agent control)</span>'
        )
        log.append("Free tier: patched Bailey crossed-out line")
    else:
        log.append(f"Free tier cross lines: {re.findall(r'cross[^<]*<[^<]+', free_chunk)}")

# SAVE
with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# FINAL VERIFY
v = []
v.append(f"localhost:3131:             {content.count('localhost:3131')}")
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
v.append(f"Agent API line in $99:     {'Agent API' in content}")
v.append(f"Connect any AI agent:      {'Connect any AI agent' in content}")
v.append(f"claude-sonnet-5:           {'claude-sonnet-5' in content}")
v.append(f"Free tier no-agent-api:    {'Agent API (no external agent control)' in content}")

all_ok = (
    content.count('localhost:3131') == 0 and
    content.count('127.0.0.1:3847') == 1 and
    content.count('2025') == 0 and
    content.count('Claude Sonnet 5') >= 1 and
    content.count('GPT-5.6') >= 1 and
    content.count('Grok 4.5') >= 1 and
    'Grok 4</div>' in content and
    'Includes Bailey' not in content and
    'Connect any AI agent' in content
)
v.append(f"\nALL_OK: {all_ok}")

with open('C:/BunkerSite/verify.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log) + '\n\n=== FINAL VERIFY ===\n' + '\n'.join(v))
print("Done")
