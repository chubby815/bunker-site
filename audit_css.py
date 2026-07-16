with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
# Extract lines 155-210 (nav-logo CSS area) and 355-375 (hero-logo) and 705-730 (footer) and 870-910 (injected CSS)
ranges = [(155,215),(355,380),(705,735),(870,915),(950,965),(1300,1315)]
for start, end in ranges:
    out.append(f"\n--- LINES {start}-{end} ---")
    for i in range(start-1, min(end, len(lines))):
        out.append(f"L{i+1}: {lines[i].rstrip()}")

with open('C:/BunkerSite/css_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("done")
