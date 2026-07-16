import re

with open('C:/BunkerSite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. PORT ──────────────────────────────────────────────────────────────────
html = html.replace('localhost:3131', '127.0.0.1:3847')
port_count = original.count('localhost:3131')
print(f'PORT: replaced {port_count} occurrences')

# ── 2. COPYRIGHT ──────────────────────────────────────────────────────────────
html = re.sub(r'©\s*2025', '© 2026', html)
copy_count = len(re.findall(r'©\s*2025', original))
print(f'COPYRIGHT: replaced {copy_count} occurrences')

# ── 3. HERO LOGO SIZE (was 100px, should be 160px) ────────────────────────────
html = re.sub(
    r'(\.hero-logo,\s*\.hero-logo-img\s*\{[^}]*?width:\s*)100px',
    r'\g<1>160px',
    html, flags=re.DOTALL
)
html = re.sub(
    r'(\.hero-logo,\s*\.hero-logo-img\s*\{[^}]*?height:\s*)100px',
    r'\g<1>160px',
    html, flags=re.DOTALL
)
print('HERO LOGO: size checked')

# ── 4. FEATURE VOTES — remove fake percentages ────────────────────────────────
# Replace the entire vote-items block with a clean "proposed" version
old_votes = re.search(r'<div class="vote-items">.*?</div>\s*</div>\s*</div>\s*</section>\s*<!-- ─── OWN', html, re.DOTALL)
if old_votes:
    print('VOTES: found block, replacing')
else:
    print('VOTES: block not found by primary pattern, trying fallback')

new_vote_block = '''<div class="vote-items">
          <div class="vote-item">
            <span class="vote-label">Agent screenshot feedback</span>
            <span class="vote-pct proposed-tag">Proposed</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Multi-agent support</span>
            <span class="vote-pct proposed-tag">Proposed</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Git diff viewer</span>
            <span class="vote-pct proposed-tag">Proposed</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Voice command mode</span>
            <span class="vote-pct proposed-tag">Proposed</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Mobile companion app</span>
            <span class="vote-pct proposed-tag">Proposed</span>
          </div>
          <p class="mono" style="font-size:12px; color:var(--muted); margin-top:16px;">
            Vote when you join — buyers set the roadmap.
          </p>
        </div>'''

html = re.sub(
    r'<div class="vote-items">.*?</div>\s*</div>\s*(?=</div>\s*</div>\s*</section>)',
    new_vote_block + '\n        ',
    html, flags=re.DOTALL, count=1
)
print('VOTES: replaced')

# ── 5. PRICING — rewrite $99 BYOA tier ───────────────────────────────────────
# Find and replace the pricing section cards
old_pricing_pattern = r'<!-- ─── PRICING.*?</section>\s*\n\s*<!-- ─── EMAIL'
pricing_match = re.search(old_pricing_pattern, html, re.DOTALL)
if pricing_match:
    print('PRICING: found section')
else:
    print('PRICING: section not found by comment pattern')

new_pricing_section = '''<!-- ─── PRICING ──────────────────────────────────────────────────── -->
<section id="pricing" class="section">
  <div class="container" style="text-align:center;">
    <span class="label">Pricing</span>
    <h2>Simple. Honest. Yours.</h2>
    <p class="sub" style="margin:0 auto 60px;">No subscriptions. No seats. No per-token billing hidden in a dashboard.<br/>Pay once — own the tool.</p>

    <div class="compare" style="max-width:860px; margin:0 auto;">
      <!-- FREE TIER -->
      <div class="compare-col">
        <div class="compare-header">
          <p class="mono" style="color:var(--muted); font-size:12px; letter-spacing:0.1em;">FREE</p>
          <p style="font-size:36px; font-weight:700; color:var(--white); margin:8px 0;">$0</p>
          <p style="color:var(--muted); font-size:14px;">Forever free</p>
        </div>
        <div class="compare-body">
          <div class="compare-item"><span class="check-blue">✓</span> <span>Full Bunker editor</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>AI chat &amp; inline edit</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Bring your own API key (BYOK)</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>All major cloud models</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Local Ollama support</span></div>
          <div class="compare-item muted-item"><span style="color:var(--muted);">✕</span> <span style="color:var(--muted);">Agent API (no external agent control)</span></div>
          <div class="compare-item muted-item"><span style="color:var(--muted);">✕</span> <span style="color:var(--muted);">Telegram command interface</span></div>
          <div style="margin-top:24px;">
            <a href="#email" class="btn btn-ghost" style="width:100%; justify-content:center;">Join waitlist</a>
          </div>
        </div>
      </div>

      <!-- $99 BYOA TIER -->
      <div class="compare-col" style="border-color:var(--blue); box-shadow:var(--glow);">
        <div class="compare-header" style="background:rgba(30,144,255,0.07);">
          <p class="mono" style="color:var(--blue-hi); font-size:12px; letter-spacing:0.1em;">BYOA — BRING YOUR OWN AGENT</p>
          <p style="font-size:36px; font-weight:700; color:var(--white); margin:8px 0;">$99</p>
          <p style="color:var(--blue-hi); font-size:14px; font-weight:600;">One time. Yours for life.</p>
        </div>
        <div class="compare-body">
          <p style="font-size:13px; color:var(--muted); margin-bottom:16px; line-height:1.6;">
            Unlocks the <strong style="color:var(--white);">Agent API</strong> — so any AI agent (Python, Node, anything) can drive your editor programmatically. Connect Bailey, build your own, or plug in whatever you want.
          </p>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Everything in Free</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Agent API — full read/write/run access</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Any agent: Python, Node, shell scripts</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Telegram command interface</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Screenshot + browser console reads</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>Persistent memory across sessions</span></div>
          <div class="compare-item"><span class="check-blue">✓</span> <span>All future updates — lifetime</span></div>
          <div style="margin-top:24px;">
            <a href="#email" class="btn btn-primary" style="width:100%; justify-content:center;">Get Bunker — $99</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ─── EMAIL'''

html = re.sub(old_pricing_pattern, new_pricing_section, html, flags=re.DOTALL, count=1)
print('PRICING: replaced')

# ── 6. FOUNDER BIO + CONTACT SECTIONS — inject before footer ─────────────────
founder_contact_html = '''
<!-- ─── FOUNDER ────────────────────────────────────────────────────── -->
<section id="founder" class="section">
  <div class="container">
    <div class="split" style="gap:60px; align-items:flex-start;">
      <div>
        <span class="label">The Builder</span>
        <h2>Javier Sandoval<br/><span style="color:var(--blue-hi); font-size:clamp(18px,2.5vw,28px); font-weight:500;">Founder</span></h2>
        <p class="sub" style="margin-top:20px; max-width:520px;">
          Self-taught engineer with 15+ years building on the web. I got tired of renting my tools, so I built the editor I wanted to own.
        </p>
        <p style="font-size:16px; color:var(--muted); line-height:1.8; max-width:520px; margin-top:16px;">
          Bunker is built solo, in the open, shaped by the people who use it. Not a big company — one builder who ships fast and answers to the community, not investors.
        </p>
        <div class="highlight-box" style="margin-top:32px;">
          <span>⚡</span>
          <span>If something's broken, I fix it. If you need a feature, you vote for it.<br/>That's the whole company.</span>
        </div>
      </div>
      <div style="padding-top:8px;">
        <div class="code-block" style="min-width:280px;">
          <div><span class="cmt"># 15+ years. Still shipping solo.</span></div>
          <div>&nbsp;</div>
          <div><span class="cmd">experience</span> <span class="out">= [</span></div>
          <div>&nbsp; <span class="out">"self-taught",</span></div>
          <div>&nbsp; <span class="out">"full-stack",</span></div>
          <div>&nbsp; <span class="out">"15+ years on the web",</span></div>
          <div>&nbsp; <span class="out">"ships fast",</span></div>
          <div>&nbsp; <span class="out">"answers to users not VCs",</span></div>
          <div><span class="out">]</span></div>
          <div>&nbsp;</div>
          <div><span class="cmd">company_size</span> <span class="out">= 1</span></div>
          <div><span class="cmd">investors</span> <span class="out">= []</span></div>
          <div><span class="cmd">telemetry</span> <span class="out">= False</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ─── CONTACT ───────────────────────────────────────────────────────── -->
<section id="contact" class="section">
  <div class="container" style="text-align:center;">
    <span class="label">Get in touch</span>
    <h2>Say hello.</h2>
    <p class="sub" style="margin:0 auto 40px;">Questions, feedback, partnership ideas — I read every message.</p>
    <a href="mailto:hello@bunker.dev" class="btn btn-outline" style="font-size:16px; padding:14px 32px;">
      ✉ hello@bunker.dev
    </a>
    <div style="margin-top:40px; display:flex; justify-content:center; gap:24px; flex-wrap:wrap;">
      <a href="#" class="btn btn-ghost">𝕏 Twitter / X</a>
      <a href="#" class="btn btn-ghost">💬 Discord</a>
      <a href="#" class="btn btn-ghost">▶ YouTube</a>
      <a href="#" class="btn btn-ghost">🐙 GitHub</a>
    </div>
  </div>
</section>

'''

# Inject before the footer
html = html.replace('\n<!-- ─── FOOTER', founder_contact_html + '\n<!-- ─── FOOTER', 1)
print('FOUNDER + CONTACT: injected')

# ── 7. ADD proposed-tag CSS (for vote items) + contact/founder CSS ─────────────
extra_css = '''
  /* ─── PROPOSED TAGS ─────────────────────────────────────────────── */
  .proposed-tag {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--blue);
    border: 1px solid var(--blue-dim);
    background: rgba(30,144,255,0.08);
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.05em;
    white-space: nowrap;
  }

  .vote-item {
    justify-content: space-between;
  }

  /* ─── COMPARE HEADER / BODY ─────────────────────────────────────── */
  .compare-header {
    padding: 32px 28px 24px;
    border-bottom: 1px solid var(--border);
  }

  .compare-body {
    padding: 28px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  /* ─── FOUNDER / CONTACT SECTION ─────────────────────────────────── */
  #founder .highlight-box {
    display: inline-flex;
    align-items: flex-start;
    gap: 10px;
    text-align: left;
    line-height: 1.6;
  }
'''

# Inject before closing </style>
html = html.replace('</style>', extra_css + '\n</style>', 1)
print('CSS: proposed-tag + compare layout + founder/contact injected')

# ── 8. NAV — add Contact link ─────────────────────────────────────────────────
html = html.replace(
    '<a href="#community">Community</a>',
    '<a href="#community">Community</a>\n          <a href="#contact">Contact</a>'
)
print('NAV: Contact link added')

# ── VERIFY ───────────────────────────────────────────────────────────────────
checks = {
    'localhost:3131 remaining': html.count('localhost:3131'),
    '©2025 remaining': len(re.findall(r'©\s*2025', html)),
    '©2026 present': html.count('© 2026'),
    'vote-pct % remaining': len(re.findall(r'vote-pct">\d+%', html)),
    'proposed-tag present': html.count('proposed-tag'),
    'BYOA section present': html.count('BRING YOUR OWN AGENT'),
    'Includes Bailey present': html.count('Includes Bailey'),
    'Agent API present': html.count('Agent API'),
    'founder section present': html.count('id="founder"'),
    'contact section present': html.count('id="contact"'),
    'hello@bunker.dev present': html.count('hello@bunker.dev'),
    'Javier Sandoval present': html.count('Javier Sandoval'),
}

print('\n=== VERIFICATION ===')
all_ok = True
for k, v in checks.items():
    status = '✓' if v == 0 and 'remaining' in k else ('✓' if v > 0 and 'remaining' not in k else '✗')
    if 'remaining' in k and v > 0:
        all_ok = False
    if 'remaining' not in k and v == 0:
        all_ok = False
    print(f'  {status} {k}: {v}')

print(f'\nALL_OK: {all_ok}')

with open('C:/BunkerSite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nFile written: {len(html)} chars')
