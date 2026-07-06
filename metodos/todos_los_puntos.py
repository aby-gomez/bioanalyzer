import numpy as np
from itertools import combinations
from metodos.circunferencia import Circunferencia
from metodos.calcular_error_dv import CalcularErrorDV
from metodos.parameters import ParametersDV

def TodosLosPuntos(datos: np.ndarray):
    """
    ingresan set de datos en 3 columnas, frec, real, imaginaria
    """
    # MATLAB: tamano=(size(datos,1)), shape devuelve tupla de dimensiones (50, 3), 0 extrae el primer valor
    tamano = datos.shape[0]
    
    # para construir infinito usamos float
    best_error = float('inf')

    # centro y radio de la mejor circunferencia, array inicializado para ganar x,y y r
    best_circumference = np.array([np.nan, np.nan, np.nan])

    points3 = None
    freq_out = None
    
    # Reemplazo directo y eficiente de: for i=... for j=... for k=...
    # combinations(range(tamano), 3) genera grupos de 3 indices unicos
    for i, j, k in combinations(range(tamano), 3):
        # extrae un subarray de la fila i , la parte real e imaginaria(col 1 y 2), y sucesivamnete...
        a = datos[i, 1:3]
        b = datos[j, 1:3]
        c = datos[k, 1:3]
        

        # MATLAB: nueva_circunferencia=Circunferencia(a,b,c);
        nueva_circunferencia = Circunferencia(a, b, c)
        
        #si los 3 puntos no forman un triangulo empiezo el for nuevamente
        if np.isnan(nueva_circunferencia[0]):
            continue
            
        # MATLAB: errores_nuevos=CalcularErrorDV(nueva_circunferencia,datos);
        errores_nuevos = CalcularErrorDV(nueva_circunferencia, datos)
        error_actual = errores_nuevos[0]  # Tomamos E1 para comparar
        
        # MATLAB: if el error de la combinacion es mas chico que el actual guardamos la circun y reemplazamos best error
        if best_error > error_actual:
            best_circumference = nueva_circunferencia
            best_error = error_actual
            # Guardamos los puntos, índices y frecuencias ganadoras de la combinación
            points3 = np.array([a[0], a[1], b[0], b[1], c[0], c[1], i, j, k])
            freq_out = np.array([datos[i, 0], datos[j, 0], datos[k, 0]])
            

    Rinf, R0, tau, alpha = ParametersDV(best_circumference, datos)

    return Rinf, R0, tau, alpha, best_circumference,best_error