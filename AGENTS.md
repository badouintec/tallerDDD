# AGENTS.md — reglas para agentes de IA en este repositorio

## Objetivo

Este repositorio tiene **dos ejercicios vinculados**: análisis de carrera con CSV en Colab (`ejercicio_1/`) y un sitio profesional estático (la raíz). El sitio de ejemplo es de Mateo Duarte, un personaje de demostración; cada estudiante lo **sustituye por su propia información**.

## Prioridades del agente

1. **Verdad antes que apariencia.** Al personalizar el sitio de un estudiante, no inventar empleos, premios, escuelas, métricas, certificados ni perfiles sociales.
2. **HTML, CSS y JS simples.** Sitio estático, accesible y rápido. Prohibido introducir React, Tailwind, bundlers, Node/npm o frameworks salvo petición expresa y justificada.
3. **Ponytail — simplicidad.** Cambio mínimo, reutilizar lo existente, eliminar complejidad. Al entregar: pruebas hechas, pendientes y riesgos. Referencia: <https://ponytail.dev/>
4. **No perder la función.** Verificar menú en celular, enlaces, responsive, modo oscuro, impresión del CV y páginas del blog.
5. **Publicación segura.** Publicar SOLO `dist/`, generado con `python3 build.py`. Nunca publicar `ejercicio_1/`, CSV, notebooks, `.md` ni claves. Si agregas un archivo público nuevo en la raíz, añádelo a `PUBLICO` en `build.py`.
6. **Indexación responsable.** Mantener `noindex,nofollow` mientras el sitio tenga contenido de ejemplo. Quitarlo solo cuando el estudiante confirme que todo es real y haya definido `PUBLIC_SITE_URL`.
7. **SEO sin trucos.** Títulos y descripciones honestos, `alt`, estructura semántica, JSON-LD solo con datos verificables. Mantener `sitemap.xml` al día al agregar o quitar artículos.
8. **Privacidad.** Jamás incrustar claves, correos ajenos, datos de estudiantes ni resultados privados.
9. **Datos del Ejercicio 1.** Mantener los CSV originales por fuente y unidad. No mezclar salarios de México con EE. UU., ni interpretar K-Means como predicción de contratación.
10. **Proceso.** Leer el README, proponer un plan breve, modificar pocos archivos, ejecutar `python3 build.py` y describir qué cambió. Si una herramienta no está disponible, no fingir haberla usado.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `index.html` | Portada con secciones comentadas |
| `blog/` | Artículos; rutas con `../` |
| `assets/css/styles.css` | Diseño; sección 1 = colores y fuentes (claro y oscuro) |
| `assets/js/main.js` | Menú en celular, imprimir CV, año |
| `assets/img/` | Fotos WebP en 3 tamaños + favicon |
| `robots.txt`, `sitemap.xml` | SEO; dominio de ejemplo `https://example.com` |
| `_headers` | Cabeceras de seguridad de Cloudflare |
| `build.py` | Genera `dist/` y valida privacidad, SEO y enlaces |
| `ejercicio_1/` | Análisis de carrera en Colab; nunca se publica |

## Criterios de aceptación

- [ ] `python3 build.py` termina sin errores.
- [ ] Sin errores de consola ni enlaces rotos.
- [ ] Navegación por teclado, celular y escritorio; modo oscuro legible.
- [ ] Fotos con `alt` y WebP; sin fuentes ni scripts externos.
- [ ] El CV se imprime solo, sin el resto del sitio.
- [ ] Las imágenes no se deforman.
- [ ] `noindex` activo mientras haya contenido de ejemplo.
- [ ] Puedes explicar qué produjo el agente y qué cambiaste y verificaste tú.
