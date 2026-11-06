// Run with Playwright browser_run_code_unsafe({ filename: 'tests/browser_checks.js' }).
async (page) => {
  const errors = [], bad = [];
  page.on('pageerror', error => errors.push(String(error)));
  page.on('response', response => { if (response.status() >= 400) bad.push(response.url()); });
  const slugs = ['inthanon-signature', 'dalmation', 'hamiqua', 'rock-melon', 'sweet-hamy', 'sweet-lavender'];
  let checked = 0;
  for (const width of [360, 390, 768, 1024, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    for (const path of ['/', ...slugs.map(slug => `/produk/${slug}.html`)]) {
      await page.goto(`http://127.0.0.1:8000${path}`);
      if (!await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)) throw Error(`Overflow: ${width} ${path}`);
      const smallTargets = await page.locator('a,button,summary').evaluateAll(elements => elements.filter(el => {
        const r = el.getBoundingClientRect();
        return el.getClientRects().length && !el.classList.contains('skip-link') && (r.width < 43.9 || r.height < 43.9);
      }).map(el => el.textContent.trim()));
      if (smallTargets.length) throw Error(`Target below 44px: ${width} ${path} ${smallTargets}`);
      checked++;
    }
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('http://127.0.0.1:8000/produk/dalmation.html');
  const toggle = page.locator('[data-menu-toggle]');
  await toggle.focus(); await page.keyboard.press('Enter');
  await page.waitForFunction(() => document.querySelector('[data-menu-toggle]').getAttribute('aria-expanded') === 'true');
  await page.keyboard.press('Tab'); await page.keyboard.press('Escape');
  if (await toggle.getAttribute('aria-expanded') !== 'false' || !await toggle.evaluate(el => el === document.activeElement)) throw Error('Escape focus');
  await page.keyboard.press('Space'); await page.locator('#navigasi-utama a').first().focus();
  await page.setViewportSize({ width: 1024, height: 900 });
  await page.waitForFunction(() => document.querySelector('[data-menu-toggle]').getAttribute('aria-expanded') === 'false');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForFunction(() => document.querySelector('[data-menu-toggle]').getAttribute('aria-expanded') === 'true');
  if (!await page.locator('#navigasi-utama a').first().evaluate(el => el === document.activeElement)) throw Error('Breakpoint lost focus');
  await page.keyboard.press('Escape'); await toggle.focus();
  await page.setViewportSize({ width: 1024, height: 900 });
  await page.waitForFunction(() => document.activeElement === document.querySelector('#navigasi-utama a'));
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForFunction(() => document.querySelector('[data-menu-toggle]').getAttribute('aria-expanded') === 'true');
  await page.keyboard.press('Escape'); await toggle.click();
  await page.locator('#navigasi-utama a[href="../index.html#produk"]').click();
  await page.waitForURL('**/index.html#produk');
  await page.goto('http://127.0.0.1:8000/');
  await toggle.click();
  await page.locator('#navigasi-utama a').last().focus();
  await page.keyboard.press('Tab'); await page.keyboard.press('Escape');
  if (await toggle.getAttribute('aria-expanded') !== 'false') throw Error('Escape outside header');
  await toggle.click(); await page.locator('.wordmark').click();
  if (await toggle.getAttribute('aria-expanded') !== 'false') throw Error('Wordmark leaves menu open');
  await page.goto('http://127.0.0.1:8000/produk/dalmation.html');
  const thumb = page.locator('[data-gallery-thumb]').nth(1);
  await thumb.focus(); await page.keyboard.press('Space');
  if (await thumb.getAttribute('aria-pressed') !== 'true' || !await page.locator('#foto-detail').isVisible() || await page.locator('#foto-utama').isVisible()) throw Error('Gallery selection');
  await page.reload();
  if (!await page.locator('#foto-utama').isVisible()) throw Error('Gallery reload');
  await page.emulateMedia({ reducedMotion: 'reduce' });
  if (await page.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior) !== 'auto') throw Error('Reduced motion');
  await page.emulateMedia({ reducedMotion: 'no-preference' });
  const context = await page.context().browser().newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  const staticPage = await context.newPage();
  for (const path of ['/', ...slugs.map(slug => `/produk/${slug}.html`)]) {
    await staticPage.goto(`http://127.0.0.1:8000${path}`);
    if (!await staticPage.locator('#navigasi-utama').isVisible() || await staticPage.locator('[data-menu-toggle]').isVisible()) throw Error(`No-JS navigation ${path}`);
    for (const frame of await staticPage.locator('[data-gallery-image]').all()) if (!await frame.isVisible()) throw Error(`No-JS photo ${path}`);
  }
  await context.close();
  if (errors.length || bad.length) throw Error(JSON.stringify({ errors, bad }));
  return { responsivePages: checked, menu: 'PASS keyboard/Escape/link/resize focus', gallery: 'PASS', reducedMotion: 'PASS', noJavaScriptPages: 7, errors, bad };
}
