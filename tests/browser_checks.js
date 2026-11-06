// Run with Playwright browser_run_code_unsafe({ filename: 'tests/browser_checks.js' }).
async (page) => {
  const errors = [], bad = [];
  page.on('pageerror', error => errors.push(String(error)));
  page.on('response', response => { if (response.status() >= 400) bad.push(response.url()); });
  const slugs = ['inthanon-signature', 'dalmation', 'hamiqua', 'rock-melon', 'sweet-hamy', 'sweet-lavender'];
  const paths = ['/', '/katalog.html', '/tentang.html', '/kontak.html', ...slugs.map(slug => `/produk/${slug}.html`)];
  const measureChrome = () => ['.site-header', '.nav-row', '.wordmark', '.main-nav', '.site-footer', '.footer-top', '.footer-brand', '.footer-links', '.footer-bottom'].map(selector => {
    const element = document.querySelector(selector), rect = element.getBoundingClientRect(), style = getComputedStyle(element);
    return { selector, x: rect.x, width: rect.width, height: rect.height,
      ...(element.closest('.site-header') ? { top: rect.top } : {}),
      ...Object.fromEntries(['display', 'padding', 'gap', 'gridTemplateColumns', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'color', 'backgroundColor', 'borderRadius'].map(key => [key, style[key]])) };
  });
  const assertChrome = (actual, expected, label) => {
    for (let i = 0; i < expected.length; i++) for (const [key, value] of Object.entries(expected[i])) {
      if (typeof value === 'number' ? Math.abs(actual[i][key] - value) > 1 : actual[i][key] !== value)
        throw Error(`Header/footer mismatch: ${label} ${expected[i].selector} ${key}: ${actual[i][key]} != ${value}`);
    }
  };
  let checked = 0;
  for (const width of [360, 390, 768, 1024, 1440]) {
    const chrome = {};
    await page.setViewportSize({ width, height: 900 });
    for (const path of paths) {
      await page.goto(`http://127.0.0.1:8000${path}`);
      await page.evaluate(() => document.fonts.ready);
      if (!path.startsWith('/produk/')) chrome[path] = await page.evaluate(measureChrome);
      if (!await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)) throw Error(`Overflow: ${width} ${path}`);
      if (await page.locator('.page-intro').count() && !await page.evaluate(() => document.querySelector('.breadcrumb').getBoundingClientRect().top >= document.querySelector('.site-header').getBoundingClientRect().bottom)) throw Error(`Header covers intro: ${width} ${path}`);
      const smallTargets = await page.locator('a,button,summary').evaluateAll(elements => elements.filter(el => {
        const r = el.getBoundingClientRect();
        return el.getClientRects().length && !el.classList.contains('skip-link') && (r.width < 43.9 || r.height < 43.9);
      }).map(el => el.textContent.trim()));
      if (smallTargets.length) throw Error(`Target below 44px: ${width} ${path} ${smallTargets}`);
      checked++;
    }
    for (const [path, measurements] of Object.entries(chrome)) assertChrome(measurements, chrome['/tentang.html'], `${width} ${path}`);
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
  await page.locator('#navigasi-utama a[href="../katalog.html"]').click();
  await page.waitForURL('**/katalog.html');
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
  staticPage.on('response', response => { if (response.status() >= 400) bad.push(response.url()); });
  staticPage.on('pageerror', error => errors.push(String(error)));
  let decodedImages = 0;
  for (const path of paths) {
    await staticPage.goto(`http://127.0.0.1:8000${path}`);
    if (!await staticPage.locator('#navigasi-utama').isVisible() || await staticPage.locator('[data-menu-toggle]').isVisible()) throw Error(`No-JS navigation ${path}`);
    for (const frame of await staticPage.locator('[data-gallery-image]').all()) if (!await frame.isVisible()) throw Error(`No-JS photo ${path}`);
    await staticPage.evaluate(() => { for (const image of document.images) image.loading = 'eager'; });
    decodedImages += await staticPage.locator('img').evaluateAll(async images => { await Promise.all(images.map(image => image.decode())); return images.length; });
    if (await staticPage.locator('.page-intro').count()) {
      for (const width of [390, 1440]) {
        await staticPage.setViewportSize({ width, height: 900 });
        if (!await staticPage.evaluate(() => document.querySelector('.breadcrumb').getBoundingClientRect().top >= document.querySelector('.site-header').getBoundingClientRect().bottom)) throw Error(`No-JS header covers intro: ${width} ${path}`);
      }
      await staticPage.setViewportSize({ width: 390, height: 844 });
    }
  }
  await context.close();
  await page.setViewportSize({ width: 1440, height: 1000 });
  for (const destination of ['katalog.html', 'tentang.html', 'kontak.html']) {
    await page.goto('http://127.0.0.1:8000/');
    await page.locator(`#navigasi-utama a[href="${destination}"]`).click();
    await page.waitForURL(`**/${destination}`);
    await page.reload();
    if (await page.locator('#navigasi-utama [aria-current="page"]').getAttribute('href') !== destination) throw Error(`Current page ${destination}`);
    const introClear = await page.evaluate(() => document.querySelector('h1').getBoundingClientRect().top > document.querySelector('.site-header').getBoundingClientRect().bottom);
    if (!introClear) throw Error(`Header covers intro ${destination}`);
    if (destination === 'kontak.html') {
      const currentLink = page.locator('#navigasi-utama [aria-current="page"]');
      const restingOutline = await currentLink.evaluate(el => getComputedStyle(el).outline);
      await page.keyboard.press('Tab'); await currentLink.focus();
      if (await currentLink.evaluate(el => getComputedStyle(el).outline) === restingOutline) throw Error('Current contact link has no distinct keyboard focus');
      await currentLink.evaluate(el => el.blur());
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await toggle.click();
    await page.locator(`#navigasi-utama a[href="${destination}"]`).click();
    if (await toggle.getAttribute('aria-expanded') !== 'false') throw Error(`Same-page navigation ${destination}`);
    await page.setViewportSize({ width: 1440, height: 1000 });
  }
  for (const slug of slugs) {
    await page.goto('http://127.0.0.1:8000/katalog.html');
    await page.locator(`main a[href="produk/${slug}.html"]`).click();
    await page.waitForURL(`**/produk/${slug}.html`);
    await page.reload();
    await page.locator('.breadcrumb a[href="../katalog.html"]').click();
    await page.waitForURL('**/katalog.html');
    await page.goto(`http://127.0.0.1:8000/produk/${slug}.html`);
    await page.getByRole('link', { name: 'Kembali ke katalog' }).click();
    await page.waitForURL('**/katalog.html');
  }
  for (const destination of ['tentang.html', 'kontak.html']) {
    await page.goto('http://127.0.0.1:8000/produk/dalmation.html');
    await page.locator(`#navigasi-utama a[href="../${destination}"]`).click();
    await page.waitForURL(`**/${destination}`);
  }
  for (const anchor of ['layanan', 'kemitraan']) {
    await page.goto('http://127.0.0.1:8000/tentang.html');
    await page.locator(`#navigasi-utama a[href="index.html#${anchor}"]`).click();
    await page.waitForURL(`**/index.html#${anchor}`);
    if (!await page.locator(`#${anchor}`).isVisible()) throw Error(`Home anchor ${anchor}`);
  }
  if (errors.length || bad.length) throw Error(JSON.stringify({ errors, bad }));
  return { responsivePages: checked, headerFooterParity: 'PASS four root pages at five widths', menu: 'PASS keyboard/Escape/link/resize focus', gallery: 'PASS', reducedMotion: 'PASS', noJavaScriptPages: paths.length, decodedImages, navigation: 'PASS home/new pages/six details/breadcrumb/return/home anchors', errors, bad };
}
