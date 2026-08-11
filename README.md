# Workshop 1 — Análisis Exploratorio de Datos (EDA)

**Equipo:** Cristian Cabezas, Mateo Lopera, Juanes Villada

Ciclo completo de exploración de datos (reconocimiento, limpieza, análisis descriptivo y
visualización) sobre el dataset **Anime Recommendations Database** de Kaggle.

- **Notebook:** [`WORKSHOP_1.ipynb`](WORKSHOP_1.ipynb) — viene ejecutado, con todas las salidas
  y gráficas visibles directamente desde GitHub.
- **Dataset:** [CooperUnion/anime-recommendations-database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database).
  Trabajamos con `anime.csv` (12,294 animes de MyAnimeList); el otro archivo del dataset,
  `rating.csv` (~7.8 M calificaciones usuario-anime), queda anotado como trabajo futuro.

## Cómo ejecutarlo

El notebook descarga el dataset con `kagglehub`, así que no hay que subir archivos a mano:

```python
import kagglehub
path = kagglehub.dataset_download("CooperUnion/anime-recommendations-database")
```

- **En Colab:** abrir el notebook y darle *Run all*. Si `kagglehub` llegara a fallar, la celda
  de carga tiene un respaldo para subir `anime.csv` manualmente.
- **En local:** instalar las dependencias y ejecutar. Si `anime.csv` ya está al lado del
  notebook, lo usa directamente sin volver a descargar nada.

```bash
pip install pandas numpy matplotlib seaborn kagglehub jupyter
```

## Contenido

| Fase | Qué contiene |
|---|---|
| 1 | Reconocimiento: diccionario de datos, `.info()`/`.dtypes`, `.describe()` interpretado y cálculo manual con NumPy |
| 2 | Limpieza: nulos con estrategia justificada, duplicados, inconsistencias de formato y outliers por IQR |
| 3 | Exploración: `value_counts()`, diccionario sobre subconjunto filtrado, `groupby()` y ordenamientos |
| 4 | Visualización: barras, pie, histograma, scatter y dos boxplots — cada uno con interpretación y recomendación de negocio |
| 5 | Conclusiones generales y resumen visual en un `subplot(2,2)` |
