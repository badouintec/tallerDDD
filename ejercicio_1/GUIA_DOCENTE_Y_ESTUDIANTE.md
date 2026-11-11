# Guía del ejercicio 1 — Career Intelligence Sonora

## Objetivo andragógico

Tomar una decisión profesional **argumentada y provisional**, no imponer una especialización a todos. La primera persona estudiante que analicemos será un personaje **ficticio**: Mateo Duarte Armenta, 21 años, cursa Mecatrónica en la Universidad de Tecnología e Innovación del Desierto (institución **ficticia**), con egreso estimado en 2027. Sus intereses y habilidades se construyen como escenario de clase, no datos reales.

**Pregunta abierta:** «Si estoy a uno o dos años de egresar, ¿cuál es el mapa económico y laboral que debería investigar, y qué proyectos o cursos podría tomar para probar una trayectoria?»

### Agenda sugerida: 80 minutos

| Minuto | Experiencia | Entregable cognitivo |
|---|---|---|
| 0–8 | Mostrar el caso y preguntar hipótesis: ¿mecatrónica = semiconductores? | Hipótesis inicial escrita sin IA |
| 8–18 | Censos definitivos INEGI; ocupación, valor agregado, sectores; cociente de localización | Interpretación correcta de LQ y límites |
| 18–27 | Demografía COESPO/CONAPO, peso de Hermosillo y otros municipios | Una inferencia sobre territorio y generación de empleo |
| 27–38 | Sueldos nacionales OLA vs remuneraciones sectoriales vs BLS EE. UU. | Tres métricas sin mezclarlas |
| 38–51 | Vacantes reales de Hermosillo: lectura del texto, habilidades explícitas, experiencia | Lista de brechas con una corrección de IA/dato |
| 51–61 | K-Means: ver etiquetas, grupos, PCA; repetir con otra carrera | Aprendizaje de ML transparente, sin falsos pronósticos |
| 61–70 | Mapa municipios Sonora y nodos Sonora/Arizona; programas oficiales | Identificar opciones verificables, no ubicaciones ficticias |
| 70–80 | Cambiar una variable de carrera/perfil y exportar plan | Hipótesis profesional y acción de 30 días |

## Instrucciones de Colab

Abrir `Career_Intelligence_Sonora_2026.ipynb` en https://colab.research.google.com/ y subir una sola vez `CSV_Career_Intelligence_Sonora_2026.zip` cuando aparezca el selector. Los cálculos se realizan localmente dentro del notebook a partir de los CSV; las gráficas Plotly permiten hacer zoom, filtrar en leyendas y consultar información pasando el cursor.

## Definiciones y fórmula

**Personal ocupado**: personas trabajando en unidades censadas del sector privado y empresas paraestatales durante 2023, según definiciones de Censos Económicos 2024. No equivale al total de personas empleadas por la ENOE ni a los empleos con IMSS.

**VACB**: valor agregado censal bruto, valor creado por unidades económicas bajo definiciones censales. No equivale a nómina ni rentabilidad de firmas individuales.

**LQ manufacturero**: `(empleo manufacturero de Sonora / empleo total censal de Sonora) / (empleo manufacturero de México / empleo censal total de México)`. Con datos definitivos, aproximadamente **1.183**. **No es el Índice de Complejidad Económica (ECI)**. Un sector con LQ alto puede tener empleos variados y no implica tecnología sofisticada ni crecimiento futuro.

**Ingreso promedio OLA**: ingreso mensual del grupo de profesionistas ocupados en México. La tabla no contiene un salario inicial de un mecatrónico en Hermosillo.

**Salario mediano BLS**: mediana ocupacional nacional de EE. UU. en mayo de 2025. Las proyecciones 2025–2035 son de empleo por ocupación en EE. UU., no de necesidades de Sonora.

**Codificación de vacantes**: habilidades extraídas de requisitos textuales de anuncios. Es deliberadamente una pequeña muestra didáctica, no un muestreo representativo ni un índice de contrataciones. Algunas herramientas pueden ser **preferidas**, no obligatorias: hay que leer el enlace de origen.

