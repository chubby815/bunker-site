import re

TALLY = "https://tally.so/r/QKWqDl"
path = "C:/BunkerSite/index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# ── Fix 1: nav button has duplicate href (href="#pricing" AND href=tally)
# Pattern: <a href="#pricing" class="btn btn-primary" href="tally...">Join Waitlist</a>
# Remove the first stale href="#pricing"
html = re.sub(
    r'<a href="#pricing"\s+(class="btn btn-primary"\s+href="' + re.escape(TALLY) + r'")',
    r'<a \1',
    html
)

# ── Fix 2: pricing section button has duplicate href (href="#capture" AND href=tally)
html = re.sub(
    r'<a href="#capture"\s+(class="btn btn-primary"\s+href="' + re.escape(TALLY) + r'")',
    r'<a \1',
    html
)

# ── Fix 3: $99 pricing button — find the btn in the $99 card and relabel it
# The $99 card button currently says "Join Waitlist" — change to "Join Waitlist — Get Early Access"
# It should be the btn-outline in the pricing card that has $99 context
# Find it by looking for the tally link inside a card with "99" nearby
# Safer: find 4th tally occurrence (the $99 pricing one) and fix its label
# Actually let's just do a targeted replace on the specific text
html = html.replace(
    f'href="{TALLY}" target="_blank" class="btn btn-outline" style="width:100%; justify-conten',
    f'href="{TALLY}" target="_blank" class="btn btn-primary" style="width:100%; justify-conten',
)

# Fix the label on the $99 card button - find "Join Waitlist</a>" that follows the $99 price marker
# Strategy: find the pricing $99 card block and replace just that button text
pattern = r'(99.*?href="' + re.escape(TALLY) + r'"[^>]*>)\s*Join Waitlist\s*</a>'
html = re.sub(pattern, r'\1Join Waitlist \u2014 Get Early Access</a>', html, count=1, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

# ── Verify ──────────────────────────────────────────────────────────────────
with open(path, "r", encoding="utf-8") as f:
    final = f.read()

# Check for duplicate href on same <a> tag
double_href = re.findall(r'<a[^>]+href=[^>]+href=', final)
print(f"Duplicate href on <a> tags: {len(double_href)}")

tally_count = final.count(TALLY)
early_access = final.count("Early Access")
print(f"Tally links: {tally_count}")
print(f"'Early Access' occurrences: {early_access}")

# Show all tally link labels
for m in re.finditer(re.escape(TALLY) + r'[^>]*>([^<]+)</a>', final):
    print(f"  CTA label: '{m.group(1).strip()}'")

print("DONE")
