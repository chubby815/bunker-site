const fs = require('fs');
let h = fs.readFileSync('C:/BunkerSite/index.html', 'utf8');

// ── FIX 1: Move @import to the very top of the <style> block ─────────────
// Remove the misplaced @import line wherever it is
const importLine = `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');`;
h = h.replace(/\s*@import url\([^)]+\);\s*/g, '\n');
// Insert it as the very first thing inside <style>
h = h.replace('<style>', '<style>\n  ' + importLine);
console.log('@import moved to top:', h.indexOf('@import') < h.indexOf('*, *::before'));

// ── FIX 2: Replace logo.png <img> tags with inline SVG tree logo ──────────
// The SVG: a stylized "B" bunker tree mark in electric blue on transparent bg
const svgLogo = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32" aria-label="Bunker logo">
  <defs>
    <filter id="glow"><feGaussianBlur stdDeviation="1.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <!-- trunk -->
  <rect x="28" y="44" width="8" height="14" rx="2" fill="#1e90ff" filter="url(#glow)"/>
  <!-- base branches -->
  <polygon points="32,10 8,48 56,48" fill="none" stroke="#00bfff" stroke-width="2.5" stroke-linejoin="round" filter="url(#glow)"/>
  <!-- mid layer -->
  <polygon points="32,20 12,46 52,46" fill="#0a3a6e" stroke="#1e90ff" stroke-width="1.5" stroke-linejoin="round"/>
  <!-- top pip -->
  <circle cx="32" cy="10" r="3.5" fill="#00bfff" filter="url(#glow)"/>
</svg>`;

// Replace all <img src="logo.png" ...> in nav and hero
// Nav logo img
h = h.replace(
  /<img src="logo\.png" alt="Bunker logo"[^>]*\/>/g,
  svgLogo
);
// Hero logo img (different class)
h = h.replace(
  /<img src="logo\.png" alt="Bunker"[^>]*\/>/g,
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="120" height="120" aria-label="Bunker" class="hero-logo">
  <defs>
    <filter id="glow2"><feGaussianBlur stdDeviation="2.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect x="28" y="44" width="8" height="14" rx="2" fill="#1e90ff" filter="url(#glow2)"/>
  <polygon points="32,10 8,48 56,48" fill="none" stroke="#00bfff" stroke-width="2.5" stroke-linejoin="round" filter="url(#glow2)"/>
  <polygon points="32,20 12,46 52,46" fill="#0a3a6e" stroke="#1e90ff" stroke-width="1.5" stroke-linejoin="round"/>
  <circle cx="32" cy="10" r="3.5" fill="#00bfff" filter="url(#glow2)"/>
</svg>`
);
// Any remaining logo.png refs
h = h.replace(/<img[^>]*logo\.png[^>]*>/g, svgLogo);
console.log('logo.png img tags remaining:', (h.match(/logo\.png/g)||[]).length);

// ── FIX 3: Add id="own-it" to the "Own It" section ───────────────────────
// Find the section that talks about own/ownership — look for "Own It" heading
// The section likely has a different id or no id — patch it
h = h.replace(
  /(<section)([^>]*)(>[\s\S]{0,200}?(?:Own It|own it|you own|OWN IT))/,
  (match, tag, attrs, rest) => {
    if (attrs.includes('own-it')) return match; // already has it
    // inject id
    return tag + ' id="own-it"' + attrs + rest;
  }
);
console.log('#own-it id present:', h.includes('id="own-it"'));

// ── FIX 4: Add id="email" to the email capture section ───────────────────
// Find the section containing the email input
h = h.replace(
  /(<section)([^>]*)(>[\s\S]{0,400}?type="email")/,
  (match, tag, attrs, rest) => {
    if (attrs.includes('"email"')) return match;
    return tag + ' id="email"' + attrs + rest;
  }
);
console.log('#email id present:', h.includes('id="email"'));

fs.writeFileSync('C:/BunkerSite/index.html', h, 'utf8');
console.log('Written bytes:', h.length);
console.log('DONE');
