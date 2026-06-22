import numpy as np
import matplotlib.pyplot as plt

def generar_fourgraficas(datos: np.ndarray, resultados_metodos: dict, c: int):
    """
    Reconstruye las curvas teóricas de Cole-Cole para cada método y genera
    las 4 gráficas comparativas. Equivale a fourgraficas.m
    
    Parámetros:
    -----------
    datos : np.ndarray
        Matriz original con columnas [frecuencia, parte_real, parte_imaginaria]
    resultados_metodos : dict
        Diccionario con los arrays de salida de cada método, por ejemplo:
        {
           'Ayllon Modificado': [Rinf, R0, tau, alpha, x0, y0, R],
           'Todos los Puntos': [Rinf, R0, tau, alpha, x0, y0, R]
        }
    c : int
        0 = frecuencia en rad/s, 1 = frecuencia en Hz
    """
    freq = datos[:, 0]
    R_exp = datos[:, 1]
    X_exp = datos[:, 2] # Nota: En Python usualmente se mantiene el signo real
    
    # Escalar frecuencia angular (w) según la bandera c
    w = freq * (2.0 * np.pi) if c == 1 else freq
    j = 1j

    # Crear el lienzo de 2x2
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Comparativa de Métodos de Ajuste - Modelo Cole-Cole", fontsize=14, fontweight='bold')

    # Definir colores fijos para cada método (similar al script de MATLAB)
    colores = {
        'Ayllon Modificado': 'g-',
        'Ayllon Original': 'b-',
        'Todos los Puntos': 'c-'
    }

    # 1. Gráfica de Datos Experimentales (Puntos Rojos) en los 4 subplots
    axs[0, 0].plot(R_exp, -X_exp, '*r', label='Datos Exp.') # Nyquist
    axs[0, 1].semilogx(freq, np.sqrt(R_exp**2 + X_exp**2), '*r') # |Z| vs f
    axs[1, 0].loglog(freq, R_exp, '*r') # R vs f
    axs[1, 1].loglog(freq, -X_exp, '*r') # -X vs f

    # Diccionario para exportar las matrices Zbest finales
    zbest_export = {}

    # 2. Reconstrucción y graficación de curvas teóricas para cada método provisto
    for nombre_metodo, params in resultados_metodos.items():
        Rinf, R0, tau, alpha = params[0], params[1], params[2], params[3]
        
        # Ecuación de Cole-Cole (Traducción exacta de aux y aux2 de tu .m)
        # Se usa freq/(2*pi) si el método internamente requería Hz, o w directo.
        # Para acoplar estricto con tu script:
        f_termino = freq / (2.0 * np.pi) if c == 1 else freq
        
        aux = (1.0 + (j * f_termino * tau) ** alpha)
        Z_est = Rinf + (R0 - Rinf) / aux
        
        X_est = Z_est.real
        Y_est = Z_est.imag
        mod_Zest = np.abs(Z_est)

        # Guardar datos simulados para el retorno de la función
        zbest_export[nombre_metodo] = np.vstack([freq, X_est, Y_est, mod_Zest]).T

        # Dibujar la línea del método correspondiente si está mapeado en los colores
        fmt = colores.get(nombre_metodo, 'k-')

        axs[0, 0].plot(X_est, -Y_est, fmt, label=nombre_metodo)
        axs[0, 1].semilogx(freq, mod_Zest, fmt)
        axs[1, 0].loglog(freq, X_est, fmt)
        axs[1, 1].loglog(freq, -Y_est, fmt)

    # 3. Formateo y Estética de los Subplots
    # Cuadrante 1: Nyquist
    axs[0, 0].set_xlabel('R ($\Omega$)')
    axs[0, 0].set_ylabel('-X ($\Omega$)')
    axs[0, 0].set_title('Cole Cole (Plano Complejo)')
    axs[0, 0].grid(True, which="both")
    axs[0, 0].legend(loc='lower left')

    # Cuadrante 2: Módulo Z
    axs[0, 1].set_xlabel('Frecuencia (Hz)' if c==1 else '$\omega$ (rad/s)')
    axs[0, 1].set_ylabel('|Z| ($\Omega$)')
    axs[0, 1].set_title('|Z| vs f')
    axs[0, 1].grid(True, which="both")

    # Cuadrante 3: Componente Real R(w)
    axs[1, 0].set_xlabel('Frecuencia (Hz)')
    axs[1, 0].set_ylabel('R ($\Omega$)')
    axs[1, 0].set_title('R(w)')
    axs[1, 0].grid(True, which="both")

    # Cuadrante 4: Componente Imaginaria X(w)
    axs[1, 1].set_xlabel('Frecuencia (Hz)')
    axs[1, 1].set_ylabel('-X ($\Omega$)')
    axs[1, 1].set_title('-X(w)')
    axs[1, 1].grid(True, which="both")

    plt.tight_layout()
    plt.show()

    return zbest_export