import sys
sys.stdout.reconfigure(encoding='utf-8')

content = open('C:/BunkerSite/index.html', encoding='utf-8').read()

# Full pricing col 2 (BYOA)
pi = content.lower().find('id="pricing"')
print('=== FULL PRICING ===')
print(content[pi:pi+6000])
