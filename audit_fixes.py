import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check vote heading
for needle in ['CURRENT FEATURE VOTES', 'PROPOSED', 'vote-pct', 'vote-bar', '91%', '78%', '65%', '54%', '48%']:
    idx = html.find(needle)
    print(f'{needle!r}: {"FOUND at " + str(idx) if idx >= 0 else "NOT FOUND"}')

# Show vote section context
idx = html.find('CURRENT FEATURE VOTES')
if idx >= 0:
    print('\n--- VOTE SECTION (500 chars) ---')
    print(html[max(0,idx-100):idx+500])

# Check gpt-4o
idx2 = html.find('gpt-4o')
print(f'\ngpt-4o: {"FOUND at " + str(idx2) if idx2 >= 0 else "NOT FOUND"}')
if idx2 >= 0:
    print(html[max(0,idx2-100):idx2+200])

# Check gpt-5.6
idx3 = html.find('gpt-5.6')
print(f'\ngpt-5.6: {"FOUND at " + str(idx3) if idx3 >= 0 else "NOT FOUND"}')
