# Career Intelligence Sonora 2026 · notebook exportado a .py

# Este script usa carpeta datos/ presente en directorio de trabajo.

# %% [markdown]
# # Career Intelligence Sonora 2026
# ## ¿Hacia dónde debe apuntar mi carrera? · Caso inicial: Ingeniería Mecatrónica
#
# **Laboratorio de 75–90 minutos.** Sin APIs: se leen 15 CSV preparados previamente, con fuentes oficiales o anuncios originales y fechas.
#
# **Caso didáctico:** Mateo Duarte Armenta, 21 años, Mecatrónica, universidad **ficticia** de Hermosillo. Las decisiones de Alex son hipótesis, no recomendaciones universales.
#
# **Resultados**: gráficos interactivos, un cociente de localización industrial (LQ), mercado laboral nacional, contraste con EE. UU., mapa de geografía económica, matriz de brechas, agrupación ML no supervisada de puestos, y una ruta de formación a validar.
#
# > **AVISO METODOLÓGICO:** Nunca mezcles salarios de México con ingresos de EE. UU. como si fueran directamente comparables. El censo reporta remuneraciones anuales por actividad y el Observatorio Laboral ingresos mensuales por formación, no salarios iniciales. **Un LQ no es el ECI** (Índice de Complejidad Económica). Las vacantes son una muestra intencional, predominantemente de TE Connectivity; no estiman demanda regional, empleabilidad ni pronostican salarios.
#
# **Fuentes principales:** [INEGI Sonora definitivos](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf) · [CONAPO/COESPO](https://coespo.sonora.gob.mx/images/documentos/Proyecciones2020-2070/Proyecciones2025-2040-Estatal.pdf) · [Observatorio Laboral](https://www.observatoriolaboral.gob.mx/static/estudios-publicaciones/Ingenierias.html) · [BLS](https://www.bls.gov/ooh/) · [IMCO metodología](https://comparacarreras.imco.org.mx/metodologia/) · [Data México complejidad](https://www.economia.gob.mx/datamexico/es/eci/explore).
# %%
# CELDA 1 · IMPORTAR 15 CSV DESDE UN SOLO ZIP, SIN LLAMADAS A APIs
from pathlib import Path
import zipfile, io, json, csv
import pandas as pd
import numpy as np
import plotly.express as px
from IPython.display import display, Markdown

RAIZ = Path('/content') if Path('/content').exists() else Path.cwd()
DATOS = RAIZ / 'datos'
if not DATOS.exists() or not list(DATOS.glob('*.csv')):
    try:
        from google.colab import files
        print('Selecciona CSV_Career_Intelligence_Sonora_2026.zip (un solo archivo).')
        subidos = files.upload()
        candidatos = [v for n,v in subidos.items() if n.lower().endswith('.zip')]
        if not candidatos:
            raise ValueError('Debes subir el ZIP de los CSV, no los CSV individualmente.')
        with zipfile.ZipFile(io.BytesIO(candidatos[0])) as z:
            for info in z.infolist():
                destino = (RAIZ / info.filename).resolve()
                if not destino.is_relative_to(RAIZ.resolve()):
                    raise ValueError('ZIP contiene ruta insegura')
            z.extractall(RAIZ)
    except ImportError:
        raise FileNotFoundError('Ejecutando fuera de Colab: descomprime ZIP aquí, con carpeta datos/ junto al notebook.')
assert DATOS.exists(), 'No se encontró la carpeta datos/'

def csv_de(nombre):
    ruta=DATOS/nombre
    if not ruta.exists(): raise FileNotFoundError(f'Falta: {ruta}')
    return pd.read_csv(ruta, encoding='utf-8-sig', keep_default_na=False)

