import numpy as np

def CalcularErrorDV(nueva_circunferencia: np.ndarray, datos: np.ndarray) -> np.ndarray:
    # MATLAB: N=size(datos,1);
    N = datos.shape[0]
    
    # MATLAB: centro(1)=nueva_circunferencia(1); ... radio=nueva_circunferencia(3);
    centro_x = nueva_circunferencia[0]
    centro_y = nueva_circunferencia[1]
    radio = nueva_circunferencia[2]
    
    # MATLAB: dist_x= datos(:,2)-centro(1); dist_y= datos(:,3)-centro(2);
    dist_x = datos[:, 1] - centro_x
    dist_y = datos[:, 2] - centro_y
    
    # MATLAB: distancia=sqrt(dist_x.*dist_x+dist_y.*dist_y);
    distancia = np.sqrt(dist_x**2 + dist_y**2)
    
    # MATLAB: diferencia=abs(distancia-radio); diferencia_normal=...
    diferencia = np.abs(distancia - radio)
    diferencia_normal = np.abs((distancia - radio) / radio)
    
    # MATLAB: E1=(1/N)*sum(sqrt(diferencia));
    E1 = (1.0 / N) * np.sum(np.sqrt(diferencia))
    E2_normal = (1.0 / N) * np.sum(np.sqrt(diferencia_normal))
    
    # MATLAB: ErroresDV=[E1 E2_normal], deuvelve par de errores calculados
    return np.array([E1, E2_normal])