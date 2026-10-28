/* Pro Choice Roofing — shared behaviour.
   Degrades gracefully: without GSAP or Lenis everything is still visible and usable. */
(function () {
  /* ===== EDIT CONTACT DETAILS HERE (updates every page) ===== */
  var CONFIG = {
    phone: '087 438 5708', phoneHref: 'tel:+353874385708',
    whatsapp: 'https://wa.me/353874385708',
    email: 'prochoiceroofers@gmail.com',
    address: '20 Mount Eustace Crescent, Dublin 15, D15 RY6R',
    // Paste a Web3Forms access key here (free at web3forms.com) to have forms send straight to the inbox.
    // Left blank, forms open the visitor's email app with everything filled in.
    formEndpoint: 'https://api.web3forms.com/submit',
    formKey: ''
  };
  /* ============================================================ */
  const html = document.documentElement;
  html.classList.add('js');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer: fine)').matches;
  const touch = !fine;
  const G = typeof gsap !== 'undefined';
  const ST = G && typeof ScrollTrigger !== 'undefined';
  if (ST) gsap.registerPlugin(ScrollTrigger);
  if (touch) html.classList.add('touch');
  if (G && ST && !touch && !reduce) html.classList.add('gsap');
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const rand = (a, b) => a + Math.random() * (b - a);

  /* config fill */
  $$('[data-cfg]').forEach(el => {
    const k = el.dataset.cfg;
    if (k === 'phone') { el.textContent = CONFIG.phone; if (el.tagName === 'A') el.href = CONFIG.phoneHref; }
    else if (k === 'email') { el.textContent = CONFIG.email; if (el.tagName === 'A') el.href = 'mailto:' + CONFIG.email; }
    else if (k === 'year') el.textContent = new Date().getFullYear();
    else if (k in CONFIG) el.textContent = CONFIG[k];
  });
  $$('a[data-href="phone"]').forEach(a => a.href = CONFIG.phoneHref);
  $$('a[data-href="whatsapp"]').forEach(a => a.href = CONFIG.whatsapp);
  $$('a[data-href="email"]').forEach(a => a.href = 'mailto:' + CONFIG.email);

  /* smooth scroll (desktop only) */
  let lenis = null;
  if (!reduce && fine && typeof Lenis !== 'undefined') {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    if (G) { lenis.on('scroll', () => ST && ScrollTrigger.update()); gsap.ticker.add(t => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0); }
    else { const raf = t => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf); }
  }
  const lockScroll = on => { if (lenis) on ? lenis.stop() : lenis.start(); };

  /* header */
  const hdr = $('.hdr');
  const onScroll = () => hdr && hdr.classList.toggle('solid', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* mobile menu */
  const burger = $('.burger');
  if (burger) burger.addEventListener('click', () => {
    const open = html.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open); lockScroll(open);
  });
  $$('.mnav a').forEach(a => a.addEventListener('click', () => { html.classList.remove('menu-open'); lockScroll(false); }));
  // Services opens as a drop-down in the phone menu
  $$('.mtog').forEach(b => b.addEventListener('click', () => {
    const acc = b.closest('.macc'), open = !acc.classList.contains('open');
    acc.classList.toggle('open', open); b.setAttribute('aria-expanded', String(open));
  }));

  /* quote panel: drops down from under the header (like vantageroofing.ie) */
  const qd = $('#qdrop');
  const setQ = open => {
    if (!qd) return;
    html.classList.toggle('qdrop-open', open); qd.setAttribute('aria-hidden', String(!open));
    $$('.qbtn').forEach(b => b.setAttribute('aria-expanded', String(open)));
    if (open) { html.classList.remove('menu-open'); if (burger) burger.setAttribute('aria-expanded', 'false'); lockScroll(false); }
    if (open && fine) setTimeout(() => { const f = $('input:not(.hp)', qd); if (f) f.focus({ preventScroll: true }); }, 380);
  };
  $$('[data-quote]').forEach(b => b.addEventListener('click', e => {
    e.preventDefault();
    const sel = qd && $('select[name=service]', qd); if (sel && b.dataset.svc) sel.value = b.dataset.svc;
    setQ(b.classList.contains('qbtn') ? !html.classList.contains('qdrop-open') : true);
  }));
  $$('[data-qclose]').forEach(b => b.addEventListener('click', () => setQ(false)));
  document.addEventListener('click', e => { if (html.classList.contains('qdrop-open') && !e.target.closest('.hdr, [data-quote]')) setQ(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape') { setQ(false); closeLb(); } });
  if (location.hash === '#quote') setQ(true);

  /* job clips play while on screen */
  $$('video[data-autoplay]').forEach(v => new IntersectionObserver(es => es[0].isIntersecting ? v.play().catch(() => {}) : v.pause(), { threshold: 0.25 }).observe(v));

  /* forms */
  $$('form[data-form]').forEach(form => {
    const msg = $('.fmsg', form);
    const say = (t, ok) => { if (!msg) return; msg.textContent = t; msg.className = 'fmsg ' + (ok ? 'ok' : 'err'); };
    form.addEventListener('submit', async e => {
      e.preventDefault();
      let bad = null;
      $$('[required]', form).forEach(f => {
        const ok = f.value.trim() && f.checkValidity();
        f.closest('label').classList.toggle('bad', !ok);
        if (!ok && !bad) bad = f;
      });
      if (bad) { say('Please fill in the highlighted fields.'); bad.focus(); return; }
      if ($('.hp', form) && $('.hp', form).value) return;
      const data = Object.fromEntries(new FormData(form).entries()); delete data.botcheck;
      const subject = 'Website enquiry: ' + (data.service || 'Roofing quote') + ' – ' + (data.name || '');
      const body = Object.entries(data).filter(([, v]) => v).map(([k, v]) => k.charAt(0).toUpperCase() + k.slice(1) + ': ' + v).join('\n');
      const btn = $('button[type=submit]', form); const label = btn.innerHTML;
      if (CONFIG.formEndpoint && CONFIG.formKey) {
        btn.disabled = true; btn.textContent = 'Sending…';
        try {
          const r = await fetch(CONFIG.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ access_key: CONFIG.formKey, subject, from_name: 'Pro Choice Roofing website', ...data }) });
          const j = await r.json().catch(() => ({}));
          if (!r.ok || j.success === false) throw new Error();
          form.reset(); say('Thanks, we have your request. We aim to respond within 24 hours. If it’s urgent, call ' + CONFIG.phone + '.', true);
        } catch (err) { say('Sorry, that didn’t send. Please call ' + CONFIG.phone + ' or email ' + CONFIG.email + '.'); }
        btn.disabled = false; btn.innerHTML = label;
      } else {
        location.href = 'mailto:' + CONFIG.email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
        say('Your email app should now open with your details filled in. Just press send. Or call us on ' + CONFIG.phone + '.', true);
      }
    });
    $$('input,select,textarea', form).forEach(f => f.addEventListener('input', () => f.closest('label') && f.closest('label').classList.remove('bad')));
  });

  /* before / after sliders: drag anywhere on the photo (mouse or finger) */
  $$('.compare').forEach(c => {
    const r = $('input', c);
    const set = v => { r.value = v; c.style.setProperty('--p', v + '%'); };
    r.addEventListener('input', () => set(r.value)); set(r.value);
    let drag = false, sx = 0, sy = 0, lock = null;
    const at = x => { const b = c.getBoundingClientRect(); set(Math.round(Math.min(Math.max((x - b.left) / b.width, 0), 1) * 1000) / 10); };
    c.addEventListener('pointerdown', e => { drag = true; sx = e.clientX; sy = e.clientY; lock = e.pointerType === 'mouse' ? 'x' : null; if (lock) { at(e.clientX); c.setPointerCapture(e.pointerId); } e.preventDefault(); });
    c.addEventListener('pointermove', e => {
      if (!drag) return;
      if (!lock) { const dx = Math.abs(e.clientX - sx), dy = Math.abs(e.clientY - sy); if (dx < 6 && dy < 6) return; lock = dx > dy ? 'x' : 'y'; if (lock === 'x') c.setPointerCapture(e.pointerId); }
      if (lock === 'x') at(e.clientX);
    });
    const end = e => { if (drag && !lock && e.type === 'pointerup') at(e.clientX); drag = false; lock = null; };
    c.addEventListener('pointerup', end); c.addEventListener('pointercancel', end);
  });

  /* photo viewer: tap any photo to see it full size */
  const photos = [...$$('.gal a, .tile').map(a => ({ src: a.href, alt: ($('img', a) || {}).alt || '', el: a })),
    ...$$('.collage img, .ph img').map(img => ({ src: img.currentSrc || img.src, alt: img.alt, el: img }))];
  let lb = $('.lb'), lbI = 0;
  if (photos.length && !lb) {
    lb = document.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-label', 'Photo viewer');
    const ic = d => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="${d}"/></svg>`;
    lb.innerHTML = `<button class="x" aria-label="Close">${ic('M18 6L6 18M6 6l12 12')}</button><button class="pv" aria-label="Previous">${ic('M15 18l-6-6 6-6')}</button><img alt=""><button class="nx" aria-label="Next">${ic('M9 18l6-6-6-6')}</button>`;
    document.body.appendChild(lb);
  }
  function showLb(i) { lbI = (i + photos.length) % photos.length; const im = $('img', lb); im.src = photos[lbI].src; im.alt = photos[lbI].alt; }
  function closeLb() { if (lb && lb.classList.contains('on')) { lb.classList.remove('on'); lockScroll(false); } }
  if (lb && photos.length) {
    photos.forEach((ph, i) => { ph.el.classList.add('zoom'); ph.el.addEventListener('click', e => { e.preventDefault(); showLb(i); lb.classList.add('on'); lockScroll(true); }); });
    $('.x', lb).addEventListener('click', closeLb);
    $('.pv', lb).addEventListener('click', () => showLb(lbI - 1));
    $('.nx', lb).addEventListener('click', () => showLb(lbI + 1));
    lb.addEventListener('click', e => { if (e.target === lb) closeLb(); });
    addEventListener('keydown', e => { if (!lb.classList.contains('on')) return; if (e.key === 'ArrowLeft') showLb(lbI - 1); if (e.key === 'ArrowRight') showLb(lbI + 1); });
    let tx0 = null; lb.addEventListener('touchstart', e => tx0 = e.touches[0].clientX, { passive: true });
    lb.addEventListener('touchend', e => { if (tx0 == null) return; const dx = e.changedTouches[0].clientX - tx0; if (Math.abs(dx) > 50) showLb(lbI + (dx < 0 ? 1 : -1)); tx0 = null; });
  }

  /* rain */
  function rainOn(host, o = {}) {
    if (reduce) return null;
    const cv = document.createElement('canvas'); cv.className = 'rain'; cv.setAttribute('aria-hidden', 'true');
    host.insertBefore(cv, host.firstElementChild ? host.firstElementChild.nextSibling : null);
    const ctx = cv.getContext('2d'); let w, h, drops = [], vis = true, raf;
    const dpr = Math.min(devicePixelRatio || 1, 2);
    const size = () => { w = cv.clientWidth; h = cv.clientHeight; cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.round(w * h / 10000 * (o.density || 1)); drops = Array.from({ length: n }, () => ({ x: rand(0, w), y: rand(0, h), l: rand(10, 24), v: rand(9, 16) * (o.speed || 1), a: rand(.08, .28) * (o.alpha || 1) })); };
    size(); addEventListener('resize', size);
    const tick = () => {
      ctx.clearRect(0, 0, w, h); ctx.lineWidth = 1;
      for (const d of drops) {
        ctx.strokeStyle = (o.color || 'rgba(170,215,255,') + d.a + ')';
        ctx.beginPath(); ctx.moveTo(d.x, d.y); ctx.lineTo(d.x - d.l * .18, d.y + d.l); ctx.stroke();
        d.y += d.v; d.x -= d.v * .18;
        if (d.y > h) { d.y = -d.l; d.x = rand(0, w * 1.15); }
      }
      if (vis || o.always) raf = requestAnimationFrame(tick);
    };
    if (!o.always) new IntersectionObserver(es => { const was = vis; vis = es[0].isIntersecting; if (vis && !was) raf = requestAnimationFrame(tick); }).observe(host);
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }
  $$('[data-rain]').forEach(el => rainOn(el));

  /* ---------- intro: slates are laid across the screen from the eaves up,
     the logo is revealed, then the tiles lift away from the centre to open the page ---------- */
  const loader = $('#loader');
  function finishIntro() { if (loader) loader.remove(); html.classList.remove('intro'); heroIn(); if (ST) ScrollTrigger.refresh(); }
  function runIntro() {
    try { sessionStorage.setItem('pcr_intro', '1'); } catch (e) {}
    if (!loader || !html.classList.contains('intro') || reduce || !loader.animate) { finishIntro(); return; }
    const host = $('.slates', loader), W = innerWidth, H = innerHeight;
    const tw = Math.max(64, Math.min(140, W / 8)), th = Math.round(tw * .62), gap = 3;
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
    const layMs = 1000, per = layMs / rows;
    tiles.forEach(o => o.t.animate(
      [{ opacity: 0, transform: 'translateY(-46px) rotateX(70deg)' }, { opacity: 1, transform: 'none' }],
      { duration: 420, delay: (rows - 1 - o.r) * per + (o.x / W) * 120, easing: 'cubic-bezier(.2,.8,.2,1)', fill: 'forwards' }));
    // 2. light runs across the finished roof and the logo is revealed
    setTimeout(() => {
      loader.classList.add('laid');
      const sh = $('.sheen', loader);
      if (sh) sh.animate([{ opacity: 0, transform: 'translateX(-70%)' }, { opacity: 1, offset: .2 }, { opacity: 1, offset: .8 }, { opacity: 0, transform: 'translateX(70%)' }], { duration: 1300, easing: 'cubic-bezier(.5,0,.3,1)', fill: 'forwards' });
    }, layMs + 250);
    // 3. the tiles lift off from the centre outwards, revealing the home page underneath
    const openAt = layMs + 1900;
    setTimeout(() => {
      loader.classList.add('open'); heroIn();
      tiles.forEach(o => {
        const dx = o.x - cx, dy = o.y - cy, d = Math.hypot(dx, dy) / maxD, k = 60 + Math.random() * 80;
        o.t.animate([{ opacity: 1, transform: 'none' },
          { opacity: 0, transform: `translate(${dx / (d * maxD || 1) * k}px,${dy / (d * maxD || 1) * k - 30}px) rotateX(${55 + Math.random() * 30}deg) rotateZ(${(Math.random() - .5) * 30}deg) scale(.85)` }],
          { duration: 650, delay: d * 520, easing: 'cubic-bezier(.5,0,.75,0)', fill: 'forwards' });
      });
      setTimeout(finishIntro, 1250);
    }, openAt);
  }

  /* split headings into words */
  function splitWords(el) {
    if (el.dataset.splitDone) return $$('.w > span', el);
    const walk = node => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            const w = document.createElement('span'); w.className = 'w'; w.style.cssText = 'display:inline-block;overflow:hidden;vertical-align:bottom;padding-bottom:.08em;margin-bottom:-.08em';
            const i = document.createElement('span'); i.style.display = 'inline-block'; i.textContent = part;
            w.appendChild(i); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && !n.classList.contains('w')) walk(n);
      });
    };
    walk(el); el.dataset.splitDone = '1';
    return $$('.w > span', el);
  }

  /* hero entrance */
  let heroDone = false;
  function heroIn() {
    if (heroDone) return; heroDone = true;
    const hero = $('.hero, .phero'); if (!hero) return;
    $$('video', hero).forEach(v => v.play().catch(() => {}));
    if (!G || reduce) return;
    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
    const h = $('h1', hero);
    if (h) { if (touch) tl.from(h, { opacity: 0, y: 26, duration: 0.9, clearProps: 'all' }, 0.1); else tl.from(splitWords(h), { yPercent: 110, duration: 1, stagger: 0.045, clearProps: 'all' }, 0.05); }
    const gb = $('.gbadge', hero); if (gb) tl.from(gb, { opacity: 0, y: -12, scale: 0.96, duration: 0.7, clearProps: 'all' }, 0);
    const eb = $('.eyebrow, .crumb', hero); if (eb) tl.from(eb, { opacity: 0, x: -20, duration: 0.8, clearProps: 'all' }, 0.1);
    const lead = $('.lead', hero); if (lead) tl.from(lead, { opacity: 0, y: 20, duration: 0.9, clearProps: 'all' }, 0.45);
    const btns = $$('.btn-row .btn', hero); if (btns.length) tl.from(btns, { opacity: 0, y: 16, duration: 0.7, stagger: 0.1, clearProps: 'all' }, 0.6);
    const trust = $('.trust', hero); if (trust) tl.from(trust, { opacity: 0, y: 14, duration: 0.8, clearProps: 'all' }, 0.85);
    const vc = $('.vcard', hero); if (vc) tl.from(vc, { clipPath: 'inset(45% 0 45% 0 round 28px)', scale: 0.97, duration: 1.2, ease: 'power4.inOut', clearProps: 'all' }, 0.15);
    const fr = $('.vwrap .frame', hero); if (fr) tl.from(fr, { opacity: 0, scale: 1.05, duration: 1, clearProps: 'all' }, 0.9);
    const pill = $('.vwrap .pill', hero); if (pill) tl.from(pill, { opacity: 0, y: 20, scale: 0.92, duration: 0.7, ease: 'back.out(1.6)', clearProps: 'all' }, 1.2);
    const tag = $('.vwrap .tag', hero); if (tag) tl.from(tag, { opacity: 0, x: -14, duration: 0.6, clearProps: 'all' }, 1.1);
    const bg = $('img.bg', hero); if (bg && !touch) tl.from(bg, { scale: 1.12, duration: 1.8, ease: 'power2.out', clearProps: 'transform' }, 0);
    const sc = $('.scroll', hero); if (sc) tl.from(sc, { opacity: 0, duration: 0.8 }, 1.3);
  }

  /* scroll animations */
  function ioFx() {
    const els = $$('[data-reveal]').filter(el => !el.closest('.hero, .phero'));
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return; const el = e.target;
      if (el.dataset.reveal === 'group') [...el.children].forEach((c, i) => { c.style.transitionDelay = (i * 70) + 'ms'; });
      el.classList.add('in'); io.unobserve(el);
    }), { rootMargin: '0px 0px -6% 0px', threshold: 0.01 });
    els.forEach(el => io.observe(el));
    $$('[data-reveal]').filter(el => el.closest('.hero, .phero')).forEach(el => el.classList.add('in'));
  }
  function scrollFx() {
    if (reduce) { $$('[data-reveal]').forEach(el => el.classList.add('in')); return; }
    if (touch || !ST) { ioFx(); return; }
    gsap.defaults({ ease: 'power3.out' });
    $$('[data-reveal]').forEach(el => {
      el.classList.add('in');
      if (el.closest('.hero, .phero')) return;
      if (el.dataset.reveal === 'group') gsap.from(el.children, { y: 44, opacity: 0, duration: 1, stagger: 0.1, clearProps: 'transform,opacity', scrollTrigger: { trigger: el, start: 'top 88%' } });
      else gsap.from(el, { y: 44, opacity: 0, duration: 1, clearProps: 'transform,opacity', scrollTrigger: { trigger: el, start: 'top 90%' } });
    });
    $$('[data-split]').forEach(el => { if (el.closest('.hero, .phero')) return; gsap.from(splitWords(el), { yPercent: 110, duration: 0.9, stagger: 0.03, clearProps: 'all', scrollTrigger: { trigger: el, start: 'top 86%' } }); });
    $$('[data-clip]').forEach(el => {
      const img = $('img', el);
      const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 85%' } });
      tl.from(el, { clipPath: 'inset(0 0 100% 0 round 24px)', duration: 1.2, ease: 'power4.inOut', clearProps: 'clipPath' }, 0);
      if (img) tl.from(img, { scale: 1.2, duration: 1.6, ease: 'power3.out', clearProps: 'transform' }, 0);
    });
    $$('.weather .big').forEach(el => gsap.to(el, { xPercent: -14, ease: 'none', scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } }));
    $$('[data-count]').forEach(el => { const n = +el.dataset.count; const o = { v: 0 }; gsap.to(o, { v: n, duration: 1.6, ease: 'power2.out', onUpdate: () => el.textContent = Math.round(o.v), scrollTrigger: { trigger: el, start: 'top 90%' } }); });
  }

  scrollFx();
  runIntro();
})();
