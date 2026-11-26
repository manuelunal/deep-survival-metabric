# Análisis de supervivencia en cáncer de mama con deep learning (METABRIC)

Proyecto aplicado de la materia de Deep Learning – Universidad Nacional de Colombia.

Comparamos modelos de deep learning para análisis de supervivencia (**DeepSurv** y **DeepHit**) frente al modelo de riesgos proporcionales de **Cox**, para estimar la curva de supervivencia individual de pacientes con cáncer de mama a partir de variables clínicas, patológicas y de tratamiento del conjunto de datos METABRIC.

## Equipo

- Manuel Esteban Amarillo Giraldo
- Juan David Bonilla Sotelo
- Sergio Alejandro Rubiano Bautista

## Estado del proyecto

| Fase | Contenido | Estado |
| --- | --- | --- |
| 1. Entendimiento del negocio y carga de datos | Project charter, diccionario de datos, código de carga | En curso |
| 2. Análisis exploratorio y preprocesamiento | EDA, limpieza, codificación y partición | Pendiente |
| 3. Modelado | Cox, DeepSurv y DeepHit | Pendiente |
| 4. Evaluación | C-index, IBS, AUC dependiente del tiempo, calibración | Pendiente |

## Datos

Usamos la tabla clínica del consorcio **METABRIC** (Molecular Taxonomy of Breast Cancer International Consortium), publicada en [cBioPortal](https://www.cbioportal.org/study/summary?id=brca_metabric) y descargada desde [Kaggle](https://www.kaggle.com/datasets/gunesevitan/breast-cancer-metabric).

- 2.509 pacientes y 34 variables, en formato CSV.
- Variable objetivo: tiempo hasta el evento (`Overall Survival (Months)`) e indicador de muerte o censura (`Overall Survival Status`).
- Los datos **no se suben al repositorio**. El script de carga los descarga automáticamente en `data/raw/`.

El detalle de cada variable está en el [diccionario de datos](docs/data/data_dictionary.md).

## Cómo ejecutar

Requisitos: Python 3.9 o superior.

```bash
pip install "kagglehub[pandas-datasets]" pandas
python scripts/data_acquisition/main.py
```

El script descarga el dataset, valida su estructura, muestra un resumen y guarda el archivo en `data/raw/metabric.csv`.

## Estructura del repositorio

```
├── docs/
│   ├── business_understanding/
│   │   └── project_charter.md      # Marco del proyecto
│   ├── data/
│   │   └── data_dictionary.md      # Diccionario de datos
│   ├── modeling/
│   ├── deployment/
│   └── acceptance/
├── scripts/
│   ├── data_acquisition/
│   │   └── main.py                 # Descarga y validación de los datos
│   ├── eda/
│   ├── preprocessing/
│   ├── training/
│   └── evaluation/
├── .gitignore
├── pyproject.toml
└── README.md
```

La estructura sigue la plantilla [TDSP](https://github.com/mindlab-unal/tdsp_template) del curso.

## Metodología

Seguimos TDSP (Team Data Science Process) en cinco semanas. El modelo de Cox con regularización L2 es la línea base. Lo comparamos con DeepSurv, una red neuronal entrenada con la verosimilitud parcial de Cox, y con DeepHit, un modelo de tiempo discreto que no asume riesgos proporcionales. Más detalle en el [project charter](docs/business_understanding/project_charter.md).

## Referencias

- Curtis, C. et al. (2012). The genomic and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups. *Nature*, 486, 346–352.
- Pereira, B. et al. (2016). The somatic mutation profiles of 2,433 breast cancers refine their genomic and transcriptomic landscapes. *Nature Communications*, 7, 11479.
- Katzman, J. L. et al. (2018). DeepSurv: personalized treatment recommender system using a Cox proportional hazards deep neural network. *BMC Medical Research Methodology*, 18, 24.
- Lee, C. et al. (2018). DeepHit: A deep learning approach to survival analysis with competing risks. *AAAI Conference on Artificial Intelligence*.