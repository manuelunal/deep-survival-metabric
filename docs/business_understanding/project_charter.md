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

## Metodología

El proyecto seguirá una **metodología experimental de aprendizaje supervisado**, organizada en cinco fases que permiten desarrollar y comparar modelos de análisis de supervivencia utilizando la cohorte METABRIC.

1. **Comprensión del problema:** definir el objetivo de predicción de supervivencia en pacientes con cáncer de mama, identificando las variables clínicas y moleculares, el tiempo de seguimiento y el evento de interés (fallecimiento).

2. **Exploración y preparación de datos:** realizar un análisis exploratorio mediante estadísticas descriptivas, curvas de Kaplan-Meier y pruebas log-rank. Posteriormente, tratar los valores faltantes, seleccionar variables, codificar categorías y estandarizar los predictores, conservando la información de las observaciones censuradas.

3. **Partición del conjunto de datos:** utilizar una estrategia *hold-out* estratificada por el indicador de evento, distribuyendo los datos en **70 % para entrenamiento, 15 % para validación y 15 % para prueba**. Las transformaciones se ajustarán exclusivamente con el conjunto de entrenamiento para evitar fuga de información.

4. **Implementación y entrenamiento:** desarrollar tres modelos mediante Python y TensorFlow/Keras: **Cox**, como referencia estadística; **DeepSurv**, para capturar relaciones no lineales; y **DeepHit**, para modelar la distribución temporal del evento. Se emplearán regularización y técnicas de parada temprana (*early stopping*) para controlar el sobreajuste.

5. **Evaluación y comparación:** evaluar los modelos utilizando el **índice de concordancia (C-index)** y el **Integrated Brier Score (IBS)**, considerando adecuadamente las observaciones censuradas. Se compararán sus resultados sobre el mismo conjunto de prueba para determinar si los modelos de aprendizaje profundo presentan mejoras frente a Cox.

Finalmente, se documentarán los resultados, las limitaciones metodológicas y las conclusiones, garantizando la reproducibilidad del experimento mediante notebooks y control de versiones en GitHub.

## Cronograma

El proyecto se desarrollará mediante **cuatro entregas semanales**, programadas para los jueves, entre el **26 de noviembre y el 17 de diciembre de 2026**. Las actividades seguirán una secuencia de comprensión del problema, preparación de datos, modelamiento y evaluación, utilizando la metodología definida anteriormente.

| Etapa | Duración estimada | Fecha de entrega | Entregable |
|---|---|---|---|
| **1. Entendimiento del negocio y planificación** | Hito inicial | 26 de noviembre de 2026 | Project Charter: objetivo, alcance, metodología, cronograma y organización del proyecto en GitHub. |
| **2. Exploración y preprocesamiento de datos** | 1 semana | 3 de diciembre de 2026 | Análisis exploratorio de METABRIC, estudio de censura, Kaplan-Meier, log-rank, tratamiento de valores faltantes y preparación de datos. |
| **3. Modelamiento e implementación experimental** | 1 semana | 10 de diciembre de 2026 | Implementación y entrenamiento de Cox, DeepSurv y DeepHit, incluyendo las arquitecturas, funciones de pérdida y estrategias de validación. |
| **4. Evaluación, documentación y entrega final** | 1 semana | 17 de diciembre de 2026 | Comparación mediante C-index e IBS, análisis de curvas de supervivencia, conclusiones, limitaciones y consolidación del repositorio. |

**Consideraciones:**

- Las entregas se realizarán cada jueves, conforme al cronograma académico previsto.
- Las actividades de cada etapa se documentarán mediante notebooks, archivos Markdown y control de versiones en GitHub.
- El proyecto tendrá un alcance experimental y académico; no se contempla el despliegue de modelos en un entorno clínico de producción.

## Equipo del Proyecto

El proyecto será desarrollado por un equipo de tres integrantes de la **Universidad Nacional de Colombia**, bajo un esquema de trabajo colaborativo y responsabilidades compartidas.

| Integrante | Rol | Responsabilidades |
|---|---|---|
| **Juan David Bonilla Sotelo** | Investigador del proyecto | Desarrollo integral del proyecto. |
| **Sergio Alejandro Rubiano Bautista** | Investigador del proyecto | Desarrollo integral del proyecto. |
| **Manuel Esteban Amarillo Giraldo** | Investigador del proyecto | Desarrollo integral del proyecto. |

### Organización del equipo

Los tres integrantes participarán conjuntamente en la planificación, exploración y preparación de datos, implementación de modelos, evaluación de resultados y documentación.

Las decisiones se tomarán de manera colaborativa, utilizando GitHub para el control de versiones y seguimiento de las contribuciones.

## Presupuesto

El presupuesto se estima para una duración de referencia de **16 semanas (4 meses)**, a ajustar según el cronograma definitivo. El proyecto se plantea como un encargo de un centro de investigación oncológica (patrocinador) a un equipo de ciencia de datos. Las tarifas por hora son valores de referencia del mercado colombiano para perfiles de analítica y salud. Todos los valores están expresados en pesos colombianos (COP).

### Talento humano

