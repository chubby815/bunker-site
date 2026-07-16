import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    'localhost:3131 remaining': html.count('localhost:3131'),
    '2025 copyright remaining': len(re.findall(r'2025', html)),
    '2026 copyright present': html.count('2026'),
    'vote fake % remaining': len(re.findall(r'vote-pct">\d+%', html)),
    'proposed-tag present': html.count('proposed-tag'),
    'BYOA section present': html.count('BRING YOUR OWN AGENT'),
    'Includes Bailey present': html.count('Includes Bailey'),
    'Agent API present': html.count('Agent API'),
    'founder section present': html.count('id="founder"'),
    'contact section present': html.count('id="contact"'),
    'hello@bunker.dev present': html.count('hello@bunker.dev'),
    'Javier Sandoval present': html.count('Javier Sandoval'),
    'pricing section present': html.count('id="pricing"'),
    'Vote when you join present': html.count('Vote when you join'),
    'Compare-header present': html.count('compare-header'),
    'total chars': len(html),
}

print('=== VERIFY ===')
for k, v in checks.items():
    print(f'  {k}: {v}')
