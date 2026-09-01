import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, '..')

from metodos.ayllon_modificado import metodo_ayllon_modificado
from metodos.ayllon import metodo_ayllon
from metodos.graficas import graficar_resultados
from metodos.todos_los_puntos import TodosLosPuntos
from metodos.graficar_nquyst import graficar_nyquist
from metodos.fourgraficas import generar_fourgraficas
from metodos.lm_method import LMMethod

# 1. Configuración de parámetros de entrada
PARAMETRO_A = 0  # 0: real/imag, 1: mod/fase
PARAMETRO_C = 1  # 0: rad/s,     1: Hz

# Cargar un archivo Excel real
df = pd.read_excel('datos_prueba/nivel0_01ma_1.xlsx')

# Extraemos 3 columnas → sigue siendo DataFrame , .values lo convierte → NumPy array (matriz)
datos = df[['frequency', 'real', 'imaginary', 'magnitude', 'phase']].values

print("Primeras 5 filas:")
print(datos[:5])

# Ejecutar método
#resultado = metodo_ayllon_modificado(datos, a=PARAMETRO_A, c=PARAMETRO_C)
#resultado = metodo_ayllon(datos, a=PARAMETRO_A, c=PARAMETRO_C)

resultados_para_graficar = {}

""" metodo = 'Ayllon Original'
Rinf  = resultado[0]
Rcero = resultado[1]
tau   = resultado[2]
alpha = resultado[3]
x0    = resultado[4]
y0    = resultado[5]
radio = resultado[6] """



""" print("\nResultados:")
print(f"Rinf  = {Rinf}")
print(f"R0    = {Rcero}")
print(f"tau   = {tau}")
print(f"alpha = {alpha}")
print(f"x0    = {x0}")
print(f"y0    = {y0}")
print(f"radio = {radio}") """


""" resultado= TodosLosPuntos(datos)
metodo = 'Todos los puntos'

Rinf  = resultado[0]
Rcero = resultado[1]
tau   = resultado[2]
alpha = resultado[3]
circunferencia = resultado[4]
best_error = resultado[5]

print("\nResultados:")
print(f"Rinf  = {Rinf}")
print(f"R0    = {Rcero}")
print(f"tau   = {tau}")
print(f"alpha = {alpha}")
print(f"x0 = {circunferencia[0]}")
print(f"y0 = {circunferencia[1]}")
print(f"radio = {circunferencia[2]}")
print(f"mejor error = {best_error}")

graficar_resultados(metodo,datos, resultado, parametro_c=PARAMETRO_C )  """


# ==============================================================================
# METODO 1: TODOS LOS PUNTOS
# ==============================================================================
print("\n--- Ejecutando Todos los Puntos ---")
resultado_tdp = TodosLosPuntos(datos)

Rinf_tdp  = resultado_tdp[0]
Rcero_tdp = resultado_tdp[1]
tau_tdp   = resultado_tdp[2]
alpha_tdp = resultado_tdp[3]
circ_tdp  = resultado_tdp[4] # Array [x0, y0, radio]
best_error = resultado_tdp[5]

print(f"Rinf  = {Rinf_tdp}")
print(f"R0    = {Rcero_tdp}")
print(f"tau   = {tau_tdp}")
print(f"alpha = {alpha_tdp}")
print(f"x0    = {circ_tdp[0]}")
print(f"y0    = {circ_tdp[1]}")
print(f"radio = {circ_tdp[2]}")
print(f"Mejor error = {best_error}")

# Guardamos en el diccionario con la estructura de 7 elementos: [Rinf, R0, tau, alpha, x0, y0, R]
resultados_para_graficar['Todos los Puntos'] = [
    Rinf_tdp, Rcero_tdp, tau_tdp, alpha_tdp, circ_tdp[0], circ_tdp[1], circ_tdp[2]
]

# ==============================================================================
# METODO 2: AYLLÓN ORIGINAL (Opcional, descomentar si querés comparar)
# ==============================================================================
print("\n--- Ejecutando Ayllón Original ---")
resultado_ayllon = metodo_ayllon(datos, a=PARAMETRO_A, c=PARAMETRO_C)
resultados_para_graficar['Ayllon Original'] = resultado_ayllon

Rinf_ayllon  = resultado_ayllon[0]
Rcero_ayllon = resultado_ayllon[1]
tau_ayllon   = resultado_ayllon[2]
alpha_ayllon = resultado_ayllon[3]



print(f"Rinf  = {Rinf_ayllon}")
print(f"R0    = {Rcero_ayllon}")
print(f"tau   = {tau_ayllon}")
print(f"alpha = {alpha_ayllon}")
print(f"x0    = {resultado_ayllon[4]}")
print(f"y0    = {resultado_ayllon[5]}")
print(f"radio = {resultado_ayllon[6]}")

# ==============================================================================
# METODO 3: AYLLÓN MODIFICADO (Opcional, descomentar si querés comparar)
# ==============================================================================
print("\n--- Ejecutando Ayllón Modificado ---")
resultado_ayllon_mod = metodo_ayllon_modificado(datos, a=PARAMETRO_A, c=PARAMETRO_C)
resultados_para_graficar['Ayllon Modificado'] = resultado_ayllon_mod

Rinf_ayllon  = resultado_ayllon_mod[0]
Rcero_ayllon = resultado_ayllon_mod[1]
tau_ayllon   = resultado_ayllon_mod[2]
alpha_ayllon = resultado_ayllon_mod[3]



print(f"Rinf  = {resultado_ayllon_mod[0]}")
print(f"R0    = {resultado_ayllon_mod[1]}")
print(f"tau   = {resultado_ayllon_mod[2]}")
print(f"alpha = {resultado_ayllon_mod[3]}")
print(f"x0    = {resultado_ayllon_mod[4]}")
print(f"y0    = {resultado_ayllon_mod[5]}")
print(f"radio = {resultado_ayllon_mod[6]}")
print("\n--- Ejecutando Levenberg-Marquardt ---")

resultado_lm = LMMethod(datos) # Retorna directamente el array de 7 elementos
resultados_para_graficar['Metodo LM'] = resultado_lm



print(f"Rinf  = {resultado_lm[0]}")
print(f"R0    = {resultado_lm[1]}")
print(f"tau   = {resultado_lm[2]}")
print(f"alpha = {resultado_lm[3]}")
print(f"x0    = {resultado_lm[4]}")
print(f"y0    = {resultado_lm[5]}")
print(f"radio = {resultado_lm[6]}")

# ==============================================================================
# GENERACIÓN DE LAS 4 GRÁFICAS COMPARATIVAS
# ==============================================================================
print("\nGenerando gráficas comparativas...")
generar_fourgraficas(datos, resultados_para_graficar, c=PARAMETRO_C)
graficar_resultados("lm metodo",datos, resultado_lm, parametro_c=PARAMETRO_C )
   

