const fs = require('fs');
let h = fs.readFileSync('C:/BunkerSite/index.html', 'utf8');

// FIX A: section id="own" -> id="own-it" (so nav #own-it link resolves)
h = h.replace('id="own" class="section"', 'id="own-it" class="section"');
console.log('#own-it now present:', h.includes('id="own-it"'));

// FIX B: email section has duplicate id="email" id="capture" — collapse to just id="email"
h = h.replace('id="email" id="capture"', 'id="email"');
console.log('duplicate email id fixed:', !h.includes('id="email" id="capture"'));

// VERIFY no logo.png refs remain
console.log('logo.png refs remaining:', (h.match(/logo\.png/g)||[]).length);

// VERIFY @import is first in style
const importPos = h.indexOf('@import');
const firstRule = h.indexOf('*, *::before');
console.log('@import before first rule:', importPos < firstRule);

// Final check all section ids
const ids = ['hero','byoa','models','gamedev','own-it','community','pricing','email'];
ids.forEach(id => console.log('#' + id + ':', h.includes('id="' + id + '"') ? 'OK' : 'MISSING'));

fs.writeFileSync('C:/BunkerSite/index.html', h, 'utf8');
console.log('Written bytes:', h.length);
