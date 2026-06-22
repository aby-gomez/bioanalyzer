import numpy as np

def ParametersDV(best_circumference: np.ndarray, datos: np.ndarray):
    # MATLAB: x0=best_circumference(1); y0=best_circumference(2); R=best_circumference(3);
    x0 = best_circumference[0]
    y0 = best_circumference[1]
    R = best_circumference[2]
    
    # MATLAB: R0=sqrt(R*R-y0*y0)+x0;
    R0 = np.sqrt(R**2 - y0**2) + x0
    
    # MATLAB: Rinf=x0-sqrt(R*R-y0*y0);
    Rinf = x0 - np.sqrt(R**2 - y0**2)
    
    # MATLAB: alpha=(2/pi)*atan((y0/(sqrt(R*R-y0*y0))));
    alpha = (2.0 / np.pi) * np.arctan(y0 / np.sqrt(R**2 - y0**2))
    
    # MATLAB: if alpha>0 alpha=1-alpha; else alpha=1+alpha; end
    if alpha > 0:
        alpha = 1.0 - alpha
    else:
        alpha = 1.0 + alpha
        
    # MATLAB: [Ymin, pos] = min(datos(:,3)); fc=datos(pos,1);
    pos = np.argmin(datos[:, 2]) # argmin busca el índice del valor mínimo
    fc = datos[pos, 0]
    
    # MATLAB: tau=1/(2*pi*fc);
    tau = 1.0 / (2.0 * np.pi * fc)
    
    return np.array([Rinf, R0, tau, alpha])