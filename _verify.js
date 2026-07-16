const fs = require('fs');
const s = fs.readFileSync('C:/BunkerSite/index.html', 'utf8');
const checks = [
  ['bytes > 20000', s.length > 20000],
  ['NAV logo.png', s.includes('nav-logo') && s.includes('logo.png')],
  ['hero headline — The code editor', s.includes('The code editor')],
  ['hero sub — No subscription', s.includes('No subscription')],
  ['BYOA section', s.includes('id="byoa"')],
  ['models section', s.includes('id="models"')],
  ['gamedev section', s.includes('id="gamedev"')],
  ['own section', s.includes('id="own"')],
  ['community section', s.includes('id="community"')],
  ['pricing section', s.includes('id="pricing"')],
  ['compare-col featured', s.includes('compare-col featured')],
  ['email capture section', s.includes('id="capture"')],
  ['footer-inner', s.includes('footer-inner')],
  ['Get Bunker $99 btn', s.includes('Get Bunker')],
  ['model-pill', s.includes('model-pill')],
  ['vote-item', s.includes('vote-item')],
  ['code-block', s.includes('code-block')],
  ['editor-window', s.includes('editor-window')],
  ['hero-logo', s.includes('hero-logo')],
  ['color #1e90ff', s.includes('#1e90ff')],
  ['bg #0a0a0f', s.includes('#0a0a0f')],
  ['JetBrains Mono', s.includes('JetBrains Mono')],
  ['handleSubmit', s.includes('handleSubmit')],
  ['IntersectionObserver', s.includes('IntersectionObserver')],
  ['parallax perspective', s.includes('perspective(900px)')],
  ['no purple gradient', !s.includes('purple-gradient')],
  ['label class', s.includes('class="label"')],
  ['stats-row', s.includes('stats-row')],
  ['contrast-box good', s.includes('contrast-box good')],
  ['step-num circles', s.includes('step-num')],
];
let pass = 0, fail = 0;
checks.forEach(([name, ok]) => {
  process.stdout.write((ok ? 'PASS' : 'FAIL') + ' ' + name + '\n');
  ok ? pass++ : fail++;
});
process.stdout.write('\n' + pass + '/' + checks.length + ' passed, ' + fail + ' failed\n');
process.stdout.write('File size: ' + s.length + ' bytes\n');
