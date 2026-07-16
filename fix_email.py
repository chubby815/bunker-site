with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old = 'hello@bunker.dev'
new = 'hello@getbunkerai.com'
count = html.count(old)
html = html.replace(old, new)

with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Replaced: {count} occurrence(s)')
print(f'Old remaining: {html.count(old)}')
print(f'New present: {html.count(new)}')
