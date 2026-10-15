// Kiểm giao diện điện thoại của bản gửi khách: cuộn hết trang, mọi khối phải hiện, không tràn ngang, không dòng một chữ.
// Dùng: node check_mobile.js <deck.html> [thư_mục_ảnh]   (thử ở 390px và 360px)
const { chromium } = require('./_pw');
const orphanCheck = require('./orphans');
(async () => {
  const [file, shotDir] = process.argv.slice(2); let bad = 0;
  const browser = await chromium.launch();
  for (const width of [390, 360]) {
    const ctx = await browser.newContext({ viewport: { width, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
    const page = await ctx.newPage(); const errs = [];
    page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); page.on('pageerror', e => errs.push(String(e)));
    await page.goto('file://' + require('path').resolve(file)); await page.waitForTimeout(600);
    const mobile = await page.evaluate(() => document.documentElement.classList.contains('m') || !!window.__mobile);
    const H = await page.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < H; y += 320) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(90); }
    await page.waitForTimeout(2500);
    const st = await page.evaluate(() => window.__mobile ? window.__mobile.state() : null);
    const over = await page.evaluate(() => { const vw = innerWidth; return [...document.querySelectorAll('#stage *')].filter(e => { if (e.classList.contains('ghost')) return false; const b = e.getBoundingClientRect(); return b.width && (b.right > vw + 0.5 || b.left < -0.5); }).slice(0, 5).map(e => e.className); });
    const orph = await page.evaluate(`(${orphanCheck})('#stage *, #mtop *')`);
    const scrollW = await page.evaluate(() => document.documentElement.scrollWidth);
    console.log(`ĐIỆN THOẠI ${width}px: giao diện mobile ${mobile ? 'bật' : 'KHÔNG bật'} · khối hiện ${st ? st.shown + '/' + st.steps : '?'} · lỗi console: ${errs.length ? errs.join(' | ') : 'không'}`);
    const issues = [];
    if (!mobile) issues.push('không chuyển sang giao diện đọc dọc');
    if (st && st.pending) issues.push(`${st.pending} khối chưa hiện sau khi cuộn hết`);
    if (scrollW > width) issues.push(`trang cuộn ngang (${scrollW}px > ${width}px)`);
    over.forEach(o => issues.push('tràn lề: ' + o)); orph.forEach(o => issues.push('dòng một chữ — ' + o));
    console.log(issues.length ? issues.map(x => '  ✕ ' + x).join('\n') : '  ✓ ổn');
    bad += issues.length + errs.length;
    if (shotDir && width === 390) { const n = await page.evaluate(() => document.querySelectorAll('#stage > .slide').length);
      for (let i = 1; i <= n; i++) { const el = await page.$('#s' + i); if (!el) continue; await el.scrollIntoViewIfNeeded(); await page.waitForTimeout(120); await el.screenshot({ path: `${shotDir}/m${String(i).padStart(2, '0')}.png` }); } }
    await ctx.close();
  }
  await browser.close(); process.exit(bad ? 1 : 0);
})();
