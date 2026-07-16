import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('C:/BunkerSite/index.html', encoding='utf-8').read()

# Roadmap/votes section
print('=== ROADMAP VOTES SECTION ===')
ri = content.find('vote-item')
print(content[max(0,ri-200):ri+3000])

# Pricing section
print('\n\n=== PRICING SECTION ===')
pi = content.lower().find('id="pricing"')
print(content[pi:pi+3000])

# Footer
print('\n\n=== FOOTER SECTION ===')
fi = content.lower().find('<footer')
print(content[fi:fi+3000])