archivos={p.stem:csv_de(p.name) for p in sorted(DATOS.glob('*.csv'))}
print(f'{len(archivos)} CSV cargados. Sin APIs ni scraping en vivo.')
display(pd.DataFrame([{'archivo':k+'.csv','filas':len(v),'columnas':len(v.columns)} for k,v in archivos.items()]))
# %% [markdown]
# ### Configuración: experimenta cambiando **solo estas variables**
#
# Esta sección **no simula que un estudiante real ya conoce las habilidades de un profesional**: representa el perfil ficticio creado para la práctica. Puedes modificarlo y volver a ejecutar las celdas de diagnóstico.
# %%
# CELDA 2 · CONFIGURACIÓN EDITABLE POR EL ESTUDIANTE
CARRERA = 'Mecatrónica'  # Prueba: 'Mecánica', 'Software', 'Industrial', 'Electrónica', 'Datos', 'Administración', 'Arquitectura'
EDAD = 21
ANIO_EGRESO = 2027
HABILIDADES_ACTUALES = ['excel', 'sensores', 'python', 'ingles']  # Ficticias: cámbialas por evidencias REALES

carreras = csv_de('09_carreras_habilidades_orientativas.csv')
assert CARRERA in carreras['carrera'].tolist(), f'Carrera no incluida. Elige: {carreras.carrera.tolist()}'
print(f'Analizando: {CARRERA} | edad {EDAD} | egreso {ANIO_EGRESO}')
print('Habilidades declaradas para el ejercicio:', ', '.join(HABILIDADES_ACTUALES))
print('NOTA: no hay inferencia estadística de “la mejor carrera”.')
# %% [markdown]
# ## Bloque A · Geografía económica de Sonora y teoría de complejidad
#
# El **cociente de localización (LQ)** compara la concentración de empleo de un sector en Sonora respecto del promedio nacional:
#
# \[
# LQ = # rac{\mathrm{empleo\ manufacturero\ Sonora}/\mathrm{empleo\ total\ Sonora}}{\mathrm{empleo\ manufacturero\ México}/\mathrm{empleo\ total\ México}}
# \]
#
# Interpretación: LQ mayor que 1 indica especialización relativa en *ese sector*. **NO** mide sofisticación productiva, salarios, competitividad, ni el índice ECI. El ECI real usa una matriz mucho más detallada de territorios y actividades, diversidad/ubicuidad e información de otros territorios.
#
# Fuente: [INEGI Censos Económicos 2024 definitivos, Sonora](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf), [México](https://www.inegi.org.mx/programas/ce/2024/default.html), [Data México, explicación del ECI](https://www.economia.gob.mx/datamexico/es/eci/explore).
# %%
# CELDA 3 · ESTRUCTURA Y ESPECIALIZACIÓN MANUFACTURERA
estr = csv_de('02_estructura_productiva_inegi.csv')
piv = estr.pivot(index='geografia',columns='sector',values='personal_ocupado')
piv['total'] = piv.sum(axis=1)
piv['proporcion_manufactura'] = piv['Manufacturas']/piv['total']
lq = float(piv.loc['Sonora','proporcion_manufactura']/piv.loc['México','proporcion_manufactura'])
print(f'Participación manufactura Sonora: {100*piv.loc["Sonora","proporcion_manufactura"]:.1f}%')
print(f'Participación manufactura México: {100*piv.loc["México","proporcion_manufactura"]:.1f}%')
print(f'LQ manufacturero de Sonora: {lq:.3f} (referencia 1.000)')
print('Interpretación: especialización relativa del EMPLEO, no complejidad tecnológica ni promesa de vacantes.')
fig=px.bar(estr, x='geografia', y='personal_ocupado',color='sector', barmode='stack',
  title='Personal ocupado en el sector privado y paraestatales (2023) — escalas diferentes',
  hover_data=['fuente'], labels={'personal_ocupado':'Personas ocupadas','geografia':'Territorio'})
fig.update_layout(height=450)
fig.show()

