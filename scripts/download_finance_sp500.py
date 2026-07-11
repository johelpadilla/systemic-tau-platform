#!/usr/bin/env python3
"""
Descarga datos financieros reales (S&P 500) para el Laboratorio (Finanzas).
Enfocado en la crisis financiera global (2008).
"""
import pandas as pd
from pathlib import Path
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def main():
    out_dir = Path("data/domain_samples")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    out_file = out_dir / "finance_sp500_crash2008.csv"
    if out_file.exists():
        print(f"[Finanzas] El archivo {out_file} ya existe. Omitiendo descarga.")
        return

    print("[Finanzas] Descargando datos históricos del S&P 500...")
    
    url = "https://raw.githubusercontent.com/datasets/s-and-p-500/master/data/data.csv"
    try:
        df = pd.read_csv(url)
        # El CSV contiene 'Date', 'SP500', 'Dividend', 'Earnings', 'Consumer Price Index', 'Long Interest Rate', 'Real Price', 'Real Dividend', 'Real Earnings', 'PE10'
        # Filtramos por los años de la crisis (2006 a 2010) usando strings para evitar segfaults de datetime en ciertos entornos
        df_crisis = df[df['Date'].str.startswith('2006') | df['Date'].str.startswith('2007') | df['Date'].str.startswith('2008') | df['Date'].str.startswith('2009') | df['Date'].str.startswith('2010')].copy()

        
        # Guardamos sólo fecha y precio
        df_crisis = df_crisis[['Date', 'SP500']].rename(columns={'SP500': 'sp500_close'})
        
        df_crisis.to_csv(out_file, index=False)
        print(f"[Finanzas] Guardado exitosamente: {out_file} ({len(df_crisis)} filas)")
    except Exception as e:
        print(f"[Finanzas] Error al descargar: {e}")

if __name__ == "__main__":
    main()
