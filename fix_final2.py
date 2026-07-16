import sys, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('C:/BunkerSite/index.html', encoding='utf-8').read()
original = content

# ─── 1. REPLACE vote-items block ────────────────────────────────────────────
# Strip the entire vote-items div and replace with clean "Proposed" cards
OLD_VOTES = re.compile(
    r'<div class="vote-items">.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

NEW_VOTES = '''\
<div class="vote-items">
          <div class="vote-item">
            <span class="vote-label">Agent screenshot feedback</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Multi-agent support</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Git diff viewer</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Voice command mode</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Built-in Ollama manager</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

m = OLD_VOTES.search(content)
if m:
    content = content[:m.start()] + NEW_VOTES + content[m.end():]
    print('VOTES: replaced OK')
else:
    print('VOTES: pattern not found - trying fallback')
    # Fallback: just replace the vote-items div directly
    old_vi_start = content.find('<div class="vote-items">')
    old_vi_end = content.find('</div>', old_vi_start)
    # walk closing divs to find end of vote-items
    depth = 0
    i = old_vi_start
    while i < len(content):
        if content[i:i+4] == '<div':
            depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                old_vi_end = i + 6
                break
        i += 1
    NEW_VI = '''\
<div class="vote-items">
          <div class="vote-item">
            <span class="vote-label">Agent screenshot feedback</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Multi-agent support</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Git diff viewer</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Voice command mode</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
          <div class="vote-item">
            <span class="vote-label">Built-in Ollama manager</span>
            <span class="proposed-tag">Proposed</span>
            <span class="vote-cta">Vote when you join</span>
          </div>
        </div>'''
    content = content[:old_vi_start] + NEW_VI + content[old_vi_end:]
    print('VOTES: fallback replace done')

# ─── 2. UPDATE vote-item CSS (remove bar styles, add proposed/cta styles) ────
OLD_VOTE_CSS = re.compile(
    r'\.vote-item \{.*?\.vote-pct \{.*?\}',
    re.DOTALL
)
NEW_VOTE_CSS = '''\
.vote-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 20px;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    background: var(--bg2);
    transition: border-color 0.2s;
  }
  .vote-item:hover { border-color: var(--blue); }

  .vote-label {
    font-size: 14px;
    color: var(--white);
    flex: 1;
  }

  .proposed-tag {
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--blue-hi);
    border: 1px solid var(--blue-dim);
    background: rgba(30,144,255,0.08);
    padding: 2px 8px;
    border-radius: 3px;
    white-space: nowrap;
  }

  .vote-cta {
    font-size: 12px;
    color: var(--muted);
    white-space: nowrap;
  }'''

if OLD_VOTE_CSS.search(content):
    content = OLD_VOTE_CSS.sub(NEW_VOTE_CSS, content, count=1)
    print('VOTE CSS: replaced OK')
else:
    # Just inject before </style>
    content = content.replace('</style>', NEW_VOTE_CSS + '\n</style>', 1)
    print('VOTE CSS: injected before </style>')

# ─── 3. ADD CONTACT LINK TO NAV ──────────────────────────────────────────────
if '<a href="#contact">' not in content:
    content = content.replace(
        '<li><a href="#community">Community</a></li>',
        '<li><a href="#community">Community</a></li>\n      <li><a href="#contact">Contact</a></li>'
    )
    print('NAV: Contact link added')
else:
    print('NAV: Contact link already present')

# ─── 4. INJECT FOUNDER BIO + CONTACT SECTIONS before </footer> ───────────────
FOUNDER_CONTACT = '''
<!-- ─── FOUNDER ──────────────────────────────────────────────────────── -->
<section id="founder" class="section" style="border-bottom:1px solid var(--border);">
  <div class="container">
    <div style="max-width:700px; margin:0 auto; text-align:center;">
      <span class="label">The Builder</span>
      <h2>Javier Sandoval</h2>
      <p style="font-size:18px; color:var(--muted); line-height:1.8; margin-top:20px;">
        Self-taught engineer with 15+ years building on the web. I got tired of renting my tools,
        so I built the editor I wanted to own. Bunker is built solo, in the open, shaped by the
        people who use it. Not a big company — one builder who ships fast and answers to the
        community, not investors.
      </p>
    </div>
  </div>