sub = csv_de('14_subsectores_manufactura_sonora.csv')
long = sub.melt(id_vars='subsector',value_vars=['participacion_vacb_manufacturas_2018_pct','participacion_vacb_manufacturas_2023_pct'],var_name='periodo',value_name='porcentaje')
fig=px.bar(long,x='subsector',y='porcentaje',color='periodo',barmode='group',
  title='Subsectores manufactureros seleccionados: participación en valor agregado de manufactura',
  labels={'porcentaje':'% del VACB manufacturero'})
fig.update_layout(height=440);fig.show()
# %% [markdown]
# ## Bloque B · ¿Qué tan diversa es la economía sonorense?
#
# Miremos **empleo, valor agregado y remuneración**, pero cada indicador tiene distinto denominador. Una mina puede tener poca participación en el empleo y mucho valor agregado. El censo **no describe cuántos ingenieros mecatrónicos contrata cada sector**.
#
# Las remuneraciones anuales por trabajador remunerado **no se convierten a “sueldo mensual de ingeniero”**. [Fuente INEGI](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf).
# %%
# CELDA 4 · SONORA: EMPLEO Y VALOR AGREGADO, SIN CONFUNDIRLOS
sec=csv_de('03_sectores_sonora_detalle_inegi.csv')
sec=sec.sort_values('personal_ocupado',ascending=False)
fig=px.bar(sec.head(12), x='personal_ocupado',y='sector',orientation='h',
   title='Sonora 2023: personal ocupado de sectores seleccionados (censo definitivo)',
   hover_data=['valor_agregado_millones_mxn','fuente'], labels={'personal_ocupado':'Personas ocupadas'})
fig.update_layout(yaxis={'categoryorder':'total ascending'},height=620);fig.show()
fig=px.scatter(sec, x='personal_ocupado',y='valor_agregado_millones_mxn',text='sector',
   size='unidades_economicas',hover_data=['fuente'],
   title='Sonora: empleo vs. valor agregado (NO equivale a sueldo ni productividad individual)',
   labels={'personal_ocupado':'Personal ocupado','valor_agregado_millones_mxn':'Valor agregado, millones MXN'})
fig.update_traces(textposition='top center');fig.update_layout(height=570);fig.show()
rem=csv_de('04_remuneraciones_por_actividad_inegi.csv')
fig=px.bar(rem,x='actividad',y='remuneracion_media_anual_pesos',
   title='Remuneración anual por trabajador remunerado, sector 2023 (NO sueldo de ingeniería)',
   labels={'remuneracion_media_anual_pesos':'Pesos por año'})
fig.update_layout(height=430);fig.show()
# %% [markdown]
# ## Bloque C · Proyección poblacional y mercado laboral
#
# Las proyecciones de CONAPO en esta serie específica de COESPO **no son observaciones** ni predicen vacantes. Las cifras dependen de los supuestos de cada edición; no combinarlas con otras series demográficas de distinta versión. [CONAPO/COESPO](https://coespo.sonora.gob.mx/images/documentos/Proyecciones2020-2070/Proyecciones2025-2040-Estatal.pdf).
# %%
# CELDA 5 · DEMOGRAFÍA PROYECTADA
pob=csv_de('01_demografia_conapo_sonora.csv')
ll=pob.melt(id_vars='anio',value_vars=['poblacion_0_14','poblacion_15_64','poblacion_65_mas'],var_name='grupo',value_name='personas')
fig=px.bar(ll,x='anio',y='personas',color='grupo',barmode='stack',
 title='Proyecciones CONAPO/COESPO por edad — Sonora, 2025–2040',
 labels={'personas':'Personas proyectadas'})
