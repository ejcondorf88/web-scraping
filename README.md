# Proyecto de Análisis de Carreras y Empresas

Este proyecto contiene archivos y scripts para analizar información relacionada con carreras, universidades, empresas y salarios. A continuación, se explica cómo configurar y usar el proyecto paso a paso.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Python instalado:** Necesitas tener Python instalado en tu computadora. Si no lo tienes, sigue las instrucciones a continuación.
2. **Git instalado (opcional):** Si quieres clonar el repositorio, necesitas Git. Si no lo tienes, puedes descargar el proyecto como un archivo ZIP.

---

## Paso 1: Verificar si tienes Python instalado

1. Abre una terminal o consola:
   - En **Windows:** Presiona `Win + R`, escribe `cmd` y presiona Enter.
   - En **macOS o Linux:** Abre la aplicación "Terminal".

2. Ejecuta el siguiente comando para verificar si tienes Python instalado:
   ```bash
   python --version
## Paso 2: Instalar las dependencias

Este proyecto utiliza varias bibliotecas de Python, como **pdfplumber** para extraer información de archivos PDF. Para instalarlas, sigue estos pasos:

1. **Instalar un entorno virtual (opcional pero recomendado):**

   Si prefieres no instalar las dependencias globalmente, puedes crear un entorno virtual de Python. Para hacerlo, sigue estos pasos:

   - En la terminal, navega hasta el directorio donde se encuentra el proyecto.
   - Ejecuta el siguiente comando para crear un entorno virtual:

     ```bash
     python -m venv venv
     ```

   - Luego, activa el entorno virtual:
     - En **Windows**:

       ```bash
       .\venv\Scripts\activate
       ```

     - En **macOS/Linux**:

       ```bash
       source venv/bin/activate
       ```

2. **Instalar las dependencias necesarias**:

   Con el entorno virtual activado, instala las bibliotecas necesarias usando **pip**:

   ```bash
   pip install -r requirements.txt
## Paso 3: Configuración y ejecución de los scripts

Una vez que tengas todo instalado, puedes empezar a ejecutar los scripts de análisis. Sigue estos pasos:

1. **Ejecutar el script principal**:

   En la terminal, navega hasta el directorio del proyecto donde se encuentra el script Python (por ejemplo, `Carreras.py`) y ejecuta el siguiente comando:

   ```bash
   python Carreras.py
