import numpy as np
import matplotlib.pyplot as plt

def graficar_nyquist(datos_experimentales: np.ndarray, best_circumference: np.ndarray):
    """
    Genera el Diagrama de Nyquist comparando los datos crudos con el ajuste teórico.
    """
    # 1. Desempaquetar datos experimentales
    real_exp = datos_experimentales[:, 1]
    imag_exp = datos_experimentales[:, 2]
    
    # 2. Desempaquetar geometría de la circunferencia ganadora
    x0, y0, radio = best_circumference[0], best_circumference[1], best_circumference[2]
    
    # 3. Generar el arco teórico continuo (vector de 500 puntos entre 0 y pi)
    theta = np.linspace(0, np.pi, 500)
    real_teorico = x0 + radio * np.cos(theta)
    imag_teorico = y0 + radio * np.sin(theta)
    
    # 4. Configurar el lienzo de Matplotlib
    plt.figure(figsize=(8, 6))
    
    # Graficar puntos experimentales (Dispersión / Scatter)
    plt.scatter(real_exp, -imag_exp, color='blue', alpha=0.6, label='Datos Experimentales (Excel)')
    
    # Graficar el ajuste circular (Línea continua)
    # Nota: Se usa -imag porque en bioimpedancia la parte imaginaria capacitiva es negativa, 
    # pero convencionalmente se grafica hacia arriba en el eje Y.
    plt.plot(real_teorico, imag_teorico, color='red', linestyle='--', linewidth=2, label='Ajuste Cole-Cole Teórico')
    
    # 5. Estética y formalidad de la cátedra
    plt.title('Diagrama de Nyquist - Ajuste de Impedancia Dieléctrica', fontsize=12, fontweight='bold')
    plt.xlabel('Resistencia Real (R) [Ω]', fontsize=10)
    plt.ylabel('-Reactancia Imaginaria (-X) [Ω]', fontsize=10)
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.axis('equal') # CRÍTICO: Mantiene la proporción 1:1 para que el círculo no se vea deformado como una elipse
    plt.legend(loc='upper right')
    
    # 6. Desplegar gráfico en pantalla
    plt.show()