# Guía de Uso e Instalación: Análisis de Bioimpedancia (Modelo Cole-Cole)

Este proyecto permite procesar archivos de mediciones de bioimpedancia (procedentes de equipos Solartron) para ajustar los datos experimentales al **Modelo Teórico de Cole-Cole** mediante 4 métodos algorítmicos. Incluye un menú interactivo en consola y herramientas para la visualización de datos en el plano complejo (Nyquist) y esquemas de Bode (Módulo, Parte Real, Parte Imaginaria y Fase).

---

## Prerrequisitos e Instalación Inicial

Si nunca has programado o no tienes herramientas de desarrollo instaladas en tu computadora, sigue estos pasos:

### 1. Descargar e instalar Python
Python es el lenguaje en el que está escrito este programa.

1. Ve al sitio oficial: [python.org/downloads](https://www.python.org/downloads/).
2. Descarga la versión más reciente para tu sistema operativo (Windows, macOS o Linux).
3. **Paso Crítico en Windows:** Al iniciar el instalador, **asegúrate de marcar la casilla** que dice:
   > `☑ Add python.exe to PATH` (o "Agregar Python al PATH").
4. Haz clic en **Install Now** y completa la instalación.

---

### 2. Descargar e instalar Visual Studio Code (VS Code)
VS Code es el editor de texto y entorno donde podrás ver el código y ejecutar el programa de manera sencilla.

1. Ve a [code.visualstudio.com](https://code.visualstudio.com/).
2. Descarga e instala la versión correspondiente a tu sistema operativo.
3. Abre VS Code.
4. En el menú de la izquierda, haz clic en el ícono de **Extensiones** (cuatro cubos) o presiona `Ctrl + Shift + X` (`Cmd + Shift + X` en macOS).
5. En la barra de búsqueda escribe `Python` e instala la extensión oficial de **Microsoft**.

---

### 3. Preparar la carpeta del proyecto

1. Descarga o descomprime la carpeta de este proyecto en tu computadora (por ejemplo, en el Escritorio).
2. Abre **VS Code**.
3. Ve al menú superior: `Archivo` -> `Abrir carpeta...` (o `File` -> `Open Folder...`).
4. Selecciona la carpeta raíz del proyecto.

---

### 4. Instalar las librerías necesarias

El programa requiere módulos externos de Python para procesar datos numéricos, leer archivos Excel y generar las gráficas.

1. En VS Code, abre la terminal en el menú superior: `Terminal` -> `Nueva Terminal`.
2. Copia el siguiente comando, pégalo en la ventana inferior de la terminal y presiona `Enter`:

```bash
pip install requirements.txt



```text
════════════════════════════════════════════════════════════════
              ESTRUCTURA DE bioanalyzer (librería)
════════════════════════════════════════════════════════════════

bioanalyzer/
│
├─ __init__.py                    # Punto de entrada
│   └─ Expone: metodo_ayllon(), metodo_3_puntos(), etc.
│
├─ metodos/                       # Módulo principal
│   ├─ __init__.py
│   ├─ ayllon.py                  # Traducción MetodoAyllon.m
│   │   └─ metodo_ayllon()
│   │
│   ├─ ayllon_modificado.py       # Traducción MetodoAyllonModificado.m
│   │   └─ metodo_ayllon_modificado()
│   │
│   ├─ tres_puntos.py             # Traducción TodosLosPuntos.m
│   │   └─ metodo_tres_puntos()
│   │
│   └─ levenberg_marquardt.py     # Traducción LM_method.m
│       └─ metodo_lm()
│
├─ utils/                         # Utilidades compartidas
│   ├─ __init__.py
│   ├─ circunferencia.py          # Traducción Circunferencia.m
│   │   └─ calcular_circunferencia()
│   │
│   ├─ errores.py                 # Traducción CalcularErrorDV.m
│   │   └─ calcular_error()
│   │
│   └─ parsers.py                 # Nuevo: lectura de archivos
│       ├─ read_solartron()
│       ├─ read_csv()
│       └─ read_impedance()
│
├─ tests/
|   ├─ test_ayllon_modificado.py  # Tests automatizados
│   ├─ test_ayllon.py
│   ├─ test_tres_puntos.py
│   ├─ test_lm.py
│   └─ data/                      # Datos de referencia
│       ├─ ejemplo_matlab.csv
│       └─ resultados_esperados.json
│
├─ examples/                      # Ejemplos de uso
│   ├─ ejemplo_basico.py
│   ├─ ejemplo_batch.py
│   └─ ejemplo_comparacion_metodos.py
│
├─ docs/                          # Documentación
│   ├─ guia_instalacion.md
│   ├─ api_reference.md
│   └─ migracion_desde_matlab.md
│
├─ setup.py                       # Configuración instalación
├─ requirements.txt               # Dependencias
└─ README.md                      # Documentación principal



```
