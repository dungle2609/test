// Tìm Playwright: cài cục bộ, NODE_PATH, hoặc bản cài sẵn trong môi trường cloud.
module.exports = (() => {
  const tries = ['playwright', process.env.PLAYWRIGHT_PATH, '/opt/node22/lib/node_modules/playwright'].filter(Boolean);
  for (const t of tries) { try { return require(t); } catch (e) { /* thử tiếp */ } }
  throw new Error('Không tìm thấy Playwright. Cài bằng "npm i playwright" hoặc đặt PLAYWRIGHT_PATH.');
})();