**Machine learning**: vector binario habilidad–vacante y K-Means con tres grupos; el modelo reconoce patrones de codificación en 13 anuncios y PCA los visualiza. No contiene etiquetas de contratación, ni sueldos ni series históricas para predecir.

## Preguntas para discusión crítica

1. ¿Por qué una región con mucha manufactura no necesariamente es líder en producción de obleas de semiconductores?
2. Si el 30.4 % de personal ocupado censal de Sonora trabaja en manufacturas y el porcentaje nacional es 25.7 %, ¿qué significa **LQ > 1**? ¿Qué NO significa?
3. Si un anuncio exige 5–7 años de SAP, ¿podría un estudiante recién egresado considerarlo una vacante de entrada? ¿Cómo lo utilizaría como mapa de habilidades sin fingir que ya cumple el requisito?
4. ¿En qué se parecen los perfiles de Automatización, Planeación, Calidad y Compras? ¿Qué revela y qué no revela un grupo de K-Means?
5. ¿Qué sesgo existe al usar 12 vacantes de TE y una de Ford? ¿Qué cambia si agregas otros empleadores y ciudades?
6. ¿Qué hace falta investigar para concluir que semiconductores es una especialización conveniente para determinada persona? Incluye intereses, recursos, universidades, idioma, visados, empleos concretos y movilidad.

## Instrucción de extensión con IA (después de clase)

> Actúa como analista de datos laborales. Quiero estudiar la trayectoria de [CARRERA] en [REGIÓN] con egreso en [AÑO]. Trabaja **solo con datos y fuentes que te proporcione** para las cifras, y separa hechos, proyecciones oficiales, hipótesis y vacíos de información. No inventes salarios, número de vacantes, crecimiento de empleos ni disponibilidad de programas. Identifica conjuntos de datos públicos de INEGI, OLA/STPS, IMCO, Data México, CONAPO y BLS con enlaces oficiales y período. Indica cómo extraerlos legalmente a CSV con columnas compatibles y cómo comprobar población, unidades, temporalidad y sesgos antes de combinarlos. Propón una hipótesis profesional y tres experimentos de aprendizaje, no una “carrera ganadora”.

## Transferencia al segundo ejercicio

El estudiante llevaría al portafolio web **una conclusión firmada y verificable**: «Estoy orientando mi formación hacia [área] porque [datos + experiencia personal], y durante [periodo] desarrollaré [evidencia]». El perfil ficticio sirve para demostrar la mecánica, mientras que en el segundo ejercicio cada quien decide su narrativa profesional propia.

## Bibliografía de fuentes principales

- INEGI Sonora, [Censos Económicos 2024 resultados definitivos](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf).
- INEGI México, [Censos Económicos 2024 resultados definitivos](https://www.inegi.org.mx/programas/ce/2024/default.html).
- CONAPO/COESPO, [Proyecciones de Sonora 2025–2040](https://coespo.sonora.gob.mx/images/documentos/Proyecciones2020-2070/Proyecciones2025-2040-Estatal.pdf).
- STPS/INEGI, [Observatorio Laboral Ingenierías](https://www.observatoriolaboral.gob.mx/static/estudios-publicaciones/Ingenierias.html).
- IMCO, [Metodología Compara Carreras 2026](https://comparacarreras.imco.org.mx/metodologia/).
- Secretaría de Economía, [Data México: complejidad económica](https://www.economia.gob.mx/datamexico/es/eci/explore).
- Departamento de Trabajo estadounidense, [BLS Occupational Outlook Handbook](https://www.bls.gov/ooh/).
- TE Connectivity, [Carreras profesionales](https://careers.te.com/).
- Ford, [Carreras profesionales México](https://www.careers.ford.com/en/mexico).
- Universidad de Sonora, [IoT e IA](https://iotai.unison.mx/) y [Sistemas y Tecnología](https://mist.unison.mx/).
- University of Arizona, [Semiconductor Science and Technology](https://physics.arizona.edu/graduate-studies/master-science-physics-semiconductor-science-and-technology-emphasis).
