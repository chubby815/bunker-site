const fs = require('fs');
const h = fs.readFileSync('C:/BunkerSite/index.html', 'utf8');

// @import placement
const importPos = h.indexOf('@import');
const firstRulePos = h.indexOf('*, *::before');
console.log('@import pos:', importPos, '| first CSS rule pos:', firstRulePos);
console.log('@import AFTER rules (bug):', importPos > firstRulePos);

// Section IDs
const ids = ['hero','byoa','models','gamedev','own-it','community','pricing','email'];
ids.forEach(id => {
  const found = h.includes('id="' + id + '"') || h.includes("id='" + id + "'");
  console.log('section id #' + id + ':', found ? 'YES' : 'MISSING');
});

// Key elements
console.log('email <form>:', h.includes('<form'));
console.log('email <input type="email">:', h.includes('type="email"'));
console.log('<footer>:', h.includes('<footer'));
console.log('onerror on logo imgs:', (h.match(/onerror/g)||[]).length);
console.log('logo.png img tags:', (h.match(/logo\.png/g)||[]).length);

// Pricing
console.log('$99 refs:', (h.match(/\$99/g)||[]).length);
console.log('one-time / lifetime refs:', (h.match(/one.time|lifetime/gi)||[]).length);

// Buttons/links
console.log('btn-primary count:', (h.match(/btn-primary/g)||[]).length);
console.log('btn-outline count:', (h.match(/btn-outline/g)||[]).length);
console.log('nav links:', (h.match(/<a href="#/g)||[]).length);

// Colors
console.log('--blue (#1e90ff) defined:', h.includes('#1e90ff'));
console.log('--blue-hi (#00bfff) defined:', h.includes('#00bfff'));
console.log('--bg (#0a0a0f) defined:', h.includes('#0a0a0f'));

// Check if logo.png file actually exists
try { fs.statSync('C:/BunkerSite/logo.png'); console.log('logo.png on disk: YES'); }
catch(e) { console.log('logo.png on disk: MISSING <-- THIS IS THE BUG'); }

// Check what image files ARE there
const files = fs.readdirSync('C:/BunkerSite');
const imgs = files.filter(f => /\.(png|jpg|jpeg|svg|webp|gif)$/i.test(f));
console.log('Image files in folder:', imgs.length ? imgs.join(', ') : 'NONE');
console.log('All files:', files.filter(f=>!f.includes('node_modules')).join(', '));