fig.update_layout(height=450);fig.show()
print('Dato para discusión:',pob[['anio','poblacion_estimada','edad_mediana']].to_string(index=False))
# %% [markdown]
# ## Bloque D · Salarios: México y EE. UU. **no son la misma muestra**
#
# 1. **Observatorio Laboral:** ingreso promedio mensual de profesionistas ocupados en México (campo de formación agregado, **no salario inicial**).
# 2. **BLS:** salario mediano anual ocupacional en **Estados Unidos** (mayo de 2025), más una proyección de empleo 2025–2035 para ese país. No mezclar países ni pesos/dólares en el mismo ranking. No traducir automáticamente el salario estadounidense a lo que ganaría un recién egresado mexicano.
# 3. La ocupación BLS **mechatronics technologists and technicians** **no es** lo mismo que un *ingeniero* mecatrónico: distinguir niveles y requisitos.
#
# Fuentes: [OLA](https://www.observatoriolaboral.gob.mx/static/estudios-publicaciones/Ingenierias.html) · [BLS](https://www.bls.gov/ooh/).
# %%
# CELDA 6 · INGRESOS MÉXICO (OLA) — SIN SUELDOS INVENTADOS PARA MECATRÓNICA
mx=csv_de('05_salarios_campos_mx_ola.csv').sort_values('ingreso_mensual_promedio_mxn')
fig=px.bar(mx,x='ingreso_mensual_promedio_mxn',y='campo_profesional',orientation='h',
 title='Ingreso mensual promedio de grupos de ingeniería — México nacional (2026-T2)',
 hover_data=['profesionistas_ocupados','fuente'],
 labels={'ingreso_mensual_promedio_mxn':'MXN/mes (promedio del campo, NO sueldo inicial)'})
fig.update_layout(height=560);fig.show()
print('Mecatrónica: NO hay una cifra específica en esta tabla; puede estar distribuida entre varios campos.')
# %%
# CELDA 7 · ESTADOS UNIDOS: SALARIO ANUAL MEDIANO VS PROYECCIÓN DE EMPLEO
us=csv_de('06_ocupaciones_eeuu_bls.csv')
fig=px.scatter(us,x='salario_mediano_anual_usd_2025',y='crecimiento_empleo_pct_2025_2035',
 text='traduccion_aproximada',hover_data=['ocupacion_eeuu','codigo_soc','proyeccion_aplica_a','fuente'],
 title='EE. UU. BLS: ingreso anual mediano 2025 y crecimiento proyectado 2025–2035',
 labels={'salario_mediano_anual_usd_2025':'USD/año mediano (EE. UU.)','crecimiento_empleo_pct_2025_2035':'Crecimiento proyectado %'})
fig.update_traces(textposition='top center');fig.update_layout(height=650);fig.show()
print('ADVERTENCIA: Datos de ocupaciones de EEUU, no salario que recibiría estudiante sonorense ni acceso garantizado a visado.')
# %% [markdown]
# ## Bloque E · ¿Dónde están las actividades económicas y algunas oportunidades verificables?
#
# El mapa muestra centros urbanos **aproximados**, no coordenadas de plantas ni ubicaciones puntuales de vacantes. Los círculos de los municipios se dimensionan por participación en valor agregado censal bruto 2023; los nodos de organizaciones solo señalan **instituciones comprobadas**, no número de plazas disponibles. La capa territorial se basa en [INEGI Sonora](https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf). Empresas y universidades de AZ provienen de [TSMC](https://www.tsmc.com/static/abouttsmcaz/index.htm), [Intel](https://www.intel.com/content/www/us/en/corporate/usa-chipmaking.html) y [University of Arizona](https://csm.arizona.edu/education-training/education-training-programs).
# %%
# CELDA 8 · MAPAS INTERACTIVOS SIN API DE GEOCODIFICACIÓN
mun=csv_de('07_municipios_inegi_mapa.csv')
fig=px.scatter_geo(mun,lat='lat_centro_aprox',lon='lon_centro_aprox',
 size='participacion_vacb_pct',color='participacion_empleo_pct',
 hover_name='municipio',hover_data=['participacion_vacb_pct','participacion_empleo_pct','fuente_estadistica'],
 title='Sonora: participación municipal en valor agregado y empleo (2023)',
 labels={'participacion_vacb_pct':'% VACB Sonora','participacion_empleo_pct':'% empleo Sonora'},
 projection='mercator')
