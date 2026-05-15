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
├─ tests/                         # Tests automatizados
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

════════════════════════════════════════════════════════════════
                        USO TÍPICO
════════════════════════════════════════════════════════════════

# Instalación
pip install bioanalyzer

# Uso básico
import bioanalyzer as ba
import pandas as pd

# Leer datos
datos = ba.read_solartron('experimento.z')

# Aplicar método
params = ba.metodo_ayllon_modificado(
    freq=datos['frecuencia'],
    real=datos['real'],
    imag=datos['imag']
)

# Ver resultados
print(f"Rinf = {params['Rinf']:.2f} Ω")
print(f"R0 = {params['R0']:.2f} Ω")
print(f"tau = {params['tau']:.2e} s")
print(f"alpha = {params['alpha']:.3f}")

```
