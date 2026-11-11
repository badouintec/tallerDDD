# Prompts del taller

Prompts listos para copiar y pegar en tu agente de IA (Claude Code, Copilot, Codex, Cursor…).

**Cómo usarlos:**

1. Copia el prompt completo.
2. Sustituye **todo lo que está entre `[CORCHETES]`** con tu información real.
3. Si un campo no aplica o no lo puedes demostrar, **bórralo**: no lo inventes ni dejes que la IA lo invente.
4. Lee la propuesta del agente **antes** de aceptarla, y verifica el resultado abriendo `index.html` en tu navegador.

## Índice

1. [El prompt con el que se creó este sitio](#1-el-prompt-con-el-que-se-creó-este-sitio)
2. [Adaptar el diseño a tu disciplina](#2-adaptar-el-diseño-a-tu-disciplina)
3. [Llevar tu hipótesis del Ejercicio 1 a la sección Rumbo](#3-llevar-tu-hipótesis-del-ejercicio-1-a-la-sección-rumbo)
4. [AGENTS.md: las reglas de tu proyecto](#4-agentsmd-las-reglas-de-tu-proyecto)
5. [Ponytail: que la IA escriba menos](#5-ponytail-que-la-ia-escriba-menos)
6. [Graphify: entender el código antes de cambiarlo](#6-graphify-entender-el-código-antes-de-cambiarlo)
7. [Agregar un artículo al blog](#7-agregar-un-artículo-al-blog)
8. [SEO y accesibilidad](#8-seo-y-accesibilidad)
9. [Revisión final antes de publicar](#9-revisión-final-antes-de-publicar)
10. [Publicar en Cloudflare](#10-publicar-en-cloudflare)

---

## 1. El prompt con el que se creó este sitio

Este es un prompt **hipotético**: así se le pudo haber pedido a un agente el sitio de Mateo. Úsalo para crear **tu** versión desde cero, o para pedirle al agente que adapte este sitio a ti.

```text
Crea mi sitio web profesional personal. Lee primero AGENTS.md y respeta sus reglas.

## Quién soy
- Nombre completo: [TU NOMBRE COMPLETO]
- Carrera: [TU CARRERA], en [TU UNIVERSIDAD], [CIUDAD, ESTADO]
- Años de estudio: [AÑO DE INGRESO] — [AÑO DE EGRESO ESPERADO]
- Lo que busco: [PRÁCTICAS PROFESIONALES / PRIMER EMPLEO / BECA / PROYECTOS] para [AÑO]
- Una frase que me describe: [FRASE CORTA, ej. "Construyo sistemas que conectan software y mundo físico"]

## Sobre mí
- Qué me interesa de mi carrera: [2-3 FRASES EN TUS PALABRAS]
- Áreas en las que me enfoco: [ÁREA 1], [ÁREA 2], [ÁREA 3]
- Herramientas que sé usar (solo las que puedo demostrar): [HERRAMIENTA 1], [HERRAMIENTA 2], [HERRAMIENTA 3]
- Lo que estoy aprendiendo ahora: [CURSO O LIBRO 1 + estado], [CURSO O LIBRO 2 + estado]

## Mi rumbo (viene del Ejercicio 1)
- Hipótesis: [TU HIPÓTESIS DE CARRERA]
- Evidencia: [CIFRA + FUENTE + AÑO]
- Lo que la limita: [UN DATO QUE LA CONTRADICE O LIMITA]
- Próximos 30 días: [UNA ACCIÓN CONCRETA]

## Proyectos
- Proyecto principal: [NOMBRE], [AÑO], estado: [TERMINADO / EN DESARROLLO]
  Qué hace: [1-2 FRASES]. Tecnologías: [LISTA]. Foto: [RUTA DE LA FOTO]
- Otras líneas de exploración: [TEMA 1], [TEMA 2], [TEMA 3]

## CV
- Educación: [GRADO, INSTITUCIÓN, AÑOS]; [BACHILLERATO, INSTITUCIÓN, AÑOS]
- Reconocimientos (solo verificables): [PREMIO, ORGANIZADOR, AÑO]
- Idiomas: [IDIOMA Y NIVEL REAL]

## Contacto
- Correo: [TU CORREO]
- Perfiles (solo si existen): LinkedIn [URL], GitHub [URL], [OTRO PERFIL Y URL]

## Requisitos técnicos
- Solo HTML, CSS y JavaScript. Sin frameworks, sin npm, sin fuentes ni scripts externos.
- Archivos: index.html en la raíz, assets/css/styles.css, assets/js/main.js, assets/img/ y blog/.
- Secciones de index.html, en este orden: portada, Sobre mí, Rumbo, Proyectos, Blog, CV y Contacto.
  Cada sección empieza con un comentario HTML en español que explique para qué sirve.
- Todos los colores en variables CSS en una sola sección al inicio de styles.css,
  con modo oscuro automático (prefers-color-scheme).
- Diseño responsive: en celular, una columna y un botón "Menú" que abre y cierra la navegación.
- Botón "Imprimir / Guardar PDF" que imprima SOLO el CV (con @media print).
- Accesibilidad: alt en todas las imágenes, enlace "Saltar al contenido", contorno visible al navegar con Tab.
- SEO: title, description, Open Graph, JSON-LD de tipo Person, robots.txt y sitemap.xml.
  Usa https://example.com como dominio provisional y deja <meta name="robots" content="noindex,nofollow">.
- Fotos en WebP con srcset en 3 tamaños.

## Cómo trabajar
1. Primero dame un plan: qué archivos crearás y qué irá en cada uno. Espera mi aprobación.
2. No inventes experiencia, premios, cifras, certificados ni enlaces. Si falta un dato, pregúntame.
3. Al terminar, dime qué verificaste, qué no pudiste verificar y cómo lo pruebo yo.
```

---

## 2. Adaptar el diseño a tu disciplina

El sitio de ejemplo usa grises, negro y azul marino, que encajan con ingeniería. Tu disciplina puede pedir otra cosa.

```text
Mi disciplina es [TU DISCIPLINA, ej. Arquitectura / Psicología / Mercadotecnia / Biotecnología / Derecho].
Quiero que el sitio transmita: [3 ADJETIVOS, ej. "preciso, sobrio, confiable"].
Mi público principal es: [QUIÉN VISITARÁ EL SITIO, ej. reclutadores de despachos de arquitectura].
Sitios o portafolios de mi área que me gustan (solo como referencia, no para copiar): [URL 1], [URL 2].

Analiza index.html y la sección 1 de assets/css/styles.css y propón:
1. Una paleta para las variables de la sección 1 (modo claro y oscuro), con contraste suficiente para leer (WCAG AA).
2. Si conviene usar títulos con serif o sans-serif, usando solo fuentes del sistema (sin Google Fonts).
3. Qué secciones sobran o faltan para mi disciplina (por ejemplo, una galería para Arquitectura o publicaciones para Investigación).
4. Qué tipo de fotos debería usar.

Primero muéstrame la propuesta con los colores en una tabla. No cambies nada hasta que la apruebe.
Cuando la apruebe, cambia SOLO las variables de la sección 1 y lo mínimo necesario.
```

---

## 3. Llevar tu hipótesis del Ejercicio 1 a la sección Rumbo

```text
Lee mi archivo [NOMBRE DE TU PLAN, ej. plan_carrera_mecatrónica.md] del Ejercicio 1.
Actualiza la sección Rumbo de index.html con los cuatro campos de "Mi decisión":
hipótesis, evidencia, lo que la limita y próximos 30 días.

Reglas:
- Usa solo cifras que estén en mi plan, con su fuente y su año.
- No conviertas la hipótesis en una promesa de empleo ni de sueldo.
- No mezcles salarios de México con los de Estados Unidos.
- Mantén la misma estructura HTML (.compass, .compass-main, .compass-item).
```

---

## 4. AGENTS.md: las reglas de tu proyecto

`AGENTS.md` es el archivo que lee el agente antes de trabajar. Ya existe uno; este prompt lo adapta a tu proyecto.

```text
Lee el AGENTS.md actual y adáptalo a mi proyecto. Mi sitio es de [TU NOMBRE], de [TU CARRERA].

Conserva estas reglas:
- Verdad antes que apariencia: no inventar empleos, premios, métricas, certificados ni perfiles.
- Solo HTML, CSS y JS, sin frameworks ni npm.
- Publicación segura: lo privado va en .assetsignore.
- La sección "Ponytail" del final, sin cambios.

Agrega estas reglas propias:
- [REGLA 1, ej. "Todo el texto del sitio en español neutro y en primera persona"]
- [REGLA 2, ej. "No mostrar mi teléfono ni mi dirección"]
- [REGLA 3, ej. "Las fotos de proyectos deben indicar si son prototipos o productos terminados"]

Actualiza la tabla de "Estructura" si agregué o quité archivos.
Muéstrame el cambio como diferencias (antes/después) antes de guardarlo.
```

---

## 5. Ponytail: que la IA escriba menos

[Ponytail](https://ponytail.dev/) ya está instalado en este repositorio (al final de `AGENTS.md` y en `.github/copilot-instructions.md`).

**Si tu proyecto aún no lo tiene:**

```text
Instala Ponytail en este proyecto siguiendo su guía oficial:
https://github.com/DietrichGebert/ponytail/blob/main/INSTALL.md
Uso [TU AGENTE, ej. GitHub Copilot en VS Code / Claude Code / Cursor].
Instálalo solo a nivel de proyecto. Dime qué archivos agregaste y qué hace cada uno.
```

**Para revisar tu sitio con Ponytail:**

```text
Aplica las reglas de Ponytail (sección "Ponytail" de AGENTS.md) a todo el sitio:
index.html, blog/, assets/css/styles.css y assets/js/main.js.

Dame una lista ordenada de:
1. Qué se puede BORRAR sin que se pierda nada (reglas CSS sin uso, clases repetidas, código muerto).
2. Qué se puede SIMPLIFICAR usando algo que ya existe en el proyecto o en el navegador.
Para cada punto: archivo, línea, qué quitar y cómo comprobar que nada se rompió.
No cambies nada todavía.
```

---

## 6. Graphify: entender el código antes de cambiarlo

Este repositorio ya incluye un mapa generado en `graphify-out/`. Ver la [guía, sección 7.2](docs/GUIA.md#72-graphify-el-mapa-de-tu-código).

**Instalarlo y generar tu propio mapa:**

```text
Quiero usar Graphify para ver el mapa de mi proyecto.
1. Crea un entorno virtual de Python en .venv/ e instala el paquete anytechie-graphify.
2. Genera el grafo con: ./.venv/bin/graphify update .
3. Revisa graphify-out/ y quita cualquier ruta de mi computadora (por ejemplo /Users/[MI USUARIO]/)
   antes de que lo suba a GitHub.
4. Confirma que .venv/ esté en .gitignore (no se sube) y graphify-out/ en .assetsignore (se sube a GitHub, pero no se publica en el sitio).
Mi sistema operativo es [macOS / Windows / Linux].
```

**Usar el mapa para entender el código:**

```text
Lee graphify-out/GRAPH_REPORT.md y graphify-out/graph.json.
Explícame, como si fuera principiante:
1. Qué archivos y funciones tiene mi proyecto y cómo se conectan.
2. Qué parte del código tocaría si quisiera cambiar [LO QUE QUIERES CAMBIAR, ej. "cómo se abre el menú"].

Importante: Graphify usa una IA externa para nombrar los grupos y a veces se equivoca.
Verifica cada afirmación contra el código real y dime cuáles del reporte son incorrectas.
```

---

## 7. Agregar un artículo al blog

```text
Agrega un artículo nuevo al blog sobre [TEMA DEL ARTÍCULO].
Contenido: [PEGA AQUÍ TUS NOTAS O BORRADOR].
Fecha: [MES Y AÑO]. Categoría: [CATEGORÍA]. Foto de portada: [RUTA O "sin foto"].

1. Crea blog/[nombre-corto].html copiando la estructura de blog/olimpiada.html.
2. Agrega su tarjeta en la sección Blog de index.html (si no hay foto, usa una portada con símbolo como la de ∑).
3. Agrega su URL a sitemap.xml (sin .html al final).
4. Escribe un title y una description propios para este artículo.
No inventes datos que no estén en mis notas.
```

---

## 8. SEO y accesibilidad

```text
Audita el SEO y la accesibilidad de index.html y de blog/.
Revisa: title, description, encabezados (un solo h1 por página), Open Graph, alt de imágenes,
JSON-LD, canonical, robots.txt, sitemap.xml, contraste de colores, navegación con Tab y enlaces rotos.

Separa en dos listas:
1. Lo que puedo comprobar en mi computadora.
2. Lo que necesita el sitio publicado (por ejemplo, la vista previa al compartir en WhatsApp).
No prometas posiciones en Google. No quites noindex.
```

---

## 9. Revisión final antes de publicar

```text
Antes de publicar, revisa todo el proyecto y responde con una lista de verificación:
- ¿Quedó algún dato de Mateo Duarte o de example.com que deba reemplazar? Dime archivo y línea.
- ¿Hay alguna afirmación que no pueda demostrar (premios, cifras, cursos terminados, perfiles)?
- ¿Algún archivo privado se publicaría? Compara la raíz con .assetsignore.
- ¿Funciona el menú en celular, la impresión del CV y el modo oscuro?
- ¿Todas las imágenes tienen alt y existen?
Mi dominio final será: [TU URL, ej. https://ana-lopez.tu-subdominio.workers.dev].
Si ya todo es real, dime exactamente qué líneas cambiar para quitar noindex y poner mi dominio.
```

---

## 10. Publicar en Cloudflare

```text
Voy a publicar mi sitio en Cloudflare Workers desde GitHub.
Mi repositorio es: [USUARIO/REPOSITORIO]. Quiero que el proyecto se llame: [NOMBRE-DEL-PROYECTO].

1. Cambia "name" en wrangler.jsonc por [NOMBRE-DEL-PROYECTO].
2. Verifica que .assetsignore excluya ejercicio_1/, docs/, los archivos .md y los archivos ocultos.
3. Dime exactamente qué escribir en cada campo del formulario de Cloudflare
   (Project name, Build command, Deploy command, Preview builds, Cloudflare Access).
No crees ramas: todo va directo a main.
```

← [Volver al README](README.md)
