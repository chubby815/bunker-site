with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
print('TOTAL CHARS:', len(content))
# Print in 8000-char chunks
chunk = 8000
for i in range(0, len(content), chunk):
    print(f'=== CHUNK {i//chunk} ===')
    print(content[i:i+chunk])
