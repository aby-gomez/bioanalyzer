# Bioanalyzer - Guia de Instalacion y Uso

Sistema de analisis de bioimpedancia que ajusta datos experimentales al **Modelo Teorico de Cole-Cole** mediante 4 metodos algoritmicos.

Incluye un menu interactivo en consola y herramientas de visualizacion grafica (Nyquist, Bode).

---

## Tabla de Contenidos

1. [Que hace este programa](#que-hace-este-programa)
2. [Requisitos previos](#requisitos-previos)
3. [Instalacion en Windows](#instalacion-en-windows)
4. [Instalacion en Linux](#instalacion-en-linux)
5. [Ejecutar el programa](#ejecutar-el-programa)
6. [Uso del menu interactivo](#uso-del-menu-interactivo)
7. [Descripcion de los metodos](#descripcion-de-los-metodos)
8. [Parametros Cole-Cole](#parametros-cole-cole)
9. [Ejecutar tests](#ejecutar-tests)
10. [Estructura del proyecto](#estructura-del-proyecto)
11. [Solucion de problemas](#solucion-de-problemas)

---

## Que hace este programa

Este programa recibe archivos Excel con mediciones de bioimpedancia (provenientes de equipos Solartron) y ajusta esos datos a una circunferencia en el plano complejo para obtener los **4 parametros fisicos del modelo Cole-Cole**:

- **Rinf**: Resistencia a frecuencia infinita
- **R0**: Resistencia a frecuencia cero
- **tau**: Constante de tiempo caracteristica
- **alpha**: Exponente de distribucion

El programa ofrece 4 metodos diferentes para realizar este ajuste y genera graficas comparativas.

---

## Requisitos previos

- **Python 3.10 o superior** (se recomienda Python 3.12)
- **Un archivo Excel (.xlsx)** con datos de bioimpedancia (opcional: se incluye uno de prueba)

---

## Instalacion en Windows

### Paso 1: Instalar Python

1. Abre tu navegador y ve a: https://www.python.org/downloads/
2. Haz clic en el boton amarillo **"Download Python 3.12.x"** (o la version mas reciente)
3. Ejecuta el archivo descargado
4. **IMPORTANTE**: En la primera pantalla del instalador, marca la casilla que dice:
   ```
   ☑ Add python.exe to PATH
   ```
   Esto permite usar Python desde cualquier carpeta de tu computadora
5. Haz clic en **"Install Now"** y espera a que termine

### Paso 2: Verificar que Python se instalo correctamente

1. Presiona las teclas `Windows + R` al mismo tiempo
2. Escribe `cmd` y presiona Enter (se abre la ventana de comandos)
3. Escribe el siguiente comando y presiona Enter:
   ```
   python --version
   ```
4. Deberia aparecer algo como: `Python 3.12.x`

### Paso 3: Descargar e instalar VS Code (opcional pero recomendado)

1. Ve a: https://code.visualstudio.com/
2. Haz clic en **"Download for Windows"**
3. Ejecuta el instalador con las opciones por defecto
4. Abre VS Code
5. Presiona `Ctrl + Shift + X` para abrir Extensiones
6. Escribe `Python` en la busqueda
7. Instala la extension **"Python"** de Microsoft (la primera que aparece)

### Paso 4: Abrir el proyecto

1. Descarga el proyecto en Github haciendo click en el boton verde 'Code' y luego 'Download as Zip' luego copia la carpeta `bioanalyzer` en una ubicacion facil de recordar (por ejemplo, tu Escritorio)
2. Abre VS Code
3. Ve a `File` > `Open Folder...`
4. Selecciona la carpeta `bioanalyzer`
5. Abre la terminal: `Terminal` > `New Terminal` (o presiona `` Ctrl + ` ``)

### Paso 5: Crear el entorno virtual

Ejecutar: 

```
python -m venv venv
```


Verificar si la terminal es Powershell o CMD 

Si es Powershell ejecutar: 

```
.\venv\Scripts\Activate.ps1
```

Si es CMD :

```
venv\Scripts\activate.bat
```


### Paso 6: Instalar las librerias necesarias

En la terminal que abriste, escribe y presiona Enter:

```
pip install -r requirements.txt
```

Espera a que termine (puede tardar 1-2 minutos). Veras texto desplazandose por la pantalla, eso es normal.

Si ves un mensaje verde que dice **"Successfully installed..."**, la instalacion fue exitosa.

---

## Instalacion en Linux

### Paso 1: Instalar Python

La mayoria de distribuciones de Linux ya tienen Python instalado. Verifica abriendo una terminal y escribiendo:

```
python3 --version
```

Si aparece una version (ej: `Python 3.10.12`), ya tienes Python. Si no, instala Python:

**Ubuntu/Debian:**
```
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
```

**Fedora:**
```
sudo dnf install python3 python3-pip -y
```

**Arch Linux:**
```
sudo pacman -S python python-pip
```

### Paso 2: Descargar el proyecto

Opcion A - Con git (si lo tienes instalado):
```
git clone <url-del-repositorio>
cd bioanalyzer
```

Opcion B - Sin git:
Descarga la carpeta del proyecto y extraela en una ubicacion conveniente.

### Paso 3: Crear entorno virtual (recomendado)

Un entorno virtual aísla las librerias de este proyecto del resto de tu sistema:

```
python3 -m venv venv
source venv/bin/activate
```

Despues de activar el entorno, veras `(venv)` al inicio de tu linea de terminal.

### Paso 4: Instalar las librerias necesarias

```
pip install -r requirements.txt
```

Espera a que termine. Si ves **"Successfully installed..."**, todo esta listo.

### Paso 5 (Opcional): Instalar VS Code en Linux

**Ubuntu/Debian:**
```
sudo apt install code -y
```

**Fedora:**
```
sudo dnf install code -y
```

Despues abre VS Code, instala la extension de Python igual que en Windows.

---

## Ejecutar el programa

### Opcion 1: Desde VS Code (recomendado para principiantes)

1. Abre VS Code con la carpeta del proyecto
2. Abre la terminal: `Terminal` > `New Terminal`
3. Escribe:

   **Windows:**
   ```
   python -m scripts.main
   ```

   **Linux (con entorno virtual activado):**
   ```
   python3 -m scripts.main
   ```

### Opcion 2: Desde la terminal del sistema (sin VS Code)

**Windows:**
1. Abre la carpeta `bioanalyzer` en el explorador de archivos
2. Haz clic derecho en la ventana > "Abrir en Terminal" (o "Open in Terminal")
3. Escribe:
   ```
   python scripts\main.py
   ```

**Linux:**
1. Abre una terminal
2. Navega a la carpeta del proyecto:
   ```
   cd ruta/a/bioanalyzer
   ```
3. Activa el entorno virtual:
   ```
   source venv/bin/activate
   ```
4. Ejecuta:
   ```
   python scripts/main.py
   ```

### Opcion 3: Ejecutar desde la carpeta scripts

Tambien puedes ejecutar el programa estando dentro de la carpeta `scripts`:

**Windows:**
```
cd scripts
python main.py
```

**Linux:**
```
cd scripts
python main.py
```

---

## Uso del menu interactivo

Al ejecutar el programa, tendras la opcion de cargar datos nuevos desde en un excel o si solo presionas Enter se cargarán los datos de prueba del proyecto

```
========================================
   BIOANALYZER - Analisis de Bioimpedancia
========================================

Datos cargados: datos_prueba/nivel0_01ma_1.xlsx (XX puntos)

Seleccione un metodo:
  1) Todos los Puntos 
  2) Ayllon Original 
  3) Ayllon Modificado
  4) Levenberg-Marquardt
  5) Comparar todos los metodos
  6) Cambiar archivo de datos
  0) Salir
```

### Navegacion

- Escribe el **número** de la opciún que deseas y presiona Enter
- Despues de ejecutar un método, se mostrarán los 7 parámetros en pantalla
- Se abrirá automáticamente una ventana con las gráficas
- Se te preguntara si deseas generar la grafica comparativa
- Para salir, escribe `0` y presiona Enter

### Cambiar los datos de entrada

Si quieres usar tu propio archivo de datos:

1. Coloca tu archivo `.xlsx` en la carpeta del proyecto (o anota su ruta completa)
2. En el menu, selecciona la opcion `6`
3. Escribe la ruta del archivo y presiona Enter

**Formato del archivo Excel:** El archivo debe tener columnas llamadas (en minusculas):
- `frequency` - Frecuencia en Hz
- `real` - Parte real de la impedancia
- `imaginary` - Parte imaginaria de la impedancia
- `magnitude` - Magnitud de la impedancia
- `phase` - Fase en grados o radianes

---

## Descripcion de los metodos

### 1. Todos los Puntos 

- **Archivo:** `metodos/todos_los_puntos.py`
- **Funcion:** Prueba **todas las combinaciones posibles** de 3 puntos entre los datos experimentales
- **Como funciona:** Para cada trio de puntos, calcula la circunferencia que pasa por ellos y mide el error de ajuste. Se queda con la que tenga menor error
- **Ventaja:** No depende de semillas iniciales, es deterministico
- **Desventaja:** Es **lento** cuando hay muchos puntos (el numero de combinaciones crece rapidamente)

### 2. Ayllon Original (2008)

- **Archivo:** `metodos/ayllon.py`
- **Funcion:** `metodo_ayllon(matriz, a, c)`
- **Como funciona:**
  1. Convierte los datos a coordenadas rectangulares
  2. Construye matrices para un ajuste geometrico por minimos cuadrados
  3. Resuelve un sistema lineal para encontrar el centro y radio de la circunferencia
  4. Calcula tau mediante regresion polinomial
- **Ventaja:** Metodologia probada, basada en publicaciones cientificas
- **Desventaja:** Requiere que los datos esten bien distribuidos

### 3. Ayllon Modificado

- **Archivo:** `metodos/ayllon_modificado.py`
- **Funcion:** `metodo_ayllon_modificado(matriz, a, c)`
- **Como funciona:** Variante simplificada del metodo original
  1. Usa promedios simples en lugar de sumatorias
  2. Para calcular tau, toma directamente la frecuencia en el punto de minimo de la parte imaginaria
- **Ventaja:** Mas rapido y simple que el original
- **Desventaja:** Menos preciso en algunos casos

### 4. Levenberg-Marquardt

- **Archivo:** `metodos/lm_method.py`
- **Funcion:** `LMMethod(datos)`
- **Como funciona:**
  1. Utiliza optimizacion no lineal por minimos cuadrados
  2. Emplea el algoritmo Levenberg-Marquardt (via `scipy.optimize.curve_fit`)
  3. Requiere semillas iniciales (valores aproximados para guiar la busqueda)
- **Ventaja:** Rapido y preciso cuando las semillas son buenas
- **Desventaja:** Puede no converger si los datos son problematicos

### Comparativa entre metodos

| Caracteristica | Todos los Puntos | Ayllon Original | Ayllon Modificado | Levenberg-Marquardt |
|---|---|---|---|---|
| Velocidad | Lenta | Media | Rapida | Rapida |
| Precision | Alta | Alta | Media | Alta |
| Robustez | Alta | Media | Media | Media |
| Complejidad | Simple | Compleja | Simple | Compleja |

---

## Parametros Cole-Cole

El modelo Cole-Cole describe la impedancia electrica de un material biologico:

```
Z(w) = Rinf + (R0 - Rinf) / (1 + (j*w*tau)^alpha)
```

Donde:
- **Z(w)**: Impedancia compleja a frecuencia angular w
- **Rinf**: Resistencia a frecuencia infinita (ohms)
- **R0**: Resistencia a frecuencia cero (ohms)
- **tau**: Constante de tiempo caracteristica (segundos)
- **alpha**: Exponente de distribucion (0 < alpha <= 1)
- **w**: Frecuencia angular (2 * pi * f, en rad/s)
- **j**: Unidad imaginaria (sqrt(-1))

Los 7 valores que muestra el programa son:
1. **Rinf** - Resistencia minima (alta frecuencia)
2. **R0** - Resistencia maxima (baja frecuencia)
3. **tau** - Tiempo de relajacion caracteristico
4. **alpha** - Indica que tan "estirado" esta el arco de Nyquist
5. **x0** - Coordenada X del centro de la circunferencia
6. **y0** - Coordenada Y del centro de la circunferencia
7. **radio** - Radio de la circunferencia ajustada

---

## Estructura del proyecto

```
bioanalyzer/
|
+-- scripts/
|   +-- main.py                 # Punto de entrada (menu interactivo)
|   +-- playground.py           # Script de pruebas rapidas
|
+-- metodos/
|   +-- __init__.py
|   +-- ayllon.py               # Metodo de Ayllon Original
|   +-- ayllon_modificado.py    # Metodo de Ayllon Modificado
|   +-- todos_los_puntos.py     # Metodo combinatorio
|   +-- lm_method.py            # Metodo Levenberg-Marquardt
|   +-- circunferencia.py       # Calculo de circunferencia por 3 puntos
|   +-- calcular_error_dv.py    # Calculo de error de ajuste
|   +-- parameters.py           # Extraccion de parametros Cole-Cole
|   +-- graficas.py             # Graficas individuales (4 subplots)
|   +-- fourgraficas.py         # Grafica comparativa (5 subplots)
|   +-- graficar_nquyst.py      # Diagrama de Nyquist standalone
|
+-- tests/
|   +-- __init__.py
|   +-- test_ayllon_modificado.py   # Tests unitarios
|
+-- datos_prueba/
|   +-- nivel0_01ma_1.xlsx      # Datos de ejemplo
|
+-- requirements.txt            # Lista de dependencias
+-- .gitignore                  # Archivos excluidos de git
+-- README.md                   # Este archivo
```

---

## Descripcion de cada archivo del modulo metodos/

### circunferencia.py
Calcula la circunferencia que pasa exactamente por 3 puntos dados en el plano 2D. Resuelve un sistema lineal 3x3 para obtener el centro (x0, y0) y el radio.

### calcular_error_dv.py
Calcula dos metricas de error para una circunferencia candidata:
- **E1:** Error absoluto promedio entre la distancia de cada punto al centro y el radio
- **E2_normal:** Error relativo normalizado

### parameters.py
Convierte los parametros geometricos de la circunferencia (centro x0, y0 y radio R) en los 4 parametros fisicos del modelo Cole-Cole:
- R0 = sqrt(R^2 - y0^2) + x0
- Rinf = x0 - sqrt(R^2 - y0^2)
- alpha = (2/pi) * atan(y0 / sqrt(R^2 - y0^2))
- tau = 1 / (2*pi*fc), donde fc es la frecuencia en el punto de minimo imaginario

### graficas.py
Genera un grafico 2x2 para un metodo individual con:
1. Diagrama de Nyquist (R vs -X)
2. Modulo |Z| vs frecuencia angular
3. Parte Real vs frecuencia angular
4. Parte Imaginaria vs frecuencia angular

### fourgraficas.py
Genera un grafico 2x3 (5 graficos activos + leyenda) comparando **todos los metodos** simultaneamente con colores diferentes por metodo.

### graficar_nquyst.py
Genera un unico grafico del diagrama de Nyquist con scatter de datos experimentales y arco teorico continuo.

---

## Solucion de problemas

### "python no se reconoce como comando interno"

**Windows:** Python no se agrego al PATH durante la instalacion. Solucion:
1. Desinstala Python desde Panel de Control > Programas
2. Vuelve a instalarlo marcando la casilla **"Add python.exe to PATH"**

**Linux:** Usa `python3` en lugar de `python`, o instala `sudo apt install python-is-python3`

### "No module named 'numpy'" (o pandas, matplotlib, etc.)

Las librerias no estan instaladas. Ejecuta:
```
pip install -r requirements.txt
```

### "No such file or directory: scripts/main.py"

No estas en la carpeta correcta. Verifica que estas en la carpeta raiz de `bioanalyzer`:
```
# Windows
dir

# Linux
ls
```

Deberias ver las carpetas `scripts/`, `metodos/`, `tests/`, etc.

### "Could not open file 'datos_prueba/...'"

No se encuentra el archivo de datos. Verifica que la carpeta `datos_prueba/` existe y contiene el archivo `.xlsx`.

### Las graficas no aparecen

Asegurate de tener un entorno grafico (escritorio). Si estas en un servidor sin pantalla, las graficas no se mostraran.

### Error en Linux: "externally-managed-environment"

Usa un entorno virtual (paso 3 de la instalacion en Linux) o instala con `--break-system-packages`:
```
pip install -r requirements.txt --break-system-packages
```

### Quiero usar mi propio archivo de datos

Asegurate de que tu archivo Excel tenga estas columnas (en minusculas):
- `frequency`
- `real`
- `imaginary`
- `magnitude`
- `phase`

Puedes usar el archivo de prueba como referencia para el formato.

---

## Informacion adicional

- **Proyecto original:** Migrado de MATLAB/Octave a Python
- **Librerias utilizadas:** numpy, pandas, openpyxl, scipy, matplotlib
- **Python requerido:** 3.10 o superior (recomendado 3.12)
- **Licencia:** Ver archivo LICENSE si existe
