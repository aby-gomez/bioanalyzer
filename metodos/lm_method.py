import numpy as np
import scipy
from scipy.optimize import curve_fit

def lm_model(x, r, x0, y0):
    """
    Función modelo de la semicircunferencia para el optimizador.
    y = sqrt(R^2 - (x - x0)^2) + y0
    """
    # Usamos np.clip para evitar valores negativos dentro de la raíz 
    # debido a fluctuaciones numéricas durante las iteraciones del gradiente
    radicando = r**2 - (x - x0)**2
    #np.clip reemplaza cualquier valor negativo por 0
    return np.sqrt(np.clip(radicando, 0, None)) + y0

def LMMethod(datos: np.ndarray) -> np.ndarray:
    """
    Ajuste de Cole-Cole mediante el método de Levenberg-Marquardt.
    Devuelve: [Rinf, R0, tau, alpha, x0, y0, R]
    """
    # 1. Preparación de datos (Columna 1: Real, Columna 2: Imaginary)
    x_data = datos[:, 1]
    y_data = -datos[:, 2] # Inversión del plano capacitivo
    
    # 2. Suposición inicial [Radio, CentroX, CentroY]
    # Ajustamos la semilla original [2500, 3000, 10] a valores más lógicos 
    # basados en la escala real de los datos experimentales (aprox. 150, 200, 10)
    beta_in = [150.0, 200.0, 10.0]
    
    try:
        # 3. Ajuste por mínimos cuadrados no lineales (Levenberg-Marquardt)
        popt, _ = curve_fit(
            f=lm_model, 
            xdata=x_data, 
            ydata=y_data, 
            #valores de beta_in que lm_model recibe
            p0=beta_in, 
            # curve fit implementa  Levenberg-Marquardt
            method='lm' 
        )
        
        # Extracción 
        r = abs(popt[0])
        x0 = abs(popt[1])
        y0 = abs(popt[2])
        
    except RuntimeError:
        # Si el método LM no converge, devuelve un array de NaN 
        return np.array([np.nan] * 7)
    
    # 4. Cálculo analítico de parámetros de Cole-Cole
    termino_pitagoras = np.sqrt(np.clip(r**2 - y0**2, 0, None))
    r0 = termino_pitagoras + x0
    rinf = x0 - termino_pitagoras
    
    # Cálculo de alfa (con control de división por cero)
    if y0 != 0:
        alpha = (2.0 / np.pi) * np.arctan((x0 - rinf) / y0)
    else:
        alpha = 0.0
        
    if alpha < 0:
        alpha = 1.0 + alpha
        
    # Cálculo de tau 
    pos_max_imag = np.argmin(datos[:, 2]) # El valor más negativo de la parte imaginaria
    fc = datos[pos_max_imag, 0]           # Frecuencia correspondiente
    tau = 1.0 / (2.0 * np.pi * fc)
    
    # Retornamos el vector estructurado de 7 parámetros
    return np.array([rinf, r0, tau, alpha, x0, y0, r])