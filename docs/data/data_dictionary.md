# Diccionario de datos

## Base de datos 1: METABRIC (`Breast Cancer METABRIC.csv`) 

Tabla clínica del consorcio METABRIC obtenida desde Kaggle (`gunesevitan/breast-cancer-metabric`), con información original de cBioPortal (`brca_metabric`). Cada fila corresponde a una paciente con cáncer de mama primario. Contiene 2.509 registros y 34 variables (10 numéricas y 24 categóricas). La variable objetivo es de tiempo hasta el evento y está compuesta por `Overall Survival (Months)` y `Overall Survival Status`.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Patient ID | Identificador único de la paciente | Texto | Código alfanumérico (p. ej. MB-0000) | Kaggle – METABRIC |
| Age at Diagnosis | Edad de la paciente al diagnóstico (años) | Numérico continuo | 21,93 – 96,29 | Kaggle – METABRIC |
| Type of Breast Surgery | Tipo de cirugía realizada | Categórico | Mastectomy, Breast Conserving | Kaggle – METABRIC |
| Cancer Type | Tipo general de cáncer | Categórico | Breast Cancer, Breast Sarcoma | Kaggle – METABRIC |
| Cancer Type Detailed | Tipo histológico detallado del tumor | Categórico | Breast Invasive Ductal Carcinoma, Breast Mixed Ductal and Lobular Carcinoma, Breast Invasive Lobular Carcinoma, Invasive Breast Carcinoma, Breast Invasive Mixed Mucinous Carcinoma, Breast, Breast Angiosarcoma, Metaplastic Breast Cancer | Kaggle – METABRIC |
| Cellularity | Celularidad tumoral (proporción de células tumorales en la muestra) | Categórico ordinal | Low, Moderate, High | Kaggle – METABRIC |
| Chemotherapy | Indica si la paciente recibió quimioterapia | Binario | Yes, No | Kaggle – METABRIC |
| Pam50 + Claudin-low subtype | Subtipo molecular intrínseco PAM50 + Claudin-low | Categórico | LumA, LumB, Her2, Basal, Normal, claudin-low, NC (no clasificado) | Kaggle – METABRIC |
| Cohort | Cohorte del estudio a la que pertenece la paciente | Numérico discreto | Valores enteros (1, 2, 3, …) | Kaggle – METABRIC |
| ER status measured by IHC | Receptor de estrógeno medido por inmunohistoquímica | Categórico | Positve, Negative (el valor positivo viene mal escrito en la fuente) | Kaggle – METABRIC |
| ER Status | Estado del receptor de estrógeno | Binario | Positive, Negative | Kaggle – METABRIC |
| Neoplasm Histologic Grade | Grado histológico del tumor (diferenciación celular) | Numérico ordinal | 1, 2, 3 | Kaggle – METABRIC |
| HER2 status measured by SNP6 | Estado de HER2 según número de copias (SNP6) | Categórico | GAIN, LOSS, NEUTRAL, UNDEF | Kaggle – METABRIC |
| HER2 Status | Estado del receptor HER2 | Binario | Positive, Negative | Kaggle – METABRIC |
| Tumor Other Histologic Subtype | Subtipo histológico del tumor | Categórico | Ductal/NST, Lobular, Mixed, Medullary, Mucinous, Tubular/ cribriform, Metaplastic, Other | Kaggle – METABRIC |
| Hormone Therapy | Indica si la paciente recibió hormonoterapia | Binario | Yes, No | Kaggle – METABRIC |
| Inferred Menopausal State | Estado menopáusico inferido | Binario | Pre, Post | Kaggle – METABRIC |
| Integrative Cluster | Subgrupo integrativo (IntClust) definido por Curtis et al. (2012) | Categórico | 1, 2, 3, 4ER+, 4ER-, 5, 6, 7, 8, 9, 10 | Kaggle – METABRIC |
| Primary Tumor Laterality | Lado del tumor primario | Binario | Left, Right | Kaggle – METABRIC |
| Lymph nodes examined positive | Número de ganglios linfáticos con compromiso tumoral | Numérico discreto | 0 – 45 | Kaggle – METABRIC |
| Mutation Count | Número de mutaciones detectadas en el tumor | Numérico discreto | 1 – 80 | Kaggle – METABRIC |
| Nottingham prognostic index | Índice pronóstico calculado con el tamaño, el grado y los ganglios | Numérico continuo | 1,00 – 6,36 | Kaggle – METABRIC |
| Oncotree Code | Código OncoTree del tipo de tumor | Categórico | Códigos OncoTree (p. ej. IDC, ILC, MDLC) | Kaggle – METABRIC |
| Overall Survival (Months) | Tiempo desde el diagnóstico hasta la muerte o el último seguimiento (meses). **Objetivo: tiempo** | Numérico continuo | 0 – 355,2 | Kaggle – METABRIC |
| Overall Survival Status | Estado vital al final del seguimiento. **Objetivo: evento** | Binario | Deceased (evento), Living (censura) | Kaggle – METABRIC |
| PR Status | Estado del receptor de progesterona | Binario | Positive, Negative | Kaggle – METABRIC |
| Radio Therapy | Indica si la paciente recibió radioterapia | Binario | Yes, No | Kaggle – METABRIC |
| Relapse Free Status (Months) | Tiempo libre de recaída (meses) | Numérico continuo | ≥ 0 | Kaggle – METABRIC |
| Relapse Free Status | Indica si la paciente presentó recaída | Binario | Not Recurred, Recurred | Kaggle – METABRIC |
| Sex | Sexo de la paciente | Categórico | Female | Kaggle – METABRIC |
| 3-Gene classifier subtype | Subtipo según el clasificador de tres genes | Categórico | ER+/HER2- High Prolif, ER+/HER2- Low Prolif, ER-/HER2-, HER2+ | Kaggle – METABRIC |
| Tumor Size | Tamaño del tumor (mm) | Numérico continuo | 1 – 182 | Kaggle – METABRIC |
| Tumor Stage | Estadio del tumor | Numérico ordinal | 0 – 4 | Kaggle – METABRIC |
| Patient's Vital Status | Estado vital detallado, con la causa de muerte | Categórico | Living, Died of Disease, Died of Other Causes | Kaggle – METABRIC |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

### Notas

- **Variable objetivo:** `tiempo` = `Overall Survival (Months)`; `evento` = 1 si `Overall Survival Status` es `Deceased` y 0 si es `Living` (censura). 528 pacientes no tienen información de supervivencia y se excluyen del análisis.
- **Variables que no se usan como predictores:**
  - `Patient ID`: es un identificador.
  - `Relapse Free Status`, `Relapse Free Status (Months)` y `Patient's Vital Status`: generan fuga de información.
  - `Sex`, `Cancer Type` y `Cohort`: son constantes o administrativas.
  - `Oncotree Code`, `Tumor Other Histologic Subtype`, `3-Gene classifier subtype`, `ER status measured by IHC` y `HER2 status measured by SNP6`: son redundantes.