# Workshop 1 — Análisis exploratorio de datos (EDA)

**Equipo:** Cristian Cabezas, Mateo Lopera y Juanes Villada

En este trabajo aplicamos el ciclo completo de exploración de datos sobre el conjunto de datos **Anime Recommendations Database**: reconocimiento inicial, limpieza, análisis descriptivo, visualización y conclusiones.

El entregable principal es [`WORKSHOP_1.ipynb`](WORKSHOP_1.ipynb), que se entrega ejecutado con sus tablas, cálculos, gráficos e interpretaciones.

## Conjunto de datos y alcance del análisis

Trabajamos con la [versión 1 del conjunto de datos Anime Recommendations Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database), publicado en Kaggle.

El conjunto de datos contiene dos archivos, pero para este taller usamos únicamente `anime.csv`:

- Cada fila representa una entrada de anime en el catálogo.
- El archivo original tiene **12.294 filas y 7 columnas**.
- Después de la limpieza, el conjunto analítico queda con **12.064 filas y 7 columnas**.
- `rating.csv` no forma parte de este análisis. Ese archivo podría usarse más adelante para estudiar interacciones entre usuarios y animes o construir un sistema de recomendación.

La columna `members` corresponde al conteo que la fuente reporta para la comunidad asociada con cada anime. En el análisis la usamos como una aproximación a la popularidad dentro del catálogo, pero **no equivale a visualizaciones, número de votos ni usuarios únicos**.

## Contenido del notebook

| Fase | Contenido |
|---|---|
| 1. Reconocimiento inicial | Documentación del conjunto de datos, carga y validación, `head()`, `tail()`, `.shape`, `.info()`, `.dtypes`, `.describe()` y cálculos con NumPy |
| 2. Limpieza | Revisión y tratamiento de nulos, conversión de `episodes`, normalización de texto, duplicados y detección de valores atípicos mediante IQR |
| 3. Análisis descriptivo | Categorías, conteos, diccionario sobre subconjuntos filtrados, preguntas con `groupby()` y ordenamientos |
| 4. Visualización | Barras, gráfico circular, histograma, diagrama de dispersión y diagramas de caja, acompañados de interpretación y recomendación |
| 5. Conclusiones | Síntesis de resultados, limitaciones, preguntas futuras y resumen visual en un `subplot(2,2)` |

## Principales resultados

- Excluimos **230 registros** que no tenían `rating`; dentro de ese mismo grupo estaban los 25 registros sin `type`. Las conclusiones se limitan a las 12.064 filas del conjunto analítico.
- Después de esa exclusión quedaron **188 valores faltantes en `episodes`**. Los imputamos con la mediana del tipo correspondiente: TV 24; OVA y ONA 2; Movie, Special y Music 1.
- No encontramos filas completamente duplicadas ni valores repetidos en `anime_id`. Conservamos cuatro registros asociados con dos nombres repetidos porque tienen identificadores y características distintas.
- Los cinco géneros más frecuentes —Comedy, Action, Adventure, Fantasy y Sci-Fi— reúnen **13.937 de las 35.642 asignaciones de género**, equivalentes al **39,10 %**. Un mismo título puede pertenecer a varios géneros.
- El `rating` promedio del conjunto analítico es **6,47**, con una mediana de **6,57** y una asimetría de **−0,54357**. Esto indica una distribución moderadamente sesgada hacia la izquierda.
- La correlación de Pearson entre `rating` y `members` es **0,387979** en la escala original y **0,648254** al usar `log1p(members)`. Son asociaciones descriptivas y no demuestran causalidad.
- El criterio IQR identifica **1.884 títulos atípicos en `members`**, equivalentes al **15,62 %** del conjunto analítico. Estos títulos reúnen el **85,44 % de la suma de `members`**, lo cual no debe interpretarse como porcentaje de personas únicas.
- Encontramos **33 películas de 2.297** con más de un episodio. Todos esos valores ya estaban registrados en el archivo original; la imputación por tipo no creó nuevas excepciones.

## Cómo ejecutar el notebook

### Requisitos

```bash
pip install pandas numpy matplotlib seaborn kagglehub jupyter
```

### Ejecución local

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
jupyter notebook WORKSHOP_1.ipynb
```

La celda de carga primero busca `anime.csv` en la misma carpeta del notebook. Si el archivo no está disponible, descarga únicamente ese archivo desde la versión fijada del conjunto de datos:

```python
kagglehub.dataset_download(
    "CooperUnion/anime-recommendations-database/versions/1",
    path="anime.csv"
)
```

### Ejecución en Google Colab

Abrimos el notebook en Colab y seleccionamos **Ejecutar todas**. Si la descarga no está disponible en la sesión, podemos subir `anime.csv` al directorio de trabajo y volver a ejecutar la celda de carga.

Los mensajes de error diferencian entre Colab y una ejecución local para indicar qué se debe revisar en cada entorno.

## Comprobaciones de reproducibilidad

Al ejecutar el notebook completo esperamos obtener:

- Forma original: `(12294, 7)`.
- Forma analítica: `(12064, 7)`.
- Cero valores nulos en el conjunto analítico.
- Cero filas completamente duplicadas.
- `anime_id` único.
- `episodes` como entero positivo.
- `rating` dentro del rango de 0 a 10.
- 188 episodios imputados.
- 33 películas con más de un episodio.
- 1.884 valores atípicos en `members`.
- 85,44 % de la suma de `members` reunida en esos valores atípicos.

## Limitaciones

- Las 230 filas excluidas presentan un perfil diferente en algunas variables, por lo que no asumimos que su ausencia sea completamente aleatoria.
- `members` no permite conocer cuántas personas vieron o calificaron cada anime.
- El archivo no incluye variables temporales, estudio, plataforma, presupuesto ni número de votos.
- Las diferencias observadas entre tipos y géneros son asociaciones descriptivas. Con este EDA no podemos afirmar que el tipo de anime cause un mayor `rating` o un mayor valor de `members`.
- Para un sistema de recomendación sería necesario incorporar `rating.csv` y formular un análisis distinto al desarrollado en este taller.
