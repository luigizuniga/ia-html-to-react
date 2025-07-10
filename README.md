# Proyecto HTML a React

Este es un proyecto básico que contiene una estructura HTML simple que puede ser convertida a React.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `index.html`: Archivo HTML con la estructura básica de la página
- `styles.css`: Hoja de estilos CSS para dar formato a la página
- `script.js`: Archivo JavaScript con funcionalidad básica

## Uso

Para ver la página web, simplemente abre el archivo `index.html` en tu navegador favorito.

## Conversión a React

Este proyecto puede ser utilizado como base para aprender cómo convertir una página HTML estática a una aplicación React.

Para convertir este proyecto a React, necesitarás:

1. Configurar un entorno React (usando Create React App u otra herramienta)
2. Convertir la estructura HTML en componentes React
3. Transformar los estilos CSS (usando CSS Modules, Styled Components, u otra estrategia)
4. Migrar la funcionalidad JavaScript a hooks y manejadores de eventos de React

---

## Creador/Actualizador Interactivo de Proyectos React

---

Este script de Python (`create_react_project.py`) es una herramienta de línea de comandos diseñada para **simplificar la configuración inicial de un proyecto React**. Ya sea que estés iniciando un nuevo proyecto o necesites asegurarte de que la estructura de uno existente esté completa, esta herramienta te guiará de forma interactiva.

Utiliza **Axios** para peticiones HTTP y **Zustand** para la gestión de estado global, siguiendo las mejores prácticas modernas de desarrollo en React.

## Características Principales

- **Interfaz Interactiva:** Navega fácilmente por tus directorios usando la terminal para seleccionar la ubicación de tu proyecto.
- **Creación y Actualización Inteligente:** El script crea automáticamente las carpetas y archivos necesarios. Si los archivos ya existen y su contenido es idéntico al que el script generaría, no los modificará. Si son diferentes, los actualizará.
- **Validación y Seguridad:**
  - Verifica la existencia y accesibilidad de los directorios.
  - Pide tu confirmación antes de realizar cualquier cambio significativo en tus archivos o carpetas.
- **Resumen Detallado:** Al finalizar, el script te proporciona un listado claro de todos los archivos que fueron **creados** y los que fueron **modificados**.
- **Estructura de Proyecto Estándar:** Genera una estructura de proyecto React típica, ideal para comenzar rápidamente con Vite.

## Requisitos

Asegúrate de tener instalado **Python 3.6 o superior** en tu sistema.

## Cómo Usar

Sigue estos sencillos pasos para ejecutar el script:

### 1\. Guarda el Script

Copia el contenido completo del código Python que te proporcioné anteriormente y guárdalo en un archivo llamado `create_react_project.py` (o el nombre que prefieras).

### 2\. Ejecuta el Script

Abre tu terminal o línea de comandos, navega hasta la carpeta donde guardaste `create_react_project.py` y ejecútalo con Python:

```bash
python create_react_project.py
```

### 3\. Sigue las Instrucciones Interactivas

El script te guiará a través de los siguientes pasos:

- **Bienvenida:** Una breve introducción y una invitación a comenzar.
- **Selección de Directorio Base:**
  - Se te presentará una lista numerada de los directorios dentro de tu ubicación actual (comenzando desde tu carpeta personal).
  - **Navega** escribiendo el número correspondiente a la carpeta a la que deseas acceder.
  - Escribe `..` para **subir un nivel** en la jerarquía de directorios.
  - Una vez que estés en el directorio deseado donde quieres que se cree (o actualice) tu proyecto React, escribe `S` para **seleccionar**lo.
  - Puedes salir en cualquier momento escribiendo `Q`.
- **Nombre del Proyecto:** Se te pedirá que ingreses un nombre para tu nuevo proyecto React. Por defecto, será `my-react-app`.
- **Confirmación Final:** El script te mostrará la ruta completa donde se creará o modificará el proyecto y te pedirá una **confirmación final** antes de proceder.

### 4\. Revisa el Resumen

Una vez que el script haya terminado de procesar, verás un resumen en la terminal indicando:

- La ruta final del proyecto.
- Una lista de todos los archivos **creados**.
- Una lista de todos los archivos **modificados**.

## Próximos Pasos (Después de Ejecutar el Script)

Después de que el script haya completado su ejecución y haya configurado la estructura de tu proyecto, sigue estos pasos para poner en marcha tu aplicación React:

1. **Navega al directorio del proyecto:**

   ```bash
   cd "ruta/completa/de/tu/proyecto"
   ```

   (La ruta se mostrará en el resumen final del script, por ejemplo: `cd "C:/Users/TuUsuario/Documents/my-react-app"`)

2. **Instala las dependencias:**
   El `package.json` ya incluye las dependencias necesarias como `react`, `react-dom`, `axios` y `zustand`, así como las herramientas de desarrollo de Vite.

   ```bash
   npm install
   ```

3. **Ejecuta el servidor de desarrollo:**

   ```bash
   npm run dev
   ```

¡Con esto, tu aplicación React debería estar funcionando en tu navegador, lista para que empieces a desarrollar\!

## Licencia

Este proyecto está disponible como código abierto bajo los términos de la licencia MIT.
