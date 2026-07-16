import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('C:/BunkerSite/index.html', encoding='utf-8').read()

# 1. All % occurrences with context
print('=== VOTE % MATCHES ===')
for m in re.finditer(r'\d+\s*%', content):
    ctx = content[max(0,m.start()-80):m.end()+80].replace('\n','|')
    print(f'  pos={m.start()}: {ctx}')

# 2. Full pricing section
print('\n=== PRICING SECTION ===')
pi = content.lower().find('id="pricing"')
if pi == -1:
    pi = content.lower().find('pricing')
print(content[pi:pi+2000])

# 3. Footer — last 3000 chars
print('\n=== FOOTER / END ===')
print(content[-3000:])
