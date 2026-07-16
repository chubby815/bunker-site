import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# Fix 1: Vote section heading
old_heading = 'CURRENT FEATURE VOTES'
new_heading = 'PROPOSED &mdash; VOTE WHEN YOU JOIN'
count_heading = html.count(old_heading)
html = html.replace(old_heading, new_heading)
print(f'VOTE HEADING: replaced {count_heading} occurrence(s)')

# Fix 2: gpt-4o -> gpt-5.6 in code example
old_model = '>gpt-4o<'
new_model = '>gpt-5.6<'
count_model = html.count(old_model)
html = html.replace(old_model, new_model)
print(f'GPT MODEL: replaced {count_model} occurrence(s) of gpt-4o -> gpt-5.6')

# Verify
print('\n--- VERIFICATION ---')
print(f'CURRENT FEATURE VOTES still present: {html.count("CURRENT FEATURE VOTES")}')
print(f'PROPOSED heading present: {html.count("PROPOSED")}')
print(f'gpt-4o still present: {html.count("gpt-4o")}')
print(f'gpt-5.6 present: {html.count("gpt-5.6")}')

with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nFile written. Size: {len(html)} bytes (was {original_len})')
print('ALL_OK:', html.count("CURRENT FEATURE VOTES") == 0 and html.count("gpt-4o") == 0 and html.count("gpt-5.6") >= 1)
