import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── Fix Bailey line in $99 tier (script crashed before this ran) ─────────────
old_bailey_line = '          <div class="compare-item"><span class="check-blue">✓</span> <span>Bailey — pre-built BYOA agent</span></div>'
new_agent_line  = '          <div class="compare-item"><span class="check-blue">✓</span> <span>Agent API — connect any agent (Python, Node, anything)</span></div>'
if old_bailey_line in content:
    content = content.replace(old_bailey_line, new_agent_line)
    print("[PRICING] Bailey line replaced with Agent API")
else:
    # Maybe it already got partially written — check current state
    print("[PRICING] Bailey line not found (may already be fixed or different whitespace)")
    # Check what's actually there
    idx = content.find('check-blue')
    if idx > 0:
        print("Current check-blue lines:")
        for m in re.finditer(r'check-blue[^<]+<[^<]+</div>', content):
            print(" ", m.group())

# Fix Free tier crossed-out line
old_free_bailey = '          <div class="compare-item"><span class="cross">✕</span> <span style="color:var(--muted)">Pre-built BYOA agent (Bailey)</span></div>'
new_free_no_api = '          <div class="compare-item"><span class="cross">✕</span> <span style="color:var(--muted)">Agent API (no external agent control)</span></div>'
if old_free_bailey in content:
    content = content.replace(old_free_bailey, new_free_no_api)
    print("[PRICING] Free tier Bailey crossed-out line fixed")
else:
    print("[PRICING] Free tier Bailey line not found")
    # Check what cross lines exist
    for m in re.finditer(r'cross[^<]+<[^<]+</div>', content):
        print(" ", m.group())

# ─── Vote percentages global sweep ───────────────────────────────────────────
vote_before = len(re.findall(r'\d+% want this', content))
content = re.sub(r'\d+% want this', 'Vote when you join', content)
content = re.sub(r'[\d,]+ votes?', 'Vote when you join', content, flags=re.IGNORECASE)
print(f"[VOTES] swept {vote_before} 'want this' patterns")

# ─── SAVE ────────────────────────────────────────────────────────────────────
with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved.")

# ─── VERIFY (write to file to avoid codec issues) ────────────────────────────
results = []
results.append(f"localhost:3131 remaining:  {content.count('localhost:3131')}")
results.append(f"127.0.0.1:3847 count:      {content.count('127.0.0.1:3847')}")
results.append(f"2025 remaining:            {content.count('2025')}")
results.append(f"2026 count:                {content.count('2026')}")
results.append(f"Claude Sonnet 5:           {content.count('Claude Sonnet 5')}")
results.append(f"Claude Opus 4.8:           {content.count('Claude Opus 4.8')}")
results.append(f"GPT-5.6:                   {content.count('GPT-5.6')}")
results.append(f"Gemini 3.5 Flash:          {content.count('Gemini 3.5 Flash')}")
results.append(f"Gemini 3.1 Pro:            {content.count('Gemini 3.1 Pro')}")
results.append(f"Grok 4.5:                  {content.count('Grok 4.5')}")
results.append(f"Grok 4 pill:               {'Grok 4</div>' in content}")
results.append(f"Qwen2.5-Coder:             {content.count('Qwen2.5-Coder')}")
results.append(f"DeepSeek (Ollama):         {content.count('DeepSeek (Ollama)')}")
results.append(f"Llama (Ollama):            {content.count('Llama (Ollama)')}")
results.append(f"'Includes Bailey' in $99:  {'Includes Bailey' in content}")
results.append(f"Agent API line present:    {'Agent API — connect any agent' in content}")
results.append(f"Connect any AI agent desc: {'Connect any AI agent' in content}")
results.append(f"claude-sonnet-5 model id:  {'claude-sonnet-5' in content}")

with open('C:/BunkerSite/verify.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("Verify results written to verify.txt")
