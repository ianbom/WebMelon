// Run through Playwright browser_run_code_unsafe, then python -I tests/check_contrast.py.
async (page) => {
  await page.route('**/*', route => route.continue());
  const samples = [];
  await page.emulateMedia({ reducedMotion: 'reduce' });
  for (const width of [390, 1440]) {
    await page.setViewportSize({ width, height: 1000 });
    await page.goto('http://127.0.0.1:8000/');
    await page.evaluate(() => { for (const img of document.images) img.loading = 'eager'; });
    await page.locator('.hero-image,.product-card>img').evaluateAll(images => Promise.all(images.map(img => img.decode())));
    for (const [index, block] of (await page.locator('.hero,.product-card').all()).entries()) {
      await block.scrollIntoViewIfNeeded();
      const texts = block.locator(index === 0 ? 'h1,p' : 'h3,p,.card-end');
      const rects = await texts.evaluateAll(elements => elements.map(el => {
        const r = el.getBoundingClientRect(), b = el.closest('.hero,.product-card').getBoundingClientRect();
        const style = getComputedStyle(el), color = style.color.match(/[\d.]+/g).map(Number);
        return { box: [Math.ceil(r.left-b.left), Math.ceil(r.top-b.top), Math.floor(r.right-b.left), Math.floor(r.bottom-b.top)], color, minimum: parseFloat(style.fontSize) >= 24 ? 3 : 4.5 };
      }));
      await block.locator(index === 0 ? '.hero-content' : '.card-body').evaluate(el => el.style.visibility = 'hidden');
      const file = `.work/contrast-${width}-${index}.png`;
      await block.screenshot({ path: file, animations: 'disabled', timeout: 10000 });
      samples.push({ file, rects });
    }
  }
  const download = page.waitForEvent('download');
  await page.evaluate(samples => {
    const link = document.createElement('a');
    link.href = URL.createObjectURL(new Blob([JSON.stringify(samples)], { type: 'application/json' }));
    link.download = 'contrast.json'; link.click(); URL.revokeObjectURL(link.href);
  }, samples);
  await (await download).saveAs('.work/contrast.json');
  return { captures: samples.length };
}
