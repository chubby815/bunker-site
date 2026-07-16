const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const errors = [];
  const warnings = [];

  page.on('console', msg => {
    if (msg.type() === 'error')   errors.push(msg.text());
    if (msg.type() === 'warning') warnings.push(msg.text());
  });

  page.on('pageerror', err => errors.push('PAGE_ERROR: ' + err.message));

  const filePath = 'file:///' + path.resolve('C:/BunkerSite/index.html').replace(/\\/g, '/');
  await page.goto(filePath, { waitUntil: 'networkidle', timeout: 15000 });

  // wait a moment for any deferred scripts
  await page.waitForTimeout(2000);

  await browser.close();

  process.stdout.write('ERRORS: ' + errors.length + '\n');
  process.stdout.write('WARNINGS: ' + warnings.length + '\n');
  if (errors.length > 0) {
    errors.forEach(e => process.stdout.write('ERR: ' + e + '\n'));
  }
  if (warnings.length > 0) {
    warnings.forEach(w => process.stdout.write('WARN: ' + w + '\n'));
  }
  if (errors.length === 0) {
    process.stdout.write('BROWSER_CONSOLE_CLEAN\n');
  }
})();
