'use strict';

const header = document.querySelector('.site-header');
const toggle = document.querySelector('[data-menu-toggle]');
const nav = document.getElementById('navigasi-utama');
const mobile = window.matchMedia('(max-width: 767px)');

if (header && toggle && nav) {
  function closeMenu(restoreFocus = false) {
    if (restoreFocus) toggle.focus();
    header.classList.remove('menu-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Buka menu navigasi');
  }

  function openMenu() {
    header.classList.add('menu-open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Tutup menu navigasi');
  }

  toggle.addEventListener('click', () => {
    if (header.classList.contains('menu-open')) closeMenu();
    else openMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && mobile.matches && header.classList.contains('menu-open')) {
      event.preventDefault();
      closeMenu(true);
    }
  });
  header.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link || !mobile.matches) return;
    // Move focus out before collapsing the navigation, including same-page links.
    const url = new URL(link.href);
    const target = url.pathname === location.pathname && url.hash
      ? document.getElementById(decodeURIComponent(url.hash.slice(1))) : null;
    if (target) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    } else toggle.focus();
    closeMenu();
  });
  mobile.addEventListener('change', () => {
    if (mobile.matches && nav.contains(document.activeElement)) openMenu();
    else {
      if (!mobile.matches && document.activeElement === toggle) nav.querySelector('a').focus();
      closeMenu();
    }
  });
  header.classList.add('menu-ready');
  toggle.hidden = false;
}

for (const gallery of document.querySelectorAll('[data-gallery]')) {
  const frames = [...gallery.querySelectorAll('[data-gallery-image]')];
  const buttons = [...gallery.querySelectorAll('[data-gallery-thumb]')];
  const controls = gallery.querySelector('[data-gallery-controls]');
  const status = gallery.querySelector('[data-gallery-status]');
  if (frames.length < 2 || !controls || buttons.length !== frames.length ||
      !buttons.every(button => frames.some(frame => frame.id === button.dataset.image))) continue;

  function selectImage(button) {
    for (const frame of frames) frame.hidden = frame.id !== button.dataset.image;
    for (const thumb of buttons) thumb.setAttribute('aria-pressed', String(thumb === button));
    if (status) status.textContent = button.getAttribute('aria-label').replace('Tampilkan ', '');
  }

  for (const button of buttons) button.addEventListener('click', () => selectImage(button));
  gallery.classList.add('gallery-ready');
  selectImage(buttons[0]);
  controls.hidden = false;
  if (status) status.hidden = false;
}
