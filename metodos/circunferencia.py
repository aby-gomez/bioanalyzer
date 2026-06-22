import numpy as np

def Circunferencia(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    # MATLAB: A=[ a(1) a(2) 1; b(1) b(2) 1; c(1) c(2) 1];
    #construye matriz de 3x3 , real , imaginaria, constante 
    A = np.array([
        [a[0], a[1], 1.0],
        [b[0], b[1], 1.0],
        [c[0], c[1], 1.0]
    ])
    
    # arma vector columna de 3x1 elevando a 2 cada componente y sumandolo, luego multiplica el vector por -1
    B = -np.array([
        [a[0]**2 + a[1]**2],
        [b[0]**2 + b[1]**2],
        [c[0]**2 + c[1]**2]
    ])  
    
    try:
        # MATLAB: Sol=A\B; (linalg.solve es el equivalente directo y eficiente)
        Sol = np.linalg.solve(A, B)
        
        # solv genera una matriz bidimensional para acceder a sus componentes se usa [][] 
        #coordenadas del centro
        x0 = -Sol[0][0] / 2.0
        y0 = -Sol[1][0] / 2.0

        #  CONTROL DE RADICANDO NEGATIVO 
        argumento_raiz = x0**2 + y0**2 - np.abs(Sol[2][0])
        
        # Si el argumento es negativo, equivale al error de solución imaginaria de MATLAB
        if argumento_raiz < 0:
            return np.array([np.nan, np.nan, np.nan])
        
         # Calcula la longitud del radio del círculo a través de la raíz cuadrada del centro al cuadrado menos el término independiente de la solución.
        radio_val = np.sqrt(x0**2 + y0**2 - np.abs(Sol[2][0]))
        
        # MATLAB: nueva_circunferencia=[centro, radio];
        return np.array([x0, y0, radio_val])
        
    except np.linalg.LinAlgError:
        # Si los puntos están alineados, el sistema no tiene solución (det = 0)
        return np.array([np.nan, np.nan, np.nan])