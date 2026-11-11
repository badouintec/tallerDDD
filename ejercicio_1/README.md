# Career Intelligence Sonora 2026 — Laboratorio 1

**Ejercicio:** ¿Hacia dónde debe apuntar mi carrera en función de la economía de Sonora, las vacantes observadas y las posibilidades de formación en México y Estados Unidos?

**Datos compilados:** 11 de noviembre de 2026. **Sin API ni scraping en clase.** Los datos se consultan directamente desde archivos CSV precompilados. El notebook es ejecutable en Google Colab con un solo ZIP de datos.

## Materiales

- `Career_Intelligence_Sonora_2026.ipynb`: notebook interactivo de Google Colab.
- `Career_Intelligence_Sonora_2026.py`: mismas celdas, para consulta o ejecución con Python local y carpeta `datos/`.
- `CSV_Career_Intelligence_Sonora_2026.zip`: contiene **15 CSV** en `datos/` y un manifiesto JSON.
- `datos/`: tablas separadas por fuente, unidad, territorio, fecha y calidad.
- `GUIA_DOCENTE_Y_ESTUDIANTE.md`: desarrollo metodológico, agenda y preguntas.
- `MANIFIESTO.json`: conteos de filas y límites del corpus.

## Apertura rápida en Google Colab

1. Abre [https://colab.research.google.com/](https://colab.research.google.com/).
2. En **Archivo → Subir notebook**, selecciona `Career_Intelligence_Sonora_2026.ipynb`.
3. Ejecuta la primera celda de Python. Cuando Colab lo solicite, sube `CSV_Career_Intelligence_Sonora_2026.zip`. **No tienes que descomprimirlo ni subir 15 archivos uno por uno.**
4. Ejecuta las demás celdas en orden. Las visualizaciones Plotly son interactivas y el mapa funciona sin usar APIs de geocodificación.
5. Para cambiar de carrera, modifica **solo** la celda de configuración (celda 2) y vuelve a ejecutar la celda de brechas y las que le siguen. Ejemplos:

```python
CARRERA = 'Mecatrónica'
HABILIDADES_ACTUALES = ['excel', 'sensores', 'python', 'ingles']
ANIO_EGRESO = 2027
```

> Las habilidades de Mateo Duarte Armenta son **inventadas para fines didácticos**. Deben sustituirse por habilidades demostrables en casos reales.

6. En la última celda, el notebook descarga `plan_carrera_mecatrónica.md` (o el nombre correspondiente al área elegida).

**Requisitos:** navegador, cuenta Google para guardar el notebook, y ZIP de los CSV. Colab suele incluir pandas, numpy, scikit-learn y Plotly. El código no instala librerías ni usa claves API.

## Preguntas conductoras

1. ¿En qué sectores hay empleo, valor agregado y capacidades ya observadas en Sonora? ¿Son lo mismo?
2. ¿Qué significa que Sonora tenga un cociente de localización manufacturero de aproximadamente **1.183**? ¿Qué no significa?
3. ¿Cuánto ganan los profesionistas de campos de ingeniería **a nivel nacional**, y qué parte de esa cifra no aplica directamente a un estudiante recién egresado en Hermosillo?
4. ¿Qué habilidades están presentes en anuncios de Hermosillo? ¿Qué empleo es realmente accesible con 0–2 años de experiencia?
5. ¿Qué ocupaciones y programas de EE. UU. ofrecen pistas para investigar, sin convertir los salarios norteamericanos en promesas para México?
6. ¿Qué decide un estudiante investigar durante sus siguientes 30 días?

## Fuentes y periodo

| Tema | Fuente primaria o institucional | Periodo y alcance |
|---|---|---|
| Economía Sonora | [INEGI Censos Económicos, resultados **definitivos**](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf) | Actividad de 2023; sector privado y empresas paraestatales |
| Economía México | [INEGI Censos Económicos, resultados **definitivos**](https://www.inegi.org.mx/programas/ce/2024/default.html) | Actividad de 2023, mismo universo para calcular LQ |
| Proyecciones demográficas | [COESPO — proyecciones CONAPO](https://coespo.sonora.gob.mx/images/documentos/Proyecciones2020-2070/Proyecciones2025-2040-Estatal.pdf) | Edición local de proyecciones 2025–2040 |
| Ingresos por carrera | [Observatorio Laboral STPS/INEGI](https://www.observatoriolaboral.gob.mx/static/estudios-publicaciones/Ingenierias.html) | Grupos profesionales, nacional, 2026-T2 |
| EE. UU. | [BLS Occupational Outlook Handbook](https://www.bls.gov/ooh/) | Salario mediano anual, mayo de 2025; previsión de empleo 2025–2035 |
| Vacantes | [TE Careers](https://careers.te.com/) / [Ford Careers](https://www.careers.ford.com/) | 13 anuncios específicos, consultados el 11/11/2026; no necesariamente activos después |
| Fundamentos ECI | [Data México — complejidad](https://www.economia.gob.mx/datamexico/es/eci/explore) | ECI/PCI: método ilustrado, no calculado en este notebook |
| Educación y carreras | [IMCO — metodología 2026](https://comparacarreras.imco.org.mx/metodologia/) | Distinción entre campos de estudio, ocupaciones y salarios |

## Reglas de lectura y límites críticos

- **El LQ es un índice de concentración de empleo**, no ECI ni un cálculo del futuro de semiconductores. Se calcula de forma reproducible sobre INEGI 2023, mismo universo para Sonora y México.
- **El censo de empleo no cuenta vacantes abiertas**. Las cifras de empleo total por sector y salarios por profesión proceden de universos distintos.
- **El sueldo del ingeniero mecatrónico en Hermosillo no está estimado en este paquete**. Observatorio Laboral publica grupos agregados de formación. No se inventa un salario estatal por carrera.
- Los ingresos nacionales de profesiones y las remuneraciones industriales anuales **no son directamente comparables entre sí**.
- **BLS Estados Unidos** presenta salarios en USD/año mediano ocupacional, no remuneraciones de candidatos mexicanos ni salarios iniciales; los crecimientos de algunas ocupaciones están publicados por grupo.
- Los anuncios son una **muestra ilustrativa y sesgada** (mayoría TE Connectivity): el conteo de puestos en el CSV **no representa la oferta de vacantes de Sonora**. Se dejan en blanco los salarios o años no especificados. El texto exacto del anuncio prevalece sobre el etiquetado manual.
- Las habilidades en `08_vacantes_hermosillo_muestra.csv` fueron **codificadas manualmente**; sus afinidades de carrera son orientativas, no requisitos oficiales ni probabilidades.
- K-Means agrupa anuncios por palabras clave codificadas; **no aprende de empleabilidad real**, no clasifica personas y **no pronostica puestos ni salarios**.
- El mapa tiene **centros urbanos aproximados**, no direcciones de plantas. Empresas y universidades están documentadas, pero las coordenadas de los puntos no son geocodificación oficial de sus instalaciones.
- Los posgrados y certificaciones tienen páginas oficiales de referencia; verificar disponibilidad, reconocimiento, requisitos, costos y restricciones de inmigración antes de aplicar.

## Para profundizar

Es posible ampliar el laboratorio con [microdatos ENOE de INEGI](https://www.inegi.org.mx/programas/enoe/15ymas/), registros de empresas, [portal Data México](https://www.economia.gob.mx/datamexico/), [Harvard Growth Lab](https://growthlab.hks.harvard.edu/) o un censo más amplio y balanceado de vacantes. Esas ampliaciones requieren verificar definiciones y no están simuladas por estos CSV.
