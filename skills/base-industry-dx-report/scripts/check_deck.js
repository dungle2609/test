// Kiểm bản máy tính: đi xuôi/lùi mọi bước, lỗi console, tràn khung, dòng nguồn bị đè, tiêu đề > 2 dòng, dòng một chữ, chế độ in.
// Dùng: node check_deck.js <deck.html> [thư_mục_ảnh] [file.pdf]
const { chromium } = require('./_pw');
const orphanCheck = require('./orphans');
(async () => {
  const [file, shotDir, pdf] = process.argv.slice(2);
  const browser = await chromium.launch(); const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
  const errs = []; page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); page.on('pageerror', e => errs.push(String(e)));
  await page.goto('file://' + require('path').resolve(file)); await page.waitForTimeout(500);
  let steps = 0, last = '';
  for (let g = 0; g < 600; g++) { const st = await page.evaluate(() => window.__deck.state()); const k = st.slide + '.' + st.step; if (k === last) break; last = k; steps++; await page.evaluate(() => window.__deck.next()); await page.waitForTimeout(40); }
  last = ''; for (let g = 0; g < 600; g++) { const st = await page.evaluate(() => window.__deck.state()); const k = st.slide + '.' + st.step; if (k === last) break; last = k; await page.evaluate(() => window.__deck.prev()); await page.waitForTimeout(20); }
  const n = await page.evaluate(() => document.querySelectorAll('#stage > .slide').length);
  const issues = [];
  for (let i = 0; i < n; i++) {
    await page.evaluate(i => window.__deck.go(i, 999, 'jump'), i); await page.waitForTimeout(700);
    const r = await page.evaluate(i => {
      const s = document.querySelectorAll('#stage > .slide')[i], sr = s.getBoundingClientRect(), sc = sr.width / 1600;
      const src = s.querySelector('.srcline'), srcTop = src ? (src.getBoundingClientRect().top - sr.top) / sc : 900;
      let maxB = 0, over = [];
      s.querySelectorAll('*').forEach(e => { if (e.closest('.notes,.srcline') || e.classList.contains('ghost')) return; const cs = getComputedStyle(e); if (cs.display === 'none') return;
        const b = e.getBoundingClientRect(); if (!b.width || !b.height) return; const bot = (b.bottom - sr.top) / sc, rt = (b.right - sr.left) / sc, lf = (b.left - sr.left) / sc;
        if (bot > maxB) maxB = bot; if (rt > 1560 || lf < 40) over.push(e.className); });
      const h = s.querySelector('h1,h2'); const lines = h ? Math.round(h.getBoundingClientRect().height / sc / parseFloat(getComputedStyle(h).lineHeight)) : 0;
      return { title: s.dataset.title, maxB: Math.round(maxB), srcTop: Math.round(srcTop), over, lines };
    }, i);
    if (r.maxB > r.srcTop - 8) issues.push(`slide ${i + 1} (${r.title}): nội dung chạm dòng nguồn (${r.maxB} ≥ ${r.srcTop})`);
    if (r.maxB > 870) issues.push(`slide ${i + 1} (${r.title}): tràn đáy (${r.maxB}px)`);
    if (r.over.length) issues.push(`slide ${i + 1} (${r.title}): tràn lề — ${r.over.slice(0, 3).join(', ')}`);
    if (r.lines > 2) issues.push(`slide ${i + 1} (${r.title}): tiêu đề ${r.lines} dòng`);
    (await page.evaluate(`(${orphanCheck})('#stage > .slide:nth-child(${i + 1}) *')`)).forEach(o => issues.push('dòng một chữ — ' + o));
    if (shotDir) await page.screenshot({ path: `${shotDir}/s${String(i + 1).padStart(2, '0')}.png` });
  }
  await page.keyboard.press('p'); await page.waitForTimeout(500);
  const ph = await page.evaluate(() => document.body.scrollHeight);
  if (ph !== n * 900) issues.push(`chế độ in cao ${ph}px, cần ${n * 900}px`);
  if (pdf) await page.pdf({ path: pdf, width: '1600px', height: '900px', printBackground: true });
  console.log(`BẢN MÁY TÍNH: ${n} slide · ${steps} bước · lỗi console: ${errs.length ? errs.join(' | ') : 'không'}`);
  console.log(issues.length ? issues.map(x => '  ✕ ' + x).join('\n') : '  ✓ không có vấn đề bố cục, chữ, chế độ in');
  await browser.close(); process.exit(errs.length || issues.length ? 1 : 0);
})();
