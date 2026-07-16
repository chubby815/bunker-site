import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

TALLY = "https://tally.so/r/QKWqDl"
path = "C:/BunkerSite/index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Count tally links
tally_hits = [m.start() for m in re.finditer(re.escape(TALLY), html)]
print(f"tally.so links: {len(tally_hits)}")
for pos in tally_hits:
    snippet = html[max(0, pos-60):pos+100].replace("\n", " ")
    # Strip non-ascii to avoid cp1252 explosions
    snippet = snippet.encode("ascii", "replace").decode("ascii")
    print(f"  >> {snippet}")

print()

# Check button labels near tally links
checks = [
    ("Join Waitlist", "Join Waitlist"),
    ("Join the Waitlist", "Join the Waitlist"),
    ("Join Waitlist -- Get Early Access", "Early Access pricing btn"),
    ("Notify me", "Notify me capture"),
    ('target="_blank"', "target=_blank"),
]
for needle, label in checks:
    count = html.count(needle)
    print(f"  {label}: {count} occurrence(s)")

print()

# Stale CTAs that should be gone
stale = ["Buy Bunker", "Get Bunker", "Get free access"]
for s in stale:
    count = html.count(s)
    status = "OK (0)" if count == 0 else f"STILL PRESENT: {count}"
    print(f"  '{s}': {status}")

print()
ok = len(tally_hits) >= 5 and all(html.count(s) == 0 for s in stale)
print("ALL_OK:", ok)
