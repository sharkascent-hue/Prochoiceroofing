/* Opening animation. Inlined straight after the loader markup so it starts the moment
   the page arrives, without waiting for fonts or the animation libraries. */
(function () {
  const html = document.documentElement, loader = document.getElementById('loader');
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const rand = (a, b) => a + Math.random() * (b - a);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, touch = !matchMedia('(pointer: fine)').matches;
  const signal = n => { window['__intro_' + n] = 1; dispatchEvent(new Event('intro:' + n)); };
  /* ---------- intro: slates are laid across the screen from the eaves up,
     the logo is revealed, then the tiles lift away from the centre to open the page ---------- */
  function finishIntro() { if (typeof stopIntroRain === 'function') stopIntroRain(); if (loader) loader.remove(); html.classList.remove('intro', 'intro-out'); signal('done'); }
  function runIntro() {
    try { sessionStorage.setItem('pcr_intro', '1'); } catch (e) {}
    if (!loader || !html.classList.contains('intro') || reduce || !loader.animate) { finishIntro(); return; }
    const host = $('.slates', loader), W = innerWidth, H = innerHeight;
    const tw = touch ? Math.max(76, W / 5) : Math.max(64, Math.min(140, W / 8)), th = Math.round(tw * .62), gap = 3;
    const cols = Math.ceil(W / tw) + 1, rows = Math.ceil(H / th) + 1;
    const cx = W / 2, cy = H / 2, maxD = Math.hypot(cx, cy), tiles = [];
    const frag = document.createDocumentFragment();
    for (let r = 0; r < rows; r++) {
      const off = r % 2 ? -tw / 2 : 0; // staggered bond, like a real slate roof
      for (let c = 0; c < cols + (r % 2); c++) {
        const t = document.createElement('i'), x = c * tw + off, y = r * th;
        t.className = 'sl' + (Math.random() < .3 ? ' b' : Math.random() < .3 ? ' c' : '');
        t.style.cssText = `left:${x + gap / 2}px;top:${y + gap / 2}px;width:${tw - gap}px;height:${th - gap}px;opacity:0`;
        frag.appendChild(t); tiles.push({ t, r, x: x + tw / 2, y: y + th / 2 });
      }
    }
    host.appendChild(frag);
    // 1. laid row by row from the bottom (the eaves) up to the top (the ridge)
    const layMs = 700, per = layMs / rows;
    tiles.forEach(o => o.t.animate(
      [{ opacity: 0, transform: touch ? 'translateY(-40px)' : 'translateY(-46px) rotateX(70deg)' }, { opacity: 1, transform: 'none' }],
      { duration: 380, delay: (rows - 1 - o.r) * per + (o.x / W) * 100, easing: 'cubic-bezier(.2,.8,.2,1)', fill: 'forwards' }));
    // 2. light runs across the finished roof and the logo is revealed
    setTimeout(() => {
      loader.classList.add('laid');
      const sh = $('.sheen', loader);
      if (sh) sh.animate([{ opacity: 0, transform: 'translateX(-70%)' }, { opacity: 1, offset: .2 }, { opacity: 1, offset: .8 }, { opacity: 0, transform: 'translateX(70%)' }], { duration: 1000, easing: 'cubic-bezier(.5,0,.3,1)', fill: 'forwards' });
    }, layMs + 120);
    // 3. the tiles lift off from the centre outwards, revealing the home page underneath
    const openAt = layMs + 1250;
    setTimeout(() => {
      loader.classList.add('open'); signal('open');
      tiles.forEach(o => {
        const dx = o.x - cx, dy = o.y - cy, d = Math.hypot(dx, dy) / maxD, k = 60 + Math.random() * 80;
        o.t.animate([{ opacity: 1, transform: 'none' },
          { opacity: 0, transform: `translate(${dx / (d * maxD || 1) * k}px,${dy / (d * maxD || 1) * k - 30}px) ${touch ? '' : `rotateX(${55 + Math.random() * 30}deg) `}rotateZ(${(Math.random() - .5) * 30}deg) scale(.85)` }],
          { duration: 520, delay: d * 380, easing: 'cubic-bezier(.5,0,.75,0)', fill: 'forwards' });
      });
      setTimeout(finishIntro, 950);
    }, openAt);
  }

  runIntro();
})();