fig.update_geos(fitbounds='locations',visible=True,showland=True,landcolor='rgb(240,242,239)')
fig.update_layout(height=560);fig.show()

nodos=csv_de('15_nodos_oportunidades_geograficas.csv')
fig=px.scatter_geo(nodos,lat='lat_centro_ciudad',lon='lon_centro_ciudad',
 color='pais',symbol='especialidad',hover_name='institucion',
 hover_data=['ciudad','region','nota','fuente'],
 title='Empresas e instituciones: Sonora–Arizona (centros de ciudad, no domicilios)',projection='mercator')
fig.update_traces(marker={'size':14})
fig.update_geos(fitbounds='locations',visible=True,showland=True,landcolor='rgb(240,242,239)')
fig.update_layout(height=570);fig.show()
# %% [markdown]
# ## Bloque F · Vacantes reales y brechas observables
#
# Esta tabla **no constituye una muestra representativa**: 12 anuncios provienen de TE Connectivity y uno de Ford. Las etiquetas de habilidad fueron codificadas manualmente a partir de sus textos; **no son una medición de demanda estatal**. El sueldo no publicado se deja vacío. Los años no especificados también.
#
# **Se busca aprender a detectar errores:** por ejemplo, un anuncio de Supply Chain Analyst III requiere **5–7 años de experiencia**, mientras que Supply Chain Support V (requisición 161954) **no especifica inglés**. Una IA no debe inventar esos campos. [TE Connectivity Careers](https://careers.te.com/) · [Ford Careers](https://www.careers.ford.com/).
# %%
# CELDA 9 · DIAGNÓSTICO DE BRECHAS: SIMILITUD DE HABILIDADES, NO PROBABILIDAD DE EMPLEO
vac=csv_de('08_vacantes_hermosillo_muestra.csv').copy()

def lista(s):
 return [x.strip() for x in str(s).split(';') if x.strip()]

def afinidad(s):
 return CARRERA in lista(s)

seleccion=vac[vac['carreras_afinidades_orientativas'].apply(afinidad)].copy()
actuales=set(HABILIDADES_ACTUALES)
seleccion['habilidades_requisito'] = seleccion['habilidades_codificadas'].apply(lambda s: set(lista(s)))
seleccion['coincidencias']=seleccion['habilidades_requisito'].apply(lambda s: sorted(s & actuales))
seleccion['brechas']=seleccion['habilidades_requisito'].apply(lambda s: sorted(s - actuales))
seleccion['cobertura_habilidades_pct']=seleccion['habilidades_requisito'].apply(lambda s: round(100*len(s & actuales)/max(1,len(s)),1))
seleccion=seleccion.sort_values('cobertura_habilidades_pct',ascending=False)
display(seleccion[['empresa','puesto','familia','experiencia_textual','ingles_publicado','coincidencias','brechas','cobertura_habilidades_pct','fuente']])
fig=px.bar(seleccion,x='cobertura_habilidades_pct',y='puesto',orientation='h',color='familia',
 title=f'Coincidencia de etiquetas de habilidades · Perfil {CARRERA} (NO empleabilidad)',
 hover_data=['experiencia_textual','fuente'])
fig.update_layout(yaxis={'categoryorder':'total ascending'},height=580);fig.show()
print('Aunque el porcentaje sea alto, NO elimina requisitos de experiencia, título, visa o entrevista.')
# %% [markdown]
# ## Bloque G · Machine Learning transparente: agrupar vacantes por habilidades
#
# Modelo: **K-Means no supervisado** sobre una matriz binaria de habilidades codificadas manualmente. Cada columna indica presencia (1) o ausencia (0) de una habilidad en el conjunto de etiquetas del anuncio.
#
# - El modelo **no predice** qué empleos existirán en 2028.
# - El resultado depende de la selección de 13 anuncios y del vocabulario empleado; está fuertemente sesgado a TE Connectivity.
# - PCA reduce la representación a dos dimensiones **solo para visualizar**: los ejes no son salarios ni oportunidades.
# - La explicación útil es observar qué habilidades aparecen juntas, no confundir agrupaciones con destinos profesionales.
# %%
# CELDA 10 · MODELO DE IA EXPLICABLE: MULTI-HOT + K-MEANS + PCA
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

