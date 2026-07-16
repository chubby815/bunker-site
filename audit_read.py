import sys

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out = open('C:/BunkerSite/audit_out.txt', 'w', encoding='utf-8')

out.write('TOTAL CHARS: ' + str(len(content)) + '\n')

checks = [
    ('localhost:3131', content.count('localhost:3131')),
    ('3847', content.count('3847')),
    ('2025', content.count('2025')),
    ('2026', content.count('2026')),
    ('Claude', content.count('Claude')),
    ('GPT', content.count('GPT')),
    ('Grok', content.count('Grok')),
    ('Gemini', content.count('Gemini')),
    ('Ollama', content.count('Ollama')),
    ('Vote', content.count('Vote')),
    ('video', content.lower().count('video')),
    ('contact', content.lower().count('contact')),
    ('screenshot', content.lower().count('screenshot')),
    ('hello@bunker', content.count('hello@bunker')),
]

for k, v in checks:
    out.write('  ' + k + ': ' + str(v) + '\n')

lines = content.split('\n')
for i, line in enumerate(lines):
    lower = line.lower()
    if any(x in lower for x in ['localhost', '2025', '2026', 'vote', 'opus', 'gpt', 'grok', 'gemini', 'ollama', 'copyright', 'contact', 'video', 'screenshot', 'hello@']):
        out.write('L' + str(i+1) + ': ' + line.strip()[:140] + '\n')

out.close()
print('done')
