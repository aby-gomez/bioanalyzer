import numpy as np
import matplotlib.pyplot as plt

def comparar_sets_de_datos(dict_datasets: dict, c: int = 1):
    """
    Superpone múltiples sets de datos experimentales (y sus curvas ajustadas)
    en una misma ventana/figura (comportamiento tipo 'hold on' de MATLAB).
    
    Parámetros:
    -----------
    dict_datasets : dict
        Estructura con los datos y métodos calculados por cada archivo:
        {
          'Muestra_1': {'datos': datos_array, 'metodos': {'Levenberg-Marquardt': params, ...}},
          'Muestra_2': {'datos': datos_array, 'metodos': {'Levenberg-Marquardt': params, ...}}
        }
    c : int
        0 = rad/s, 1 = Hz
    """
    # 1. Crear el lienzo de subplots UNA SOLA VEZ fuera del bucle
    fig, axs = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle("Superposición de Múltiples Sets de Datos (Hold On)", fontsize=14, fontweight='bold')

    j = 1j
    estilos_linea = ['-', '--', '-.', ':']
    colores = ['r', 'g', 'b', 'm', 'c', 'y', 'k']

    # Bucle que itera sobre cada SET de datos cargado
    for idx_set, (nombre_set, contenido) in enumerate(dict_datasets.items()):
        datos = contenido['datos']
        resultados_metodos = contenido['metodos']

        frecuencias = datos[:, 0]
        X_exp = datos[:, 1]
        Y_exp = datos[:, 2]
        fase_exp = np.radians(datos[:, 4])
        fase_exp_pos = 2 * np.pi + fase_exp
        w = frecuencias * (2 * np.pi) if c == 1 else frecuencias

        color = colores[idx_set % len(colores)]
        estilo = estilos_linea[idx_set % len(estilos_linea)]

        # Graficar Puntos Experimentales del Set actual
        axs[0, 0].plot(X_exp, -Y_exp, 'o', color=color, label=f'Exp: {nombre_set}')
        axs[0, 1].semilogx(w, np.sqrt(X_exp**2 + Y_exp**2), 'o', color=color)
        axs[0, 2].semilogx(w, X_exp, 'o', color=color)
        axs[1, 0].semilogx(w, -Y_exp, 'o', color=color)
        axs[1, 1].semilogx(w, fase_exp_pos, 'o', color=color)

        # Superponer las curvas ajustadas teóricas del Set actual
        for nombre_metodo, params in resultados_metodos.items():
            Rinf, R0, tau, alpha = params[0], params[1], params[2], params[3]
            Z_est = Rinf + (R0 - Rinf) / (1 + (j * w * tau) ** alpha)

            EstX = Z_est.real
            EstY = Z_est.imag
            mod_Zest = np.abs(Z_est)
            fase_est_rad = np.arctan2(EstY, EstX)
            fase_est_pos = 2 * np.pi + fase_est_rad

            # Superponer curva en el mismo eje (acumula trazos)
            lbl = f'{nombre_set} ({nombre_metodo})'
            axs[0, 0].plot(EstX, -EstY, color=color, linestyle=estilo, label=lbl)
            axs[0, 1].semilogx(w, mod_Zest, color=color, linestyle=estilo)
            axs[0, 2].semilogx(w, EstX, color=color, linestyle=estilo)
            axs[1, 0].semilogx(w, -EstY, color=color, linestyle=estilo)
            axs[1, 1].semilogx(w, fase_est_pos, color=color, linestyle=estilo)

    # Configuración estética de ejes y grillas (se aplica al final)
    titulos = ['Nyquist', '|Z| (ω)', 'R (ω)', '-X (ω)', r'$\Theta$ (ω)']
    ejes_x = ['R ($\Omega$)', '$\omega$ (rad/s)', '$\omega$ (rad/s)', '$\omega$ (rad/s)', '$\omega$ (rad/s)']
    ejes_y = ['-X ($\Omega$)', '|Z| ($\Omega$)', 'Real(Z) ($\Omega$)', '-Imag(Z) ($\Omega$)', 'Fase (rad)']

    coords = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
    for (i, k), t, ex, ey in zip(coords, titulos, ejes_x, ejes_y):
        axs[i, k].set_title(t)
        axs[i, k].set_xlabel(ex)
        axs[i, k].set_ylabel(ey)
        axs[i, k].grid(True, which="both")

    axs[1, 2].axis('off')
    handles, labels = axs[0, 0].get_legend_handles_labels()
    axs[1, 2].legend(handles, labels, loc='center', fontsize=9, frameon=True)

    plt.tight_layout()
    plt.show()  # Se renderiza la ventana al final tras acumular todos los datos