mlb=MultiLabelBinarizer()
X=mlb.fit_transform(vac['habilidades_codificadas'].apply(lista))
numero_clusters=min(3,len(vac)-1)
modelo=KMeans(n_clusters=numero_clusters,random_state=42,n_init=10)
etiquetas=modelo.fit_predict(X)
vac['grupo_ml']=etiquetas.astype(str)
if 1<len(set(etiquetas))<len(vac):
 print('Silhouette (descriptiva, muestra pequeña):',round(silhouette_score(X,etiquetas),3))

xy=PCA(n_components=2,random_state=42).fit_transform(X)
vac['componente_1']=xy[:,0];vac['componente_2']=xy[:,1]
fig=px.scatter(vac,x='componente_1',y='componente_2',color='grupo_ml',symbol='familia',
 hover_name='puesto',hover_data=['empresa','habilidades_codificadas','fuente'],
 title='K-Means: similitud de habilidades declaradas en 13 anuncios — NO predicción laboral')
fig.update_layout(height=550);fig.show()
for i,centro in enumerate(modelo.cluster_centers_):
 inds=np.argsort(centro)[-5:][::-1]
 claves=[mlb.classes_[j] for j in inds if centro[j]>0]
 print(f'Grupo {i}: {len(vac[vac.grupo_ml==str(i)])} anuncios | habilidades frecuentes = {", ".join(claves)}')
print('Prueba cambiar el número de grupos y discutir por qué cambian los resultados.')
# %% [markdown]
# ## Bloque H · Cursos, especialización y decisión personal
#
# Las rutas formativas incluidas son referencias existentes, **no recomendaciones de admisión**. Compara requisitos, inglés, tiempo, costo, pertinencia y opciones locales antes de pagar. Semiconductores es una **posibilidad de especialización**, no una garantía para cualquier mecatrónico.
#
# Incluye oferta confirmada de [Universidad de Sonora](https://mist.unison.mx/) y [Maestría IoT+IA](https://iotai.unison.mx/), y rutas de [University of Arizona](https://physics.arizona.edu/graduate-studies/master-science-physics-semiconductor-science-and-technology-emphasis), además de formación técnica online.
# %%
# CELDA 11 · RUTAS DE FORMACIÓN ORIENTADAS A BRECHAS OBSERVADAS
cursos=csv_de('10_rutas_formacion_oficiales.csv').copy()
brechas=set(x for grupo in seleccion['brechas'] for x in grupo)
cursos['habilidades_cubiertas']=cursos['habilidades_relacionadas'].apply(lambda s: set(lista(s)) & brechas)
cursos['numero_de_brechas_relacionadas']=cursos['habilidades_cubiertas'].apply(len)
cursos=cursos.sort_values('numero_de_brechas_relacionadas',ascending=False)
display(cursos[['nombre','institucion','tipo','modalidad_sede','habilidades_cubiertas','nivel','limitacion','fuente']])
print('El orden solo cuenta etiquetas compartidas en este ejercicio. NO indica calidad ni retorno económico del curso.')
# %% [markdown]
# ## Bloque I · Síntesis: dato → interpretación → decisión → verificación
#
# **Entrega mínima (4–6 renglones)**: 1) un hallazgo estadístico con período y población, 2) un requisito de vacante que sí aparece en su fuente, 3) una limitación de datos, 4) una hipótesis de especialización, 5) el siguiente experimento de 30 días y 6) una fuente para verificarlo.
#
# Ejemplo razonable (no prescripción): «Sonora tiene una concentración relativa de empleo manufacturero mayor que el promedio nacional en 2023. Varios anuncios de manufactura solicitan PLC, SAP, inglés o calidad, pero la muestra está sesgada y no mide todos los puestos. Exploraré automatización industrial con un proyecto demostrable y compararé opciones de formación antes de decidir una maestría».
# %%
# CELDA 12 · EXPORTAR UN PLAN DE INVESTIGACIÓN PERSONAL Y DESCARGAR EN COLAB
fecha='2026-11-11'
seleccion_informes=seleccion.head(3)
filas=[]
filas.append(f'# Plan inicial de investigación de carrera: {CARRERA}')
filas.append(f'Caso de estudio: persona de {EDAD} años, egreso {ANIO_EGRESO}. Generado {fecha}.')
filas.append('')
filas.append(f'**LQ manufactura Sonora (2023)**: {lq:.3f}. No es índice de complejidad económica.')
filas.append('**Perfil de habilidades declaradas:** '+', '.join(HABILIDADES_ACTUALES))
filas.append('')
filas.append('## Vacantes a investigar (muestra NO representativa)')
for _,r in seleccion_informes.iterrows():
 filas.append(f'- **{r["puesto"]} — {r["empresa"]}**: brechas {", ".join(r["brechas"])}; experiencia: {r["experiencia_textual"]}. Fuente: {r["fuente"]}')
