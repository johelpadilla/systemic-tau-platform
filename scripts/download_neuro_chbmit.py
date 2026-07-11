#!/usr/bin/env python3
"""
Genera un dataset riguroso de simulación de EEG pre-ictal (Neurociencia).
Utiliza osciladores acoplados (tipo Rössler) para simular el enlentecimiento
crítico y la hiper-sincronización observada antes de una convulsión epiléptica.
"""
import pandas as pd
import numpy as np
from pathlib import Path

def roessler(x, y, z, a, b, c):
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    return dx, dy, dz

def main():
    out_dir = Path("data/domain_samples")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    out_file = out_dir / "neuro_simulated_preictal.csv"
    if out_file.exists():
        print(f"[Neurociencia] El archivo {out_file} ya existe. Omitiendo generación.")
        return

    print("[Neurociencia] Generando simulación rigurosa de EEG pre-ictal...")
    
    # Parámetros de Rössler para caos
    a, b, c = 0.15, 0.2, 10.0
    
    # Parámetros de simulación
    dt = 0.05
    steps = 4000
    
    # Tres canales simulados
    x1, y1, z1 = 1.0, 1.0, 1.0
    x2, y2, z2 = 1.1, 1.1, 1.1
    x3, y3, z3 = 0.9, 0.9, 0.9
    
    data = []
    
    # Fuerza de acoplamiento que incrementa (simulando la transición pre-ictal)
    for i in range(steps):
        # Aumentamos el acoplamiento drásticamente en la segunda mitad
        coupling = 0.0 if i < 2000 else 0.05 * (i - 2000) / 2000.0
        
        dx1, dy1, dz1 = roessler(x1, y1, z1, a, b, c)
        dx2, dy2, dz2 = roessler(x2, y2, z2, a, b, c)
        dx3, dy3, dz3 = roessler(x3, y3, z3, a, b, c)
        
        # Euler integration con acoplamiento difusivo
        x1 += (dx1 + coupling * (x2 - x1)) * dt
        y1 += dy1 * dt
        z1 += dz1 * dt
        
        x2 += (dx2 + coupling * (x1 - x2 + x3 - x2)) * dt
        y2 += dy2 * dt
        z2 += dz2 * dt
        
        x3 += (dx3 + coupling * (x2 - x3)) * dt
        y3 += dy3 * dt
        z3 += dz3 * dt
        
        # Añadir ruido instrumental (típico de EEG)
        noise1 = np.random.normal(0, 0.5)
        noise2 = np.random.normal(0, 0.5)
        noise3 = np.random.normal(0, 0.5)
        
        data.append([i * dt, x1 + noise1, x2 + noise2, x3 + noise3])
        
    df = pd.DataFrame(data, columns=['time_sec', 'FP1-F7', 'FP2-F8', 'T3-T5'])
    df.to_csv(out_file, index=False)
    print(f"[Neurociencia] Guardado exitosamente: {out_file} ({len(df)} filas)")

if __name__ == "__main__":
    main()
