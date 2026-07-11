#!/usr/bin/env python3
"""
Descarga datos reales para el Laboratorio (Epidemiología y Ecología).
"""
import pandas as pd
from pathlib import Path
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def download_ecology(out_dir: Path):
    out_file = out_dir / "eco_hudson_bay_lynx.csv"
    if out_file.exists():
        print(f"[Ecología] El archivo {out_file} ya existe. Omitiendo.")
        return
        
    print("[Ecología] Descargando dataset clásico de Lince (Hudson Bay) desde Rdatasets...")
    url = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/lynx.csv"
    try:
        df = pd.read_csv(url)
        # Formato de Rdatasets: rownames, time, value
        df = df[['time', 'value']].rename(columns={'value': 'lynx_trappings'})
        df.to_csv(out_file, index=False)
        print(f"[Ecología] Guardado exitosamente: {out_file} ({len(df)} filas)")
    except Exception as e:
        print(f"[Ecología] Error al descargar: {e}")

def download_epidemiology(out_dir: Path):
    out_file = out_dir / "epi_covid19_italy.csv"
    if out_file.exists():
        print(f"[Epidemiología] El archivo {out_file} ya existe. Omitiendo.")
        return
        
    print("[Epidemiología] Descargando datos históricos (JHU COVID-19) - Ola inicial en Italia...")
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    try:
        df = pd.read_csv(url)
        # Filtrar por Italia
        italy_data = df[df['Country/Region'] == 'Italy'].iloc[0, 4:] # Ignorar Province, Country, Lat, Long
        italy_df = pd.DataFrame({
            'date': pd.to_datetime(italy_data.index),
            'cumulative_cases': italy_data.values.astype(int)
        })
        # Calcular casos diarios (incidencia)
        italy_df['daily_cases'] = italy_df['cumulative_cases'].diff().fillna(0)
        
        # Tomar los primeros 150 días (transición de endémico a pico epidémico)
        italy_df = italy_df.head(150)
        
        italy_df.to_csv(out_file, index=False)
        print(f"[Epidemiología] Guardado exitosamente: {out_file} ({len(italy_df)} filas)")
    except Exception as e:
        print(f"[Epidemiología] Error al descargar: {e}")

def main():
    out_dir = Path("data/domain_samples")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    download_ecology(out_dir)
    download_epidemiology(out_dir)

if __name__ == "__main__":
    main()
