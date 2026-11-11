#!/usr/bin/env python3
"""Genera dist/ con SOLO los archivos públicos del sitio y revisa que todo esté bien.

Uso:   python3 build.py
Vista: python3 -m http.server 8000 --directory dist

Por qué existe: el repositorio también guarda ejercicio_1/ (CSV, notebook) y
documentos internos que NO deben publicarse. Este script copia a dist/ solo lo
que aparece en PUBLICO; Cloudflare Pages publica únicamente dist/.

Variable opcional PUBLIC_SITE_URL=https://tu-dominio: reemplaza el dominio de
ejemplo (https://example.com) en canonical, Open Graph, robots.txt y sitemap.xml.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import os
import shutil

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
PUBLICO = ['index.html', 'robots.txt', 'sitemap.xml', '_headers', 'assets', 'blog']
DOMINIO_EJEMPLO = 'https://example.com'
PROHIBIDOS = {'.csv', '.ipynb', '.zip', '.png', '.md', '.py'}


class Rutas(HTMLParser):
    """Junta todas las rutas de href, src y srcset de una página."""
    def __init__(self):
        super().__init__()
        self.rutas = []

    def handle_starttag(self, tag, attrs):
        for nombre, valor in attrs:
            if nombre in ('href', 'src') and valor:
                self.rutas.append(valor)
            elif nombre == 'srcset' and valor:
                self.rutas += [parte.split()[0] for parte in valor.split(',')]


def main():
    url = os.environ.get('PUBLIC_SITE_URL', '').strip().rstrip('/')
    if url:
        p = urlsplit(url)
        if p.scheme != 'https' or not p.netloc or p.path:
            raise SystemExit('PUBLIC_SITE_URL debe ser https://dominio, sin ruta')

    # 1. Copiar solo lo público
    shutil.rmtree(DIST, ignore_errors=True)
    DIST.mkdir()
    for nombre in PUBLICO:
        origen = ROOT / nombre
        if origen.is_dir():
            shutil.copytree(origen, DIST / nombre)
        else:
            shutil.copy2(origen, DIST / nombre)

    # 2. Poner el dominio real, si se definió
    archivos = [f for f in DIST.rglob('*') if f.is_file()]
    if url:
        for f in archivos:
            if f.suffix in ('.html', '.xml', '.txt'):
                f.write_text(f.read_text(encoding='utf-8').replace(DOMINIO_EJEMPLO, url), encoding='utf-8')

    # 3. Revisiones: privacidad, SEO básico y enlaces rotos
    filtrados = [f.name for f in archivos if f.suffix.lower() in PROHIBIDOS]
    assert not filtrados, f'Archivos privados en dist/: {filtrados}'
    paginas = sorted(DIST.rglob('*.html'))
    indexables, revisadas = [], 0
    for pagina in paginas:
        html = pagina.read_text(encoding='utf-8')
        nombre = pagina.relative_to(DIST)
        assert '<title>' in html and 'name="description"' in html, f'Falta title o description en {nombre}'
        if 'noindex' not in html:
            indexables.append(str(nombre))
            assert DOMINIO_EJEMPLO not in html, f'{nombre} es indexable pero usa example.com: define PUBLIC_SITE_URL'
        lector = Rutas()
        lector.feed(html)
        for ruta in lector.rutas:
            if urlsplit(ruta).scheme or ruta.startswith(('#', 'mailto:')):
                continue
            destino = (pagina.parent / urlsplit(ruta).path).resolve()
            assert destino.is_file(), f'Enlace roto en {nombre}: {ruta}'
            revisadas += 1

    print(f'Listo: dist/ con {len(archivos)} archivos, {len(paginas)} páginas y {revisadas} rutas válidas.')
    print('Páginas indexables: ' + (', '.join(indexables) if indexables else 'ninguna (noindex activo).'))


if __name__ == '__main__':
    main()
