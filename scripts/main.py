import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, '..')

from metodos.ayllon_modificado import metodo_ayllon_modificado
from metodos.ayllon import metodo_ayllon
from metodos.graficas import graficar_resultados
from metodos.todos_los_puntos import TodosLosPuntos
from metodos.fourgraficas import generar_fourgraficas
from metodos.lm_method import LMMethod

from metodos.multiples_graficas import comparar_sets_de_datos

# Configuración por defecto
PARAMETRO_A = 0  # 0: real/imag, 1: mod/fase
PARAMETRO_C = 1  # 0: rad/s,     1: Hz


def cargar_datos_excel(ruta_custom=None):
    if ruta_custom:
        ruta = ruta_custom
    else:
        ruta_defecto = 'datos_prueba/nivel0_01ma_1.xlsx'
        print("\n--- CARGA DE ARCHIVO DE DATOS ---")
        ruta = input(f"Ingrese la ruta del archivo Excel [{ruta_defecto}]: ").strip()
        if not ruta:
            ruta = ruta_defecto

    if not os.path.exists(ruta):
        print(f"[ERROR] El archivo '{ruta}' no existe. Se usará la ruta por defecto.")
        return None

    try:
        df = pd.read_excel(ruta)
        # Adaptación de columnas en caso de nombres en mayúsculas o minúsculas
        cols = [c.lower() for c in df.columns]
        df.columns = cols

        columnas_requeridas = ['frequency', 'real', 'imaginary', 'magnitude', 'phase']
        datos = df[columnas_requeridas].values
        print(f"\n[OK] Archivo cargado correctamente ({datos.shape[0]} filas).")
        return datos
    except Exception as e:
        print(f"[ERROR] No se pudo procesar el archivo Excel: {e}")
        return None


def imprimir_metricas(nombre, res_7p):
    print(f"\n==========================================")
    print(f" RESULTADOS: {nombre.upper()}")
    print(f"==========================================")
    print(f"  Rinf  : {res_7p[0]:.4f} Ω")
    print(f"  R0    : {res_7p[1]:.4f} Ω")
    print(f"  tau   : {res_7p[2]:.4e} s")
    print(f"  alpha : {res_7p[3]:.4f}")
    print(f"  x0    : {res_7p[4]:.4f}")
    print(f"  y0    : {res_7p[5]:.4f}")
    print(f"  radio : {res_7p[6]:.4f}")
    print(f"==========================================")


def ejecutar_metodo_individual(opcion, datos):
    if opcion == '1':
        nombre = 'Todos los Puntos'
        raw = TodosLosPuntos(datos)
        # Unificación de estructura a 7 elementos: [Rinf, R0, tau, alpha, x0, y0, radio]
        res_7p = [raw[0], raw[1], raw[2], raw[3], raw[4][0], raw[4][1], raw[4][2]]
        return nombre, res_7p, raw

    elif opcion == '2':
        nombre = 'Ayllon Original'
        res_7p = metodo_ayllon(datos, a=PARAMETRO_A, c=PARAMETRO_C)
        return nombre, res_7p, res_7p

    elif opcion == '3':
        nombre = 'Ayllon Modificado'
        res_7p = metodo_ayllon_modificado(datos, a=PARAMETRO_A, c=PARAMETRO_C)
        return nombre, res_7p, res_7p

    elif opcion == '4':
        nombre = 'Levenberg-Marquardt'
        res_7p = LMMethod(datos)
        return nombre, res_7p, res_7p

    return None, None, None

def ejecutar_comparacion_multiset():
    dict_datasets = {}
    print("\n--- MODO COMPARATIVO MULTI-SET (HOLD ON) ---")
    print("Ingrese la ruta de cada archivo Excel. Presione ENTER para finalizar la carga.\n")

    contador = 1
    while True:
        ruta = input(f"Ruta archivo #{contador}: ").strip()
        if not ruta:
            break

        datos_set = cargar_datos_excel(ruta_custom=ruta)
        if datos_set is not None:
            nombre_archivo = os.path.basename(ruta)
            
            # Ejecutar ajuste Levenberg-Marquardt para este set
            _, res_7p, _ = ejecutar_metodo_individual('4', datos_set)
            
            dict_datasets[nombre_archivo] = {
                'datos': datos_set,
                'metodos': {'Levenberg-Marquardt': res_7p}
            }
            contador += 1

    if dict_datasets:
        print(f"\nGenerando ventana gráfica con {len(dict_datasets)} conjuntos superpuestos...")
        comparar_sets_de_datos(dict_datasets, c=PARAMETRO_C)
    else:
        print("[!] No se cargó ningún conjunto de datos válido.")

def main():
    datos = cargar_datos_excel()
    if datos is None:
        return

    while True:
        print("\n" + "=" * 45)
        print("    SISTEMA DE BIOIMPEDANCIA - COLE-COLE")
        print("=" * 45)
        print("1. Todos los Puntos")
        print("2. Ayllón Original")
        print("3. Ayllón Modificado")
        print("4. Levenberg-Marquardt (LM)")
        print("5. Comparativa Global (Ejecutar todos y mostrar 5 gráficas)")
        print("6. Cambiar archivo de datos Excel")
        print("7. Comparar múltiples archivos de datos ")
        print("0. Salir")
        print("-" * 45)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '0':
            print("\nFinalizando programa.")
            break

        elif opcion in ['1', '2', '3', '4']:
            nombre, res_7p, raw = ejecutar_metodo_individual(opcion, datos)
            imprimir_metricas(nombre, res_7p)
            
            graficar_resultados(nombre, datos, raw, parametro_c=PARAMETRO_C)

            ver_5 = input("\n¿Desea ver también la comparativa de 5 gráficas con los demás métodos? (s/n): ").strip().lower()
            if ver_5 == 's':
                print("\nEjecutando restode métodos para generar comparativa global...")
                dict_metodos = {}
                for op in ['1', '2', '3', '4']:
                    n, r_7p, _ = ejecutar_metodo_individual(op, datos)
                    dict_metodos[n] = r_7p
                generar_fourgraficas(datos, dict_metodos, c=PARAMETRO_C)

        elif opcion == '5':
            print("\nEjecutando todos los métodos...")
            dict_metodos = {}
            for op in ['1', '2', '3', '4']:
                n, r_7p, _ = ejecutar_metodo_individual(op, datos)
                imprimir_metricas(n, r_7p)
                dict_metodos[n] = r_7p

            print("\nGenerando lienzo de 5 gráficas...")
            generar_fourgraficas(datos, dict_metodos, c=PARAMETRO_C)

        elif opcion == '6':
            nuevos_datos = cargar_datos_excel()
            if nuevos_datos is not None:
                datos = nuevos_datos

        elif opcion == '7':
            ejecutar_comparacion_multiset()

        else:
            print("\n[!] Opción inválida. Intente de nuevo.")


if __name__ == '__main__':
    main()