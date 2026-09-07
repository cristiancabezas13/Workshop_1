# Workshop 2 · Aprendizaje supervisado

**Integrantes:** Cristian Cabezas, Mateo Lopera y Juanes Villada.

**Repositorio de entrega:** [cristiancabezas13/Workshop_1](https://github.com/cristiancabezas13/Workshop_1).

Dos notebooks en español desarrollan el ciclo de datos, pipelines, comparación de modelos, evaluación final y validación cruzada del [enunciado original](enunciado/Workshop2_ML.pdf), conservado sin modificaciones.

| Notebook | Problema | Modelos obligatorios |
|---|---|---|
| [01_regresion_vuelos.ipynb](01_regresion_vuelos.ipynb) | Predicción de `price` | Regresión lineal múltiple, KNN, árbol, Random Forest y Gradient Boosting |
| [02_clasificacion_tiroides.ipynb](02_clasificacion_tiroides.ipynb) | Recurrencia de cáncer tiroideo (`Recurred`) | KNN, árbol, Random Forest y Gradient Boosting |

Cada notebook es autocontenido: incluye descarga verificada, código, tablas, figuras, interpretaciones, referencias y correspondencia con los puntos 1–28. Las conclusiones se calculan a partir de la ejecución; no es necesario abrir primero el otro notebook. Los predictores triviales son referencias adicionales, no sustituyen ningún modelo obligatorio.

## Ejecución local

Usar Python 3.12. Desde la raíz del repositorio, entrar primero en `workshop_2/`. Después, con [uv](https://docs.astral.sh/uv/):

```powershell
uv venv --python 3.12 .venv
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
.venv/Scripts/python.exe -m ipykernel install --sys-prefix
.venv/Scripts/python.exe -m jupyterlab
```

En Linux/macOS, cambiar `.venv/Scripts/python.exe` por `.venv/bin/python`. También se puede usar `python -m venv .venv` y el `python -m pip install -r requirements.txt` de ese entorno.

Para ejecutar ambos desde un kernel limpio y guardar sus salidas:

```powershell
.venv/Scripts/python.exe ejecutar_notebooks.py
```

También se pueden ejecutar ambos desde la raíz del repositorio, usando el entorno creado en `workshop_2/`:

```powershell
workshop_2/.venv/Scripts/python.exe workshop_2/ejecutar_notebooks.py
```

Para ejecutar solamente uno:

```powershell
.venv/Scripts/python.exe ejecutar_notebooks.py 02_clasificacion_tiroides.ipynb
```

El ejecutor utiliza el mismo Python que lo invoca y detiene la ejecución ante un error. Las dependencias científicas y herramientas directas están fijadas en [requirements.txt](requirements.txt). El notebook muestra las versiones utilizadas. La regresión usa las 300.153 observaciones: KNN, Random Forest y la validación cruzada pueden requerir varios minutos; no se sustituyen las métricas por resultados de una muestra.

## Ejecución en Colab

1. Abrir uno de los siguientes enlaces de Colab, o subir el archivo `.ipynb` mediante **Archivo → Subir notebook**.
2. Usar un entorno Python de CPU; no se requiere GPU. Ejecutar la primera celda antes de importar las bibliotecas. Si instala versiones nuevas, se detiene con **REINICIO NECESARIO**: elegir **Entorno de ejecución → Reiniciar la sesión** y después **Ejecutar todo**. Repetir únicamente la primera celda no sustituye el reinicio. La tabla siguiente comprueba que las versiones instaladas y las cargadas en memoria coincidan con las del taller.
3. Ejecutar todas las celdas en orden. Si falta el CSV, el notebook descarga la versión fijada de Kaggle y comprueba su SHA-256. No requiere montar Drive ni rutas del equipo del autor.
4. Descargar el notebook con las salidas y, si se desean, los archivos de `reportes/` y `figuras/` antes de cerrar la sesión.

| Notebook | Abrir en Colab |
|---|---|
| Regresión de vuelos | [![Regresión en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cristiancabezas13/Workshop_1/blob/main/workshop_2/01_regresion_vuelos.ipynb) |
| Clasificación de recurrencia | [![Clasificación en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cristiancabezas13/Workshop_1/blob/main/workshop_2/02_clasificacion_tiroides.ipynb) |

## Datos y trazabilidad

| Archivo | Fuente | Versión | Dimensión original |
|---|---|---:|---:|
| `Clean_Dataset.csv` | [Flight Price Prediction](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) | 2 | 300.153 × 12 |
| `Thyroid_Diff.csv` | [Thyroid Disease Data](https://www.kaggle.com/datasets/jainaru/thyroid-disease-data/data) | 1 | 383 × 17 |

[data/fuentes.json](data/fuentes.json) registra las URLs de descarga, versiones, fecha y huellas originales. Los CSV y el entorno virtual se excluyen de Git: se reconstruyen mediante la descarga de los notebooks. Se lee únicamente el miembro CSV esperado del ZIP. Un archivo con huella diferente produce un error explícito, para evitar comparar datos distintos silenciosamente.

La documentación original de tiroides es [Differentiated Thyroid Cancer Recurrence, UCI](https://archive.ics.uci.edu/dataset/915/differentiated+thyroid+cancer+recurrence), de Borzooei y Tarokhian (2023), DOI [10.24432/C5632J](https://doi.org/10.24432/C5632J). Su ficha identifica pacientes y recurrencia; el nombre del dataset de Kaggle no debe confundirse con diagnóstico inicial. Los precios se reportan en unidades monetarias del dataset, porque las fuentes inspeccionadas no especifican inequívocamente la moneda.

## Adaptación del enunciado al dataset

Se mantienen los dos datasets indicados en el taller y el PDF original. Las adaptaciones se documentan en la solución y en las listas de los puntos 1–28; no se presentan como modificaciones del enunciado aprobadas por el profesor.

**Clasificación médica.** El dataset de tiroides contiene pacientes que ya tuvieron cáncer tiroideo diferenciado. Por eso se formula la tarea como clasificación de recurrencia (`Recurred`, `Yes=1`). El modelo estima si se registró recurrencia a partir de los predictores disponibles; los datos no permiten formular un diagnóstico inicial de enfermedad tiroidea.

**Dos variables para el análisis IQR.** `Age` es la única medición numérica original. Para desarrollar el requisito de dos columnas numéricas se incorpora al EDA el conteo cuantitativo discreto `n_antecedentes_afirmativos`:

```text
n_antecedentes_afirmativos = 1 si Hx Smoking = Yes
                          + 1 si Hx Radiothreapy = Yes
```

El conteo toma valores `0`, `1` o `2` y representa cuántos de esos dos campos tienen una respuesta afirmativa. Se valida que las etiquetas sean conocidas y estén presentes; un dato desconocido o ausente no se convierte en una respuesta negativa. Se incluye su definición, frecuencias y estadísticas en el notebook. Es una variable derivada, no una segunda medición original ni un puntaje clínico, y se utiliza **solo en el EDA**: sus componentes ya están representados entre los predictores de los modelos.

El IQR se calcula exclusivamente sobre las 261 observaciones de entrenamiento. `Age` no presenta valores señalados. El conteo presenta frecuencias de 239, 19 y 3 para los valores 0, 1 y 2; tiene `Q1 = Q3 = IQR = 0`, por lo que la regla señala los 22 registros con conteo positivo. Se conservan todos: son valores válidos y el resultado muestra la limitación del criterio IQR en una variable discreta concentrada en cero. La dispersión compara edad y conteo; el desplazamiento visual de los puntos se identifica para evitar interpretarlo como datos nuevos.

Esta adaptación desarrolla el requisito de IQR en dos variables numéricas y conserva el objetivo de clasificación médica que sí permite la fuente. La limitación de disponer de una sola medición numérica original queda explícita.

## Decisiones para interpretar correctamente el trabajo

- Se excluye `Response` porque describe respuesta al tratamiento. No hay fechas individuales para asegurar cuándo se midieron todas las variables; esta incertidumbre limita la interpretación prospectiva.
- Se eliminan 19 duplicados completos conforme al taller. Como no hay identificador de paciente, igualdad de perfiles no prueba identidad de personas. Después de retirar `Response`, se agrupan perfiles iguales para mantenerlos en una misma partición, incluso cuando sus etiquetas difieren.
- **Vuelos:** se excluyen el índice y `flight`, justificando la cardinalidad del código. No se eliminan observaciones solo por compartir predictores: diferentes precios pueden ser legítimos. La partición aleatoria estima desempeño dentro del mismo contexto de observación, no garantiza generalización temporal ni a rutas nuevas.
- El EDA que guía el modelado se hace sobre entrenamiento. Las transformaciones se ajustan dentro de pipelines y dentro de cada fold. La selección se cierra con validación y luego se evalúan todos los modelos en test, sin volver a seleccionarlos a partir de test.
- La validación cruzada usa solo entrenamiento y el pipeline completo del ganador. Es un análisis de estabilidad del modelo elegido, no una validación anidada de todo el proceso de selección.

## Resultados de la ejecución incluida

| Problema | Selección en validación | Resultado de test | CV de cinco folds sobre train |
|---|---|---|---|
| Vuelos | Random Forest | MAE 1,097.86 u.m.; R² 0.9849 | MAE 1,126.25 ± 11.03 u.m. |
| Recurrencia tiroidea | Gradient Boosting | Recall 0.800; Precision 0.923; F1 0.857 | Recall 0.771 ± 0.089 |

El clasificador elegido produjo 3 falsos negativos y 1 falso positivo en 51 observaciones de test. Random Forest tuvo mayor Recall en test; se conserva el ganador elegido previamente en validación. Las tablas completas y predicciones están en `reportes/`, y las figuras también están incorporadas en los notebooks. La comparación final de ambos problemas aparece en cada notebook.

## Verificación realizada

Ambos notebooks se ejecutaron completos desde kernels limpios en Windows con Python 3.12.14, sin errores. El entrenamiento y las métricas de regresión usan todos los registros. La ejecución final regeneró las tablas y figuras en la nueva estructura del repositorio. Se revisaron visualmente las 14 figuras y se contrastaron 78 valores de métricas mediante fórmulas independientes, además de sus medias y desviaciones de CV.

Se comprobó también la descarga, verificación de huella y preparación inicial desde carpetas vacías ajenas al repositorio para los dos notebooks. **La ejecución se verificó localmente; no se abrió una sesión remota de Colab.** La instalación científica y las rutas de Colab están incluidas, y el arranque autónomo fue comprobado sin depender de rutas locales del autor.

Evidencias: [entorno local](reportes/entorno_local.json), [validación independiente de regresión](reportes/regresion_validacion_independiente.json), [validación independiente de clasificación](reportes/clasificacion_validacion_independiente.json) y [verificación de la reorganización y portabilidad](reportes/verificacion_reorganizacion.json).

## Sustentación y entrega

Revisar los apartados de sustentación y las listas de los puntos 1–28 al final de los notebooks. Cada integrante debe poder explicar el target, las exclusiones, los tres conjuntos, la diferencia entre `fit` y `transform`, el costo de falsos negativos, la brecha train/validación y la variabilidad entre folds.

La entrega contiene los dos notebooks con sus salidas, este README, el enunciado original, las dependencias y los archivos de trazabilidad y resultados. El [índice principal](../README.md) permite acceder a ambos talleres. Para entregar el Workshop 2 en la plataforma académica, usar el [enlace a esta carpeta](https://github.com/cristiancabezas13/Workshop_1/tree/main/workshop_2).
