# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis de supervivencia en cáncer de mama con deep learning (METABRIC)

## Objetivo del Proyecto

El objetivo principal del proyecto es desarrollar y comparar modelos de análisis de supervivencia basados en aprendizaje profundo (DeepSurv y DeepHit) frente al modelo clásico de riesgos proporcionales de Cox, para estimar el riesgo y la probabilidad de supervivencia en el tiempo de pacientes con cáncer de mama a partir de variables clínicas y genómicas del conjunto de datos METABRIC. Se busca determinar si los modelos de deep learning, al capturar relaciones no lineales entre las variables, mejoran la capacidad de discriminación y la calibración de las predicciones respecto al modelo de Cox. El detalle de las variables utilizadas puede consultarse en el diccionario de datos anexo.

## Alcance del Proyecto

### Incluye:

- El proyecto se sustenta en el conjunto de datos METABRIC (Molecular Taxonomy of Breast Cancer International Consortium), con aproximadamente 1.900 pacientes, que contiene variables clínicas y de expresión génica, el tiempo de seguimiento en meses y un indicador de evento (fallecimiento) o censura. Los datos fueron obtenidos de [completar: pycox, Kaggle o cBioPortal].
- Al finalizar el proyecto se espera contar con un modelo base de Cox y dos modelos de deep learning (DeepSurv y DeepHit) entrenados y optimizados, junto con un informe comparativo de métricas de supervivencia: índice de concordancia (C-index), Integrated Brier Score (IBS) y curvas de supervivencia estimadas por paciente.
- El éxito del proyecto se determinará porque al menos uno de los modelos de deep learning supere al modelo de Cox en C-index e IBS sobre el conjunto de prueba, alcance un C-index superior a un umbral predefinido (por ejemplo, 0,65) y muestre resultados estables entre particiones (validación cruzada o bootstrap).

### Excluye:

- El proyecto no constituye una herramienta de diagnóstico ni de apoyo a decisiones clínicas y no reemplaza el criterio médico. Tampoco incluye validación clínica prospectiva ni validación con cohortes externas.
- El alcance se limita a la cohorte METABRIC. Quedan por fuera otros tipos de cáncer, el uso de imágenes (histopatología o mamografía), el análisis de riesgos competitivos y la inferencia causal sobre el efecto de los tratamientos.