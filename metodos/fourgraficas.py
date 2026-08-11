import numpy as np
import matplotlib.pyplot as plt

def generar_fourgraficas(datos: np.ndarray, resultados_metodos: dict, c: int):
    """
    Reconstruye las curvas teóricas de Cole-Cole para cada método y genera
    las 4 gráficas comparativas con la escala y matemática correctas (semilogx).
    
    Parámetros:
    -----------
    datos : numpy array (Nx5)
        Columna 1: frecuencia
        Columna 2: parte real
        Columna 3: parte imaginaria
        Columna 4: módulo de Z
        Columna 5: fase en grados

    resultados_metodos : dict
        Diccionario con los arrays de salida de cada método:
        {
           'Todos los Puntos': [Rinf, R0, tau, alpha, x0, y0, R],
           'Levenberg-Marquardt': [Rinf, R0, tau, alpha, x0, y0, R]
        }

    c : int
        0 = frecuencia en rad/s
        1 = frecuencia en Hz
    """
    
    frecuencias = datos[:, 0]
    X_exp = datos[:, 1]
    Y_exp = datos[:, 2]
    fase_exp    = datos[:, 4]
    # Calcular frecuencias angulares (w) igual que en graficar_resultados
    w = frecuencias * (2 * np.pi) if c == 1 else frecuencias
    j = 1j

    # Crear el lienzo de 2x3
    fig, axs = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle("Comparativa de Métodos de Ajuste - Modelo Cole-Cole", fontsize=14, fontweight='bold')

    # Definir estilos y colores por método
    colores = {
        'Ayllon Modificado': 'g-',
        'Ayllon Original': 'b-',
        'Todos los Puntos': 'c-',
        'Levenberg-Marquardt': 'm--'
    }

    # 1. Graficar Datos Experimentales (Puntos Rojos en los 4 subplots)
    axs[0, 0].plot(X_exp, -Y_exp, '*r', label='Datos Experimentales') # Nyquist
    axs[0, 1].semilogx(w, np.sqrt(X_exp**2 + Y_exp**2), '*r')          # |Z| vs w
    axs[0, 2].semilogx(w, X_exp, '*r')                                 # 3. Real vs w
    axs[1, 0].semilogx(w, -Y_exp, '*r')                                 # Real vs w
    axs[1, 1].semilogx(w, fase_exp, '*r')                                # -Imag vs w

    zbest_export = {}

    # 2. Reconstrucción y graficación de curvas teóricas para cada método provisto
    for nombre_metodo, params in resultados_metodos.items():
        Rinf, R0, tau, alpha = params[0], params[1], params[2], params[3]
        
        # Ecuación de Cole-Cole corregida usando la frecuencia angular w correspondiente
        Z_est = Rinf + (R0 - Rinf) / (1 + (j * w * tau) ** alpha)

        
        EstX = Z_est.real
        EstY = Z_est.imag
        mod_Zest = np.abs(Z_est)
        fase_est_rad = np.arctan2(EstY, EstX)
        fase_est = np.degrees(fase_est_rad) 

        # Guardar datos simulados para el retorno
        zbest_export[nombre_metodo] = np.vstack([frecuencias, EstX, EstY, mod_Zest, fase_est]).T

        # Obtener formato de color asignado
        fmt = colores.get(nombre_metodo, 'k-')

        # Superponer la línea del método en cada cuadrante
        axs[0, 0].plot(EstX, -EstY, fmt, label=nombre_metodo)
        axs[0, 1].semilogx(w, mod_Zest, fmt)
        axs[0, 2].semilogx(w, EstX, fmt)
        axs[1, 0].semilogx(w, -EstY, fmt)
        axs[1, 1].semilogx(w, fase_est, fmt)

    # 3. Formateo, Etiquetas y Estética de los Subplots (Uso de semilogx)
    # Subplot [0, 0]: Nyquist
    axs[0, 0].set_xlabel('R ($\Omega$)')
    axs[0, 0].set_ylabel('-X ($\Omega$)')
    axs[0, 0].set_title('Modelo Cole-Cole (Plano Complejo)')
    axs[0, 0].grid(True)
   

    # Subplot [0, 1]: Módulo Z
    axs[0, 1].set_xlabel('$\omega$ (rad/s)')
    axs[0, 1].set_ylabel('|Z| ($\Omega$)')
    axs[0, 1].set_title('|Z| vs Frecuencia Angular ($\omega$)')
    axs[0, 1].grid(True, which="both")

    # Subplot [0, 2]: Parte Real 
    axs[0, 2].set_xlabel('$\omega$ (rad/s)')
    axs[0, 2].set_ylabel('Real(Z) ($\Omega$)')
    axs[0, 2].set_title('Parte Real vs $\omega$')
    axs[0, 2].grid(True, which="both")


    # Subplot [1, 0]: Componente Imaginaria
    axs[1, 0].set_xlabel('$\omega$ (rad/s)')
    axs[1, 0].set_ylabel('-Imag(Z) ($\Omega$)')
    axs[1, 0].set_title('Parte Imaginaria vs $\omega$')
    axs[1, 0].grid(True, which="both")

    # Subplot 5: Fase vs w
    unidad_fase = '(°)' 
    axs[1, 1].set_title('Fase vs $\omega$')
    axs[1, 1].set_xlabel('$\omega$ (rad/s)')
    axs[1, 1].set_ylabel(f'Fase {unidad_fase}')
    axs[1, 1].grid(True, which="both")

    # Subplot 6 (Celda vacía [1, 2]): Limpieza de ejes
    axs[1, 2].axis('off')
        # Extraer las líneas y etiquetas del gráfico de Nyquist [0, 0]
    handles, labels = axs[0, 0].get_legend_handles_labels()

    # Dibujar la leyenda centrada en el casillero [1, 2]
    axs[1, 2].legend(handles, labels, loc='center', fontsize=11, frameon=True)

    plt.tight_layout()
    plt.show()

    return zbest_export