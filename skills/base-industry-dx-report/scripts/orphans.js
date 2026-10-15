// Chạy trong trang: liệt kê dòng chữ chỉ có một chữ (bỏ qua dấu câu), sau khi tạm gỡ góc nghiêng của mảnh giao diện.
module.exports = function orphanCheck(rootSel) {
  const st = document.createElement('style'); st.textContent = '.mess>*{transform:none!important;rotate:none!important}'; document.head.appendChild(st);
  const isBlock = el => { const d = getComputedStyle(el).display; return !d.startsWith('inline') || d === 'inline-block' || d === 'inline-flex' || d === 'inline-grid'; };
  const out = [];
  document.querySelectorAll(rootSel).forEach(el => {
    if (el.closest('.notes')) return;
    const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden' || !isBlock(el)) return;
    if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
    const words = []; const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n;
    while ((n = w.nextNode())) {
      let a = n.parentElement; while (a !== el && !isBlock(a)) a = a.parentElement; if (a !== el) continue;
      const re = /\S+/g; let m;
      while ((m = re.exec(n.textContent))) { const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length); const rc = r.getClientRects(); if (rc.length) words.push({ w: m[0], top: rc[0].top }); }
    }
    if (words.length < 2) return;
    const lines = []; let c = null;
    words.forEach(x => { if (!c || Math.abs(x.top - c.top) > 6) { c = { top: x.top, ws: [] }; lines.push(c); } c.ws.push(x.w); });
    if (lines.length < 2) return;
    const sec = el.closest('.slide'); const si = sec ? [...document.querySelectorAll('#stage > .slide')].indexOf(sec) + 1 : 0;
    lines.forEach((l, k) => { const real = l.ws.filter(x => !/^[—–\-·→⇄:,.;!?"“”…()↻↓]+$/.test(x)); if (real.length <= 1) out.push('slide ' + si + ' · dòng ' + (k + 1) + '/' + lines.length + ': "' + l.ws.join(' ') + '" ← ' + el.textContent.trim().replace(/\s+/g, ' ').slice(0, 60)); });
  });
  st.remove();
  return out;
};
