import re

TALLY = "https://tally.so/r/QKWqDl"
path = "C:/BunkerSite/index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

original = html

# ── 1. NAV: "Get Bunker $99" → "Join Waitlist" ──────────────────────────────
# Targets the nav CTA anchor (look for btn-primary inside nav)
html = re.sub(
    r'(<nav[^>]*>.*?)(href="[^"]*")(>[^<]*(?:Get Bunker[^<]*\$99|Get Bunker)[^<]*</a>)',
    lambda m: m.group(1) + f'href="{TALLY}" target="_blank"' + '>Join Waitlist</a>',
    html, flags=re.DOTALL
)

# Broader nav button catch — any btn-primary in the nav bar area
html = re.sub(
    r'(class="btn btn-primary"[^>]*>)\s*Get Bunker[^<]*\$99\s*</a>',
    f'class="btn btn-primary" href="{TALLY}" target="_blank">Join Waitlist</a>',
    html
)

# ── 2. HERO: "Buy Bunker $99" → "Join the Waitlist" ─────────────────────────
html = re.sub(
    r'href="[^"]*"([^>]*)>\s*(?:&#x1F4E6;[\s\S]*?)?Buy Bunker[^<]*\$99\s*</a>',
    f'href="{TALLY}" target="_blank"\\1>&#x1F4E6; Join the Waitlist</a>',
    html
)

# ── 3. PRICING – $99 button: "Get Bunker" / "Get Bunker — $99" ───────────────
html = re.sub(
    r'href="[^"]*"([^>]*)>\s*Get Bunker\s*(?:—\s*\$99)?\s*</a>',
    f'href="{TALLY}" target="_blank"\\1>Join Waitlist — Get Early Access</a>',
    html
)

# ── 4. PRICING – Free tier: "Get free access" ────────────────────────────────
html = re.sub(
    r'href="[^"]*"([^>]*)>\s*Get free access\s*</a>',
    f'href="{TALLY}" target="_blank"\\1>Join Waitlist</a>',
    html
)

# ── 5. COMMUNITY: "Join the waitlist" (case-insensitive) ─────────────────────
html = re.sub(
    r'href="[^"]*"([^>]*)>\s*Join the waitlist\s*</a>',
    f'href="{TALLY}" target="_blank"\\1>Join the Waitlist</a>',
    html, flags=re.IGNORECASE
)

# ── 6. EMAIL CAPTURE: "Notify me" button ─────────────────────────────────────
# Change the Notify me button/submit to a link to Tally
html = re.sub(
    r'<button[^>]*>\s*Notify me\s*</button>',
    f'<a href="{TALLY}" target="_blank" class="btn btn-primary">Notify me</a>',
    html
)

# Also catch any input type=submit with value "Notify me"
html = re.sub(
    r'<input[^>]*value="Notify me"[^>]*>',
    f'<a href="{TALLY}" target="_blank" class="btn btn-primary">Notify me</a>',
    html
)

# ── 7. Any stray "Get Bunker $99" or "Get Bunker" CTA anchors ────────────────
html = re.sub(
    r'href="#[^"]*"([^>]*)>\s*Get Bunker[^<]*</a>',
    f'href="{TALLY}" target="_blank"\\1>Join Waitlist</a>',
    html
)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

# ── Verify ───────────────────────────────────────────────────────────────────
with open(path, "r", encoding="utf-8") as f:
    final = f.read()

tally_count = final.count(TALLY)
old_buy     = final.count("Buy Bunker")
old_get99   = final.count("Get Bunker")
old_free    = final.count("Get free access")
notify_btn  = final.count('<button') and "Notify me" in final

print(f"Tally links found       : {tally_count}")
print(f"'Buy Bunker' remaining  : {old_buy}")
print(f"'Get Bunker' remaining  : {old_get99}  (should be 0 in CTAs)")
print(f"'Get free access' left  : {old_free}")
print(f"'Notify me' as button   : {'YES — needs check' if notify_btn else 'NO (converted)'}")
print(f"Changed bytes           : {abs(len(final) - len(original))}")
print("DONE")