| Rol | Dedicación (horas) | Tarifa (COP/hora) | Subtotal (COP) |
|---|---:|---:|---:|
| Líder de proyecto / Scrum Master | 120 | 120.000 | 14.400.000 |
| Científico de datos senior (DeepSurv y DeepHit) | 320 | 110.000 | 35.200.000 |
| Científico de datos (preparación de datos, EDA y modelo de Cox) | 280 | 85.000 | 23.800.000 |
| Ingeniero de datos / MLOps (pipeline, versionado, reproducibilidad) | 120 | 90.000 | 10.800.000 |
| Bioestadístico (revisión metodológica de supervivencia) | 60 | 130.000 | 7.800.000 |
| Asesor clínico, oncólogo especialista en mama (interpretación de resultados) | 40 | 200.000 | 8.000.000 |
| **Subtotal talento humano** | **940** | | **100.000.000** |

### Infraestructura y tecnología

| Concepto | Supuesto | Subtotal (COP) |
|---|---|---:|
| Cómputo en la nube con GPU (entrenamiento y ajuste de hiperparámetros) | ~400 horas de instancia con GPU tipo NVIDIA T4 | 1.000.000 |
| Almacenamiento y cómputo CPU en la nube | 4 meses | 600.000 |
| Herramientas de seguimiento de experimentos y colaboración (MLflow / W&B, GitHub) | Planes académicos o de bajo costo | 800.000 |
| Conjunto de datos METABRIC | Datos públicos (sin costo de licencia) | 0 |
| **Subtotal infraestructura y tecnología** | | **2.400.000** |

### Otros costos

| Concepto | Subtotal (COP) |
|---|---:|
| Revisión del protocolo ante el Comité de Ética en Investigación | 1.100.000 |
| Taller de socialización de resultados con stakeholders | 1.500.000 |
| **Subtotal otros costos** | **2.600.000** |

### Resumen del presupuesto

| Componente | Valor (COP) |
|---|---:|
| Talento humano | 100.000.000 |
| Infraestructura y tecnología | 2.400.000 |
| Otros costos | 2.600.000 |
| **Subtotal costos directos** | **105.000.000** |
| Reserva de contingencia (10 %) | 10.500.000 |
| **Total del proyecto** | **115.500.000** |

La reserva de contingencia cubre riesgos como un mayor tiempo de ajuste de los modelos de deep learning, la necesidad de horas adicionales de GPU o reprocesos derivados de la revisión metodológica. Su uso requiere la autorización del líder del proyecto. Cualquier cambio de alcance que afecte el presupuesto se gestionará mediante solicitud de cambio aprobada por las personas de la sección de Aprobaciones.

## Stakeholders

| Stakeholder | Rol en el proyecto | Interés principal | Interés | Influencia | Estrategia de gestión |
|---|---|---|---|---|---|
| Dirección de Investigación del centro oncológico (patrocinador) | Financia el proyecto y aprueba entregables | Obtener evidencia sobre el valor del deep learning frente a Cox para futuras líneas de investigación | Alto | Alta | Gestionar de cerca: reuniones de seguimiento al cierre de cada sprint y aprobación de cambios |
| Unidad de Mastología y oncólogos clínicos | Usuarios expertos y validadores del sentido clínico de los resultados | Modelos interpretables y coherentes con el conocimiento clínico | Alto | Media | Mantener informados y consultar: revisión de variables, resultados y curvas de supervivencia |
| Comité de Ética en Investigación | Emite el aval para el uso secundario de datos de pacientes | Uso responsable de los datos y cumplimiento normativo (Ley 1581 de 2012 de protección de datos y Resolución 8430 de 1993) | Medio | Alta | Mantener satisfecho: presentar el protocolo antes de iniciar el modelado y reportar cambios relevantes |
| Equipo de ciencia de datos (Esteban Amarillo, Juan Bonilla y Sergio Rubiano) | Ejecuta el proyecto: datos, modelos, evaluación y documentación | Cumplir el alcance con calidad técnica y reproducibilidad | Alto | Media | Coordinación diaria mediante la metodología ágil definida y control de versiones en GitHub |
| Bioestadístico revisor | Asegura el rigor metodológico del análisis de supervivencia | Uso correcto de la censura, de las métricas (C-index, IBS) y de la validación | Medio | Media | Consultar en hitos clave: diseño de la validación y lectura del informe comparativo |
| Área de TI y Seguridad de la Información | Provee y controla la infraestructura y los accesos | Seguridad de los datos y costos de nube bajo control | Medio | Media | Mantener informado: acordar el entorno de nube, accesos y monitoreo de consumo |
| Docente / evaluador académico | Evalúa el proyecto como ejercicio del curso | Correcta aplicación de la metodología y calidad de los entregables | Alto | Alta | Gestionar de cerca: entregas puntuales y evidencia del trabajo en GitHub |
| Pacientes con cáncer de mama (beneficiarios indirectos) | Origen de los datos y beneficiarios futuros del conocimiento generado | Privacidad de su información y avances en la estimación del pronóstico | Medio | Baja | Monitorear: uso exclusivo de datos anonimizados y comunicación clara de que no es una herramienta clínica |

## Aprobaciones

Las partes que se relacionan a continuación aprueban el nombre, el objetivo, el alcance, la metodología, el cronograma, el equipo, el presupuesto y los stakeholders descritos en este Project Charter, y autorizan el inicio del proyecto. Cualquier modificación posterior al alcance, el cronograma o el presupuesto requerirá una solicitud de cambio aprobada por el líder del proyecto.

| Rol | Nombre |
|---|---|
| Líder del proyecto | Universidad Nacional de Colombia |
| Integrante del equipo | Esteban Amarillo |
| Integrante del equipo | Juan Bonilla |
| Integrante del equipo | Sergio Rubiano |
