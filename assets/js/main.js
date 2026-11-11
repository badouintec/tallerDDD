/* JavaScript del sitio: solo tres comportamientos pequeños.
   Se carga con "defer" en index.html y blog/*.html, así que el HTML ya existe
   cuando se ejecuta. Si un elemento no está en la página, su bloque se omite. */
(() => {
  'use strict';

  // 1. MENÚ EN CELULAR
  // El botón "Menú ☰" (data-menu-toggle) muestra u oculta la navegación (data-nav)
  // añadiendo la clase .open, definida en la sección 12 de styles.css.
  // aria-expanded y aria-label informan el estado a los lectores de pantalla.
  const toggle = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    });
    // Al elegir una opción, el menú se cierra solo.
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Abrir menú');
    }));
  }

  // 2. IMPRIMIR CV
  // Cualquier botón con data-print abre el diálogo de impresión del navegador.
  // Lo que se imprime (solo el CV) lo decide @media print en styles.css.
  document.querySelectorAll('[data-print]').forEach(btn => {
    btn.addEventListener('click', () => window.print());
  });

  // 3. AÑO DEL PIE DE PÁGINA
  // Sustituye el año escrito en el HTML por el año actual.
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
