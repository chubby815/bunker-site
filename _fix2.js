const fs = require('fs');
let h = fs.readFileSync('C:/BunkerSite/index.html', 'utf8');

// Find all section ids and their nearby headings to locate the "own it" section
const sectionMatches = [...h.matchAll(/<section([^>]*)>/gi)];
sectionMatches.forEach(m => {
  const pos = m.index;
  const snippet = h.slice(pos, pos + 300).replace(/\n/g,' ').replace(/\s+/g,' ');
  console.log('SECTION attrs:', m[1].trim() || '(no attrs)', '| content preview:', snippet.slice(0,120));
});
