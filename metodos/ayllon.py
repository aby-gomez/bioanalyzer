import numpy as np

def metodo_ayllon(matriz: np.ndarray, a: int, c: int) -> np.ndarray:
    """
    Método de Ayllon Original (2008) para Cole-Cole
    
    Parámetros:
    -----------
    matriz : numpy array (Nx3)
        Columna 1: frecuencia
        Columna 2: real o módulo
        Columna 3: imaginaria o fase
    a : int
        0 = datos en real/imaginaria
        1 = datos en módulo/fase
    c : int
        0 = frecuencia en rad/s
        1 = frecuencia en Hz
    
    Retorna:
    --------
    array : [Rinf, R0, tau, alpha, x0, y0, radio]
    """

    # 1. VALIDACIÓN DE TIPOS (Defensa contra tipos incorrectos)
    if not isinstance(matriz, np.ndarray):
        raise TypeError("El parámetro 'matriz' debe ser un arreglo de NumPy (np.ndarray).")
    
    if not isinstance(a, int) or not isinstance(c, int):
        raise TypeError("Los parámetros 'a' y 'c' deben ser números enteros.")

    # 2. VALIDACIÓN DE ESTRUCTURA (Defensa contra dimensiones incorrectas)
    #Si no es una matriz bidimensional (si es 1 es un arreglo si es 3 es un cubo) O si tiene menos de 3 columnas lanza error
    if matriz.ndim != 2 or matriz.shape[1] < 3:
        raise ValueError(
            f"La matriz de entrada debe tener 2 dimensiones y al menos 3 columnas. "
            f"Dimensiones provistas: {matriz.shape}"
        )

    # 3. VALIDACIÓN DE VALORES/BANDERAS (Defensa contra configuraciones inválidas)
    if a not in (0, 1):
        raise ValueError(f"El parámetro 'a' debe ser 0 o 1. Valor recibido: {a}")
        
    if c not in (0, 1):
        raise ValueError(f"El parámetro 'c' debe ser 0 o 1. Valor recibido: {c}")
    
    #Inicio programa

    
    # 1. Convertir a rectangular(cartesiana)
    if a == 0: 
        X = matriz[:, 1]
        Y = matriz[:, 2]
    else: 
        X = matriz[:, 1] * np.cos(matriz[:, 2] * np.pi / 180.0)
        Y = matriz[:, 1] * np.sin(matriz[:, 2] * np.pi / 180.0)
    
    Z = X + 1j * Y
    n_filas = matriz.shape[0]
    
  # 2. Construcción de matrices del ajuste geométrico (Traducción directa de ecuaciones base)
    # Mapeo exacto de m1, X1, k1, X2... para reproducir la matriz A y el vector b de MATLAB
    m1 = (1.0 / n_filas) * np.sum(2 * X)
    X1 = -2 * X + m1
    k1 = (1.0 / n_filas) * np.sum(X)
    X2 = X - k1
    a11 = np.sum(X1 * X2)
    
    m2 = (1.0 / n_filas) * np.sum(2 * Y)
    X3 = -2 * Y + m2
    a12 = np.sum(X3 * X2)
    
    k2 = (1.0 / n_filas) * np.sum(Y)
    X4 = Y - k2
    a21 = np.sum(X1 * X4)
    a22 = np.sum(X3 * X4)

    # 3. Construir matriz A (2x2)
    A = np.array([[a11, a12], 
                  [a21, a22]])
    
    # 4. Construir vector b (2x1)
    # media de la suma de los cuadrados
    m3 = (1.0 / n_filas) * np.sum(X**2 + Y**2)
    X5 = X**2 + Y**2 - m3
    b1 = np.sum(X5 * X2)
    b2 = np.sum(X5 * X4)
    b = -np.array([b1, b2])



    # 5. Devuelve las coordenadas del centro (mismo resultado que si invirtiera previamente la matriz)
    C = np.linalg.solve(A, b)
    C_complejo = C[0] + 1j * C[1]


    # 6. Calcular radio
    R2 = C[0]**2 + C[1]**2 + (1.0 / n_filas) * np.sum((X**2) + (Y**2) - (2 * C[0] * X) - (2 * C[1] * Y))
    R = np.sqrt(R2)

    # 7. Extraer Rinf, R0, alpha
    term_geo = np.sqrt(R2 - C[1]**2)
    Rinf = C[0] - term_geo
    R0 = C[0] + term_geo
    
    alpha = 1.0 - (2.0 / np.pi) * np.arctan(C[1] / term_geo)
    if alpha > 1.0:
        alpha = 1.0 + (np.arctan(C[1] / np.sqrt(R2 - X.imag**2)) / np.pi) * 2.0
    
    ## 8. Regresión polinomial para determinar Parámetro Temporal (Rodriguez Portero)
    if c == 0:
        f = matriz[:, 0] / (2.0 * np.pi)
    else:
        f = matriz[:, 0]
        
    # Construcción de la matriz de diseño Q = [1, f, f^2]
    Q = np.vstack([np.ones(n_filas), f, f**2]).T
    
    # Vector auxiliar 'aux'
    # Nota: Se añade una tolerancia pequeña (1e-12) en el denominador para evitar divisiones por cero estables
    denominador = Z - Rinf
    denominador = np.where(denominador == 0, 1e-12, denominador)
    aux = np.abs(1j * f * ((R0 - Rinf) / denominador - 1.0)**(-1.0 / alpha))
    
    # la pseudoinversa se aplica sobre Q directamente
    M = np.linalg.pinv(Q)
    V = M @ aux
    
    # fc en el script de MATLAB representa la frecuencia angular de transición (omega_c)
    omega_c = np.abs(V[0])
    
    # Se replica la doble división por 2*pi que arrastra el script de MATLAB original
    tau = 1.0 / omega_c / 2.0 / np.pi
        
    # 7. Retornar parámetros geométricos y decaimiento
    return np.array([Rinf, R0, tau, alpha, C[0], C[1], R])