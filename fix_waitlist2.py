import re, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

TALLY = "https://tally.so/r/QKWqDl"
path = "C:/BunkerSite/index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# ── Fix 1: Remove duplicate href on nav button
# <a href="#pricing" class="btn btn-primary" href="tally...">
html = re.sub(
    r'<a href="#pricing"\s+(class="btn btn-primary"\s+href="' + re.escape(TALLY) + r'")',
    r'<a \1',
    html
)

# ── Fix 2: Remove duplicate href on pricing section capture button
html = re.sub(
    r'<a href="#capture"\s+(class="btn btn-primary"\s+href="' + re.escape(TALLY) + r'")',
    r'<a \1',
    html
)

# ── Fix 3: $99 pricing card button label → "Join Waitlist — Get Early Access"
# Use a function replacement to avoid \u escape in repl string
EM_DASH_LABEL = "Join Waitlist \u2014 Get Early Access"

def fix_99_btn(m):
    return m.group(1) + EM_DASH_LABEL + "</a>"

pattern = r'(99.*?href="' + re.escape(TALLY) + r'"[^>]*>)\s*Join Waitlist\s*</a>'
html = re.sub(pattern, fix_99_btn, html, count=1, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

# ── Verify ──────────────────────────────────────────────────────────────────
with open(path, "r", encoding="utf-8") as f:
    final = f.read()

double_href = re.findall(r'<a[^>]+href=[^>]+href=', final)
print(f"Duplicate href on <a> tags: {len(double_href)}")

tally_count = final.count(TALLY)
early_access = final.count("Early Access")
print(f"Tally links: {tally_count}")
print(f"'Early Access' occurrences: {early_access}")

for m in re.finditer(re.escape(TALLY) + r'[^>]*>([^<]+)</a>', final):
    label = m.group(1).strip().encode("ascii", "replace").decode("ascii")
    print(f"  CTA label: '{label}'")

print()
print("ALL_OK:", len(double_href) == 0 and tally_count >= 5 and early_access >= 1)
