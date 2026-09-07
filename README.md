# Fundamentos de Aprendizaje Automático — Workshops

Talleres de **Cristian Cabezas, Mateo Lopera y Juanes Villada**. Este repositorio reúne los notebooks ejecutados, la documentación y las evidencias necesarias para revisar y reproducir cada trabajo.

## Talleres

| Taller | Tema y datos | Entregables |
|---|---|---|
| [Workshop 1](workshop_1/README.md) | Análisis exploratorio de datos: Anime Recommendations Database | [Notebook de EDA](workshop_1/WORKSHOP_1.ipynb) |
| [Workshop 2](workshop_2/README.md) | Aprendizaje supervisado: precios de vuelos y recurrencia de cáncer tiroideo | [Regresión de vuelos](workshop_2/01_regresion_vuelos.ipynb) · [Clasificación de recurrencia](workshop_2/02_clasificacion_tiroides.ipynb) |

### Abrir en Google Colab

| Notebook | Acceso |
|---|---|
| Workshop 1 · EDA de anime | [![Abrir EDA en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cristiancabezas13/Workshop_1/blob/main/workshop_1/WORKSHOP_1.ipynb) |
| Workshop 2 · Regresión de vuelos | [![Abrir regresión en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cristiancabezas13/Workshop_1/blob/main/workshop_2/01_regresion_vuelos.ipynb) |
| Workshop 2 · Clasificación de recurrencia | [![Abrir clasificación en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cristiancabezas13/Workshop_1/blob/main/workshop_2/02_clasificacion_tiroides.ipynb) |

Cada notebook contiene sus instrucciones de instalación y carga de datos. Las salidas incluidas se pueden consultar directamente en GitHub; abrir el notebook en Colab permite volver a ejecutarlo.

## Organización

```text
workshop_1/
├── README.md                         # Datos, metodología y ejecución
└── WORKSHOP_1.ipynb                   # EDA con resultados
workshop_2/
├── README.md                         # Metodología, adaptación y resultados
├── 01_regresion_vuelos.ipynb          # Modelos de regresión
├── 02_clasificacion_tiroides.ipynb    # Modelos de clasificación
├── requirements.txt                  # Dependencias fijadas
├── ejecutar_notebooks.py             # Ejecución desde kernels limpios
├── enunciado/                        # PDF original del taller
├── data/                             # Fuentes y huellas de los datos
├── figuras/                          # Gráficos exportados
└── reportes/                         # Tablas, predicciones y verificaciones
```

## Reproducir los trabajos

Clonar el repositorio y seguir las instrucciones del taller correspondiente:

```bash
git clone https://github.com/cristiancabezas13/Workshop_1.git
cd Workshop_1
```

- **Workshop 1:** entrar en `workshop_1/`, instalar las dependencias indicadas en su [README](workshop_1/README.md) y abrir `WORKSHOP_1.ipynb`.
- **Workshop 2:** entrar en `workshop_2/` y seguir su [guía de ejecución](workshop_2/README.md#ejecución-local). Incluye un ejecutor para guardar las salidas de ambos notebooks.

Los archivos originales descargables y los entornos virtuales se excluyen de Git. Los notebooks incluyen la carga de datos y las referencias a sus fuentes. Las tablas de resultados, figuras y documentación sí forman parte de la entrega.

## Workshop 2: correspondencia con el enunciado

El [PDF original](workshop_2/enunciado/Workshop2_ML.pdf) se conserva intacto. La [documentación del Workshop 2](workshop_2/README.md#adaptación-del-enunciado-al-dataset) explica cómo se desarrollan sus requisitos con los datos enlazados: clasificación de **recurrencia** mediante `Recurred` y análisis IQR de la edad y un conteo derivado de dos antecedentes. Cada notebook contiene una lista de correspondencia con los puntos 1–28.

La carpeta `workshop_2/` contiene la versión definitiva del segundo taller. Las versiones anteriores permanecen disponibles en el historial del repositorio.
