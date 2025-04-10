

---

# 🎵 Análisis de Preferencias en Plataformas de Streaming Musical

Este repositorio contiene un análisis de las preferencias de los oyentes en plataformas de música de todo el mundo. Para la limpieza de datos se utilizó Python (Pandas) y para la generación de un dashboard interactivo se utilizó Power BI.

## 🚀 Objetivo del Proyecto
Explorar las tendencias en el streaming de música y obtener información sobre las preferencias de los oyentes según género, país y otros indicadores relevantes.

## 🛠️ Herramientas
- **Python (Pandas):** Para la limpieza y transformación de datos.
- **Power BI:** Para la visualización interactiva y el análisis de datos.

## 📊 Fuente de Datos
El conjunto de datos utilizado en este proyecto proviene de Kaggle, una plataforma líder en análisis de datos y aprendizaje automático. Puedes encontrarlo en el siguiente enlace: [Worldwide Music Streaming Trends and Insights](https://www.kaggle.com/datasets/salehahmedsaleh/worldwide-music-streaming-trends-and-insights).

### Detalles del Conjunto de Datos
El conjunto de datos contiene información sobre las tendencias de streaming musical en varios países, incluyendo géneros preferidos, duración promedio de escucha y otros datos clave.

## 📋 Metodología de Limpieza de Datos

El proceso de limpieza y transformación de datos se realizó con Python utilizando **Pandas** en combinación con **pandasql**, lo que permitió aprovechar la comodidad y familiaridad de SQL directamente en el entorno de Python. Este enfoque fue ideal para consultar y manipular el conjunto de datos de manera eficiente.

### ¿Por qué usar SQL y pandasql?
1. **Comodidad y Familiaridad:**  
   SQL es un lenguaje ampliamente utilizado para la manipulación de datos, y su integración con pandasql permitió aplicar consultas SQL sin salir del entorno de Python.

2. **Ventajas de Pandas:**  
   Aunque SQL es poderoso, la versatilidad de Pandas permitió realizar tareas avanzadas como imputaciones estadísticas y transformaciones detalladas que no son tan intuitivas en SQL puro.

3. **Flujo de Trabajo Eficiente:**  
   La combinación de estas herramientas ofreció lo mejor de ambos mundos:  
   - SQL para filtrar, unir y seleccionar datos rápidamente.  
   - Pandas para operaciones más avanzadas, como el manejo de valores faltantes, normalización de columnas y exportación del conjunto de datos procesado.

4. **Exportación a CSV:**  
   El conjunto de datos limpio se guardó como un nuevo archivo CSV (`clean_dataset.csv`), dejándolo listo para ser importado en Power BI y asegurando datos de alta calidad para la visualización.

Esta metodología garantiza un proceso de limpieza de datos profesional y reproducible mediante el uso de herramientas modernas que maximizan tanto la precisión como la productividad.