filas.append('')
filas.append('## Mi decisión (editar después de discutir)')
filas.append('- Hipótesis de especialización: [escribe tu hipótesis, no un pronóstico]')
filas.append('- Evidencia que la respalda: [cifra, fecha, territorio, URL]')
filas.append('- Un dato que la contradice o limita: [escribe aquí]')
filas.append('- Acción realizable en 30 días: [proyecto, conversación profesional, curso introductorio]')
filas.append('')
filas.append('## Fuentes base')
filas.append('- INEGI Sonora: https://www.inegi.org.mx/contenidos/programas/ce/2024/doc/mson_ce24.pdf')
filas.append('- OLA: https://www.observatoriolaboral.gob.mx/static/estudios-publicaciones/Ingenierias.html')
filas.append('- BLS: https://www.bls.gov/ooh/')
filas.append('- Complejidad económica: https://www.economia.gob.mx/datamexico/es/eci/explore')
ruta=RAIZ/f'plan_carrera_{CARRERA.lower().replace(" ","_")}.md'
ruta.write_text('\n'.join(filas),encoding='utf-8')
print('Archivo generado:',ruta)
try:
 from google.colab import files
 files.download(str(ruta))
except ImportError:
 print('En entorno local el archivo se guardó en disco.')
# %% [markdown]
# ## Para profundizar después del taller
#
# - **Complejidad económica real:** el ECI/PCI requiere matriz de actividades y comparadores regionales; explora [Data México](https://www.economia.gob.mx/datamexico/es/eci/explore). Nuestro notebook calcula únicamente LQ manufacturero.
# - **Ampliar datos:** sustituye la muestra intencional de vacantes por anuncios de múltiples empleadores, con criterios de muestreo, fechas y vacantes cerradas. No clasifiques seniority por número romano en el título.
# - **Comparar salarios correctamente:** no presentes un salario nacional de profesionistas como salario inicial de Hermosillo; no conviertas medianas de EE. UU. a MXN sin tratar experiencia, impuestos, costo de vida, permisos laborales y salarios por ubicación.
# - **Cuidado con inferencias:** que haya inversión en semiconductores en Arizona no equivale a que Sonora tenga fábricas de obleas ni que todos los estudiantes deban especializarse en semiconductores. Investiga las cadenas productivas y sus riesgos, sin determinismo tecnológico.
#
# **Cinco preguntas de salida**: ¿qué aprendí de los datos? ¿cuál es la fuente? ¿qué afirmación no puedo hacer? ¿qué decisión revisaría? ¿cuál es mi primer experimento para aprender más?