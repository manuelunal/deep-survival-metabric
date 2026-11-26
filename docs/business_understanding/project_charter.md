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
