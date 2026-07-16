import sys
with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
with open('C:/BunkerSite/dump6.txt', 'w', encoding='utf-8') as f:
    f.write(content[38000:])
print('done, total len:', len(content))
