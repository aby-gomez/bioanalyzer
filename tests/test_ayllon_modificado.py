import numpy as np
import pandas as pd
import pytest

from metodos.ayllon_modificado import metodo_ayllon_modificado

def test_metodo_ayllon_valores_referencia():
    # 1. Preparar los datos
    df = pd.read_excel('datos_prueba/nivel0_01ma_1.xlsx')
    datos = df[['frequency', 'real', 'imaginary']].values
    
    # 2. Valores esperados obtenidos de Octave (los que me pasaste)
    valores_esperados = np.array([
        70.43853859591113,   # Rinf
        375.6241851207319,   # R0
        0.03997763007507858, # tau
        0.7743018854329428,  # alpha
        223.0313618583215,   # x0
        56.48464847158055,   # y0
        162.7116628399797    # radio
    ])
    
    # 3. Ejecutar
    resultado = metodo_ayllon_modificado(datos, a=0, c=1)
    
    # 4. Asertar (compara con una tolerancia relativa de 1e-5)
    np.testing.assert_allclose(resultado, valores_esperados, rtol=1e-5)


def test_metodo_ayllon_falla_si_parametro_a_es_invalido():
    datos_validos = np.random.rand(10, 3)
    with pytest.raises(ValueError, match="El parámetro 'a' debe ser 0 o 1"):
        metodo_ayllon_modificado(datos_validos, a=5, c=1)

def test_metodo_ayllon_falla_si_columnas_insuficientes():
    datos_invalidos = np.random.rand(10, 2) # Solo 2 columnas
    with pytest.raises(ValueError, match="al menos 3 columnas"):
        metodo_ayllon_modificado(datos_invalidos, a=0, c=1)

def test_metodo_ayllon_falla_si_no_es_numpy_array():
    with pytest.raises(TypeError, match="debe ser un arreglo de NumPy"):
        metodo_ayllon_modificado([[1, 2, 3]], a=0, c=1)