import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('C:/BunkerSite/index.html', encoding='utf-8').read()

# Find the community/roadmap HTML section (vote items in HTML body)
print('=== VOTE ITEMS IN HTML ===')
ci = content.find('community')
# find the actual vote-items div
vi = content.find('<div class="vote-items">')
print(content[vi:vi+2500])

# Pricing section
print('\n\n=== PRICING SECTION ===')
pi = content.lower().find('id="pricing"')
print(content[pi:pi+4000])

# Footer
print('\n\n=== FOOTER SECTION ===')
fi = content.lower().find('<footer')
print(content[fi:])