</section>

<!-- ─── CONTACT ──────────────────────────────────────────────────────── -->
<section id="contact" class="section" style="border-bottom:none;">
  <div class="container">
    <div style="max-width:560px; margin:0 auto; text-align:center;">
      <span class="label">Contact</span>
      <h2>Get in touch</h2>
      <p class="sub" style="margin:16px auto 40px;">Questions, feedback, or just want to say hi — reach out directly.</p>
      <div style="display:flex; flex-direction:column; align-items:center; gap:20px;">
        <a href="mailto:hello@bunker.dev"
           style="font-family:var(--mono); font-size:18px; color:var(--blue-hi);
                  text-decoration:none; border-bottom:1px solid var(--blue-dim); padding-bottom:4px;">
          hello@bunker.dev
        </a>
        <div style="display:flex; gap:24px; margin-top:8px;">
          <a href="#" style="color:var(--muted); font-size:14px; text-decoration:none;
             transition:color 0.2s;" onmouseover="this.style.color='var(--blue-hi)'"
             onmouseout="this.style.color='var(--muted)'">Twitter / X</a>
          <a href="#" style="color:var(--muted); font-size:14px; text-decoration:none;
             transition:color 0.2s;" onmouseover="this.style.color='var(--blue-hi)'"
             onmouseout="this.style.color='var(--muted)'">GitHub</a>
          <a href="#" style="color:var(--muted); font-size:14px; text-decoration:none;
             transition:color 0.2s;" onmouseover="this.style.color='var(--blue-hi)'"
             onmouseout="this.style.color='var(--muted)'">Discord</a>
        </div>
      </div>
    </div>
  </div>
</section>

'''

if 'id="founder"' not in content:
    content = content.replace('<footer', FOUNDER_CONTACT + '<footer')
    print('FOUNDER + CONTACT: injected')
else:
    print('FOUNDER + CONTACT: already present')

# ─── 5. VERIFY no fake vote percentages remain ───────────────────────────────
remaining = re.findall(r'vote-pct|vote-bar-wrap|style="width:\d+%"', content)
print(f'REMAINING FAKE VOTE ARTIFACTS: {remaining}')

# ─── WRITE ───────────────────────────────────────────────────────────────────
open('C:/BunkerSite/index.html', 'w', encoding='utf-8').write(content)
print(f'FILE WRITTEN: {len(content)} chars (was {len(original)})')

# ─── FINAL CHECKS ────────────────────────────────────────────────────────────
checks = {
    'vote-pct spans gone':     'vote-pct' not in content,
    'vote-bar gone':           'vote-bar-wrap' not in content,
    'proposed-tag present':    'proposed-tag' in content,
    'Vote when you join':      'Vote when you join' in content,
    'founder section':         'id="founder"' in content,
    'Javier Sandoval':         'Javier Sandoval' in content,
    'contact section':         'id="contact"' in content,
    'hello@bunker.dev':        'hello@bunker.dev' in content,
    'nav Contact link':        'href="#contact"' in content,
    'Includes Bailey gone':    'includes Bailey' not in content.lower(),
    'Agent API present':       'Agent API' in content,
    'copyright 2026':          '2026' in content,
    'no localhost:3131':       'localhost:3131' not in content,
}

print('\n=== FINAL VERIFY ===')
all_ok = True
for k, v in checks.items():
    status = 'OK' if v else 'FAIL'
    if not v:
        all_ok = False
    print(f'  [{status}] {k}')

print(f'\nALL_OK: {all_ok}')
