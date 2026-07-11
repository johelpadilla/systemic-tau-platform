import numpy as np
from scipy.signal import correlate

def estimate_optimal_delay(X: np.ndarray, max_delay: int = 100) -> int:
    """
    Estima el retraso óptimo (delay/tau) usando el primer cruce por cero
    de la función de autocorrelación, o el primer mínimo local rápido.
    Para series multidimensionales, promedia el retraso de cada dimensión.
    """
    if X.ndim == 1:
        X = X.reshape(-1, 1)
        
    N, D = X.shape
    delays = []
    
    for d in range(D):
        series = X[:, d]
        series = series - np.mean(series)
        
        # Calcular autocorrelación
        autocorr = correlate(series, series, mode='full')
        autocorr = autocorr[len(autocorr)//2:] # Tomar mitad derecha
        if autocorr[0] > 1e-12:
            autocorr = autocorr / autocorr[0] # Normalizar
        else:
            autocorr = np.zeros_like(autocorr)
        
        optimal_delay = 1
        for i in range(1, min(len(autocorr)-1, max_delay)):
            # Criterio: Primer cruce por cero o caída por debajo de 1/e (~0.36)
            if autocorr[i] <= 0 or autocorr[i] < np.exp(-1):
                optimal_delay = i
                break
        delays.append(optimal_delay)
        
    # Usar la mediana de los delays encontrados (limitado a max_delay)
    final_delay = int(np.median(delays))
    return max(1, min(final_delay, max_delay))

def estimate_optimal_m(X: np.ndarray) -> int:
    """
    Heurística rápida para la dimensión de inmersión (m).
    En lugar de False Nearest Neighbors (que es O(N^2) y lento en Python),
    usamos una heurística basada en el teorema de Takens.
    """
    # Takens: m >= 2D + 1 (donde D es la dimensión del atractor subyacente).
    # Como heurística rápida, devolvems 3 o 4 basados en la varianza o como
    # estándar de la literatura fisiológica (que suele ser 3).
    
    return 3

def auto_tune_params(X: np.ndarray) -> dict:
    """
    Genera un diccionario con los parámetros auto-sintonizados.
    """
    delay = estimate_optimal_delay(X)
    m = estimate_optimal_m(X)
    
    # Para el tamaño de ventana de los ordinal patterns, 
    # la teoría sugiere que (m!) debe ser << N para tener buena estadística.
    # Usamos un tamaño de ventana estándar de 100 o 200, a menos que la serie sea pequeña.
    window = min(len(X) // 2, 200)
    
    return {
        "stride": delay,
        "m": m,
        "window": window
    }
