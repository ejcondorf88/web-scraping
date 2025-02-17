# Proyecto de Análisis de Carreras y Empresas

Este proyecto contiene archivos y scripts para analizar información relacionada con carreras, universidades, empresas y salarios. A continuación, se explica cómo configurar y usar el proyecto paso a paso.

**¡No te preocupes si no tienes experiencia en programación! Este tutorial está diseñado para guiarte paso a paso.**

---

## Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Python instalado:** Necesitas tener Python instalado en tu computadora. Si no lo tienes, sigue las instrucciones a continuación.
2. **Git instalado (opcional):** Si quieres clonar el repositorio, necesitas Git. Si no lo tienes, puedes descargar el proyecto como un archivo ZIP.

---

## Paso 1: Verificar si tienes Python instalado

1. **¿Qué es Python?**
   - Python es un lenguaje de programación que usaremos para ejecutar los análisis. No te preocupes, no necesitas saber programar para usarlo.

2. **Verifica si ya tienes Python instalado:**
   - Abre una terminal o consola:
     - En **Windows:** Presiona `Win + R`, escribe `cmd` y presiona Enter.
     - En **macOS o Linux:** Abre la aplicación "Terminal".
   - Ejecuta el siguiente comando para verificar si tienes Python instalado:
     ```bash
     python --version
     ```
   - Si ves algo como `Python 3.x.x`, ¡ya tienes Python instalado! Puedes pasar al siguiente paso.
   - Si no ves nada o aparece un mensaje de error, sigue las instrucciones para instalar Python.

3. **Instalar Python (si no lo tienes):**
   - Ve al sitio oficial de Python: [https://www.python.org/](https://www.python.org/).
   - Descarga e instala la versión más reciente de Python.
   - Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"** (Agregar Python al PATH) antes de hacer clic en "Install Now".

---

## Paso 2: Instalar las dependencias

Este proyecto utiliza varias bibliotecas de Python, como **pdfplumber** para extraer información de archivos PDF. Para instalarlas, sigue estos pasos:

1. **Descargar el proyecto:**
   - Si tienes Git instalado, abre una terminal y ejecuta:
     ```bash
     git clone <URL_DEL_REPOSITORIO>
     ```
   - Si no tienes Git, descarga el proyecto como un archivo ZIP desde el repositorio y descomprímelo en una carpeta de tu computadora.

2. **Instalar un entorno virtual (opcional pero recomendado):**
   - Un entorno virtual es como una "caja separada" donde instalaremos todo lo necesario para el proyecto sin afectar el resto de tu computadora.
   - En la terminal, navega hasta el directorio donde se encuentra el proyecto:
     ```bash
     cd ruta/del/proyecto
     ```
   - Crea un entorno virtual:
     ```bash
     python -m venv venv
     ```
   - Activa el entorno virtual:
     - En **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - En **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

3. **Instalar las dependencias necesarias:**
   - Con el entorno virtual activado, instala las bibliotecas necesarias usando **pip**:
     ```bash
     pip install -r requirements.txt
     ```
   - Esto instalará automáticamente todas las herramientas que el proyecto necesita.

---

## Paso 3: Configuración y ejecución de los scripts

Una vez que tengas todo instalado, puedes empezar a ejecutar los scripts de análisis. Sigue estos pasos:

1. **Ejecutar el script principal:**
   - En la terminal, navega hasta el directorio del proyecto donde se encuentra el script Python (por ejemplo, `Carreras.py`) y ejecuta el siguiente comando:
     ```bash
     python Carreras.py
     ```
   - El script comenzará a procesar los datos y mostrará los resultados en la terminal o generará archivos de salida según lo programado.

2. **Entender los resultados:**
   - Los resultados pueden incluir tablas, gráficos o archivos exportados (como CSV o PDF). Estos archivos estarán en la carpeta del proyecto o en una carpeta específica mencionada en las instrucciones del script.

---

## ¿Necesitas ayuda?

Si tienes problemas o preguntas, no dudes en contactar al equipo del proyecto o consultar la documentación adicional en el repositorio. También puedes buscar ayuda en foros como [Stack Overflow](https://stackoverflow.com/) o comunidades de Python.

---

### Notas adicionales

- **¿Qué es un archivo ZIP?**
  - Un archivo ZIP es un archivo comprimido que contiene varios archivos y carpetas. Puedes descomprimirlo haciendo doble clic en él o usando herramientas como WinRAR o 7-Zip.

- **¿Qué es un entorno virtual?**
  - Un entorno virtual es una forma de mantener las herramientas y bibliotecas del proyecto separadas del resto de tu sistema. Es útil para evitar conflictos entre diferentes proyectos.

- **¿Qué es pip?**
  - Pip es una herramienta que se usa para instalar bibliotecas y paquetes de Python. Piensa en ello como una tienda donde puedes descargar herramientas específicas para tu proyecto.

---

¡Esperamos que disfrutes explorando este proyecto!
