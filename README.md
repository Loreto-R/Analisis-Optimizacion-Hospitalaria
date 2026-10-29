<h1 align="center">  ANÁLISIS PREDICTIVO PARA LA OPTIMIZACIÓN DE RECURSOS HOSPITALARIOS

<p align="center"> Proyecto de Data Analytics · Loreto Redondo y Javier Troyano





___



## 🏥DESCRIPCION GENERAL DEL PROYECTO

Este proyecto se centra en el análisis de datos hospitalarios y en el desarrollo de un modelo predictivo capaz de clasificar la duración de la estancia de un paciente en el hospital.

A través de herramientas de análisis de datos como Python y aprendizaje automático (Machine Learning), se ha realizado un análisis exploratorio de los datos (Power BI), un proceso de limpieza y transformación de la información y la creación y comparación de diferentes modelos de Machine Learning. Finalmente, se ha seleccionado el modelo con mejores resultados para desarrollar una aplicación interactiva con Streamlit que permita realizar predicciones a partir de la información de los datos registrados y poder así realizar una planificación de los recursos necesarios.



## 🎯OBJETIVO

Desarrollar un programa de predicción capaz de estimar la duración de la estancia hospitalaria de un paciente a partir de datos relacionados con su hospitalización, con el fin de contribuir a una mejor planificación y optimización de los recursos hospitalarios.


## 📊DATOS

El proyecto se basa en los datos obtenidos a través de un DATASET sintético con más de 300.000 casos registrados de pacientes en diferentes hospitales y ciudades.


## 🛠️HERRAMIENTAS

Python: lenguaje de programación utilizado para el análisis y tratamiento de los datos.

Jupyter Notebook: entorno de trabajo para desarrollar y ejecutar el código.

Pandas: biblioteca usada para la manipulación y el análisis de datos.

Machine Learning: técnicas utilizadas para entrenar y comparar modelos predictivos.

Streamlit: herramienta utilizada para desarrollar la aplicación interactiva de predicción.

Power BI: herramienta utilizada para el análisis exploratorio y la visualización de los datos.


## 🗂️FASES DEL PROYECTO

### FASE 0. Selección del conjunto de datos.

Búsqueda en la plataforma Kaggle de un Dataset adecuado a las necesidades y características del proyecto.


### FASE 1. Estudio, limpieza y preparación de los datos.

A través de gráficos, se realiza un estudio detallado para comprobar la coherencia de los datos y concluir que el estudio es viable para su posterior limpieza y transformación.


1. Optimizamos el conjunto de datos mediante procesos de limpieza y transformación, asegurando un formato óptimo para el entrenamiento de modelos predictivos.

2. Análisis de datos nulos para decidir si se transforman o se eliminan.

3. Creación de nuevas columnas.

4. Agrupaciones de datos para facilitar su análisis.

5. Eliminación de columnas que no aportan valor.

6. Hacer una copia del Dataset final con todos los cambios.


### FASE 2. Desarrollo y comparación de modelos predictivos.

En esta fase se entrenan y se comparan los 3 modelos y su AUC (área bajo la curva) para seleccionar el mejor.


### Tabla comparativa de resultados (métrica AUC)

| Modelo | Datos utilizados | Nivel de acierto general (AUC Macro) | Nivel de acierto ponderado (AUC Weighted) | ¿Cómo rinde? |
| --- | --- | --- | --- | --- |
| **XGBoost** 🥇 | Datos completos (transformados a formato numérico) | **82,2 %** (0.822) | **80,3 %** (0.803) | **El mejor de los tres** |
| **Random Forest** 🥈 | Datos completos | **79,9 %** (0.799) | **78,3 %** (0.783) | **Muy buen rendimiento** |
| **Regresión Logística** 🥉 | Datos con limpieza adicional | **66,0 %** (0.660) | **65,6 %** (0.656) | **Menor rendimiento** |

Por sus valores de AUC, se avanza con el modelo XGBoost, que se guarda en un archivo .pkl


### FASE 3. Aplicación del programa predictivo con STREAMLIT

Con el modelo elegido se desarrolla un programa que predice la estancia de un paciente en el hospital. El script app.py se estructura así:


1. Carga del modelo predictivo.

2. Imagen y cabecera del programa.

3. Formulario:

* Sección 1: variables con información del hospital.

* Sección 2: variables con información del paciente.

4. Botón de predicción:

* Creación del marco de datos con todos los inputs.

* Dummies para las columnas categóricas.

* Predicción.

* Conversión de la predicción numérica a categórica.


Con esto se cumple el objetivo: un programa predictivo funcional que nos permita estimar la duración hospitalaria del paciente y poder optimizar así los recursos necesarios para futuros ingresos.



### 📈PRESENTACIÓN DE RESULTADOS

A través de un archivo CANVA se presentan todos los materiales, las fases trabajadas y los resultados obtenidos el proyecto. Se añade también un archivo de Power BI con el análisis exploratorio realizado.

