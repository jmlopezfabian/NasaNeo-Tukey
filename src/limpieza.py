"""
limpieza.py — Limpieza y construcción del dataset base.

Genera los dos archivos parquet que consumen las secciones 1–5:
  data/processed/asteroids_clean.parquet
  data/processed/approaches_clean.parquet

Uso:
    python -m src.limpieza
"""

import ast
from pathlib import Path

import pandas as pd

PATH_RAW   = Path(__file__).parent.parent / "data" / "raw" / "asteroids_data.csv"
PATH_CLEAN = Path(__file__).parent.parent / "data" / "processed" / "asteroids_clean.parquet"
PATH_APPR  = Path(__file__).parent.parent / "data" / "processed" / "approaches_clean.parquet"

_DROP_COLS = [
    "equinox",             # constante (J2000 en las 2 000 filas)
    "nasa_url",            
    "api_url",            
    "sentry_data",         # 99.85 % nulo; la columna bool `sentry` lo cubre
    "close_approach_data", # se procesa en su propia tabla
    "orbit_class_desc",    # texto libre, orbit_class_type (APO/AMO/ATE/IEO) es suficiente
    "orbit_class_range",   # texto libre, redundante con orbit_class_type
]

_DATE_COLS = [
    "orbit_determination_date",
    "first_observation_date",
    "last_observation_date",
]


def limpiar_asteroides(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Devuelve asteroids_clean: un asteroide por fila, tipos normalizados, sin nulos."""
    df = df_raw.drop(columns=_DROP_COLS).copy()
    for col in _DATE_COLS:
        df[col] = pd.to_datetime(df[col])
    df["short_name"] = df["short_name"].fillna("")
    return df


def extraer_aproximaciones(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Devuelve approaches_clean: un evento de aproximación por fila.
    Parsea close_approach_data (Python literal) y aplana cada evento.
    """
    records = []
    for _, row in df_raw.iterrows():
        for e in ast.literal_eval(row["close_approach_data"]):
            records.append({
                "asteroid_id"  : row["id"],
                "asteroid_name": row["name"],
                "fecha"        : e["close_approach_date"],
                "vel_km_s"     : float(e["relative_velocity"]["kilometers_per_second"]),
                "vel_km_h"     : float(e["relative_velocity"]["kilometers_per_hour"]),
                "dist_au"      : float(e["miss_distance"]["astronomical"]),
                "dist_km"      : float(e["miss_distance"]["kilometers"]),
                "dist_lunar"   : float(e["miss_distance"]["lunar"]),
                "orbiting_body": e["orbiting_body"],
            })
    df_appr = pd.DataFrame(records)
    df_appr["fecha"] = pd.to_datetime(df_appr["fecha"])
    return df_appr


if __name__ == "__main__":
    PATH_CLEAN.parent.mkdir(parents=True, exist_ok=True)

    print("Cargando datos crudos...")
    df_raw = pd.read_csv(PATH_RAW)

    print("Limpiando dataset de asteroides...")
    df_clean = limpiar_asteroides(df_raw)
    df_clean.to_parquet(PATH_CLEAN, index=False)
    print(f"  asteroids_clean.parquet  → {df_clean.shape[0]:,} filas × {df_clean.shape[1]} columnas")

    print("Extrayendo eventos de aproximación...")
    df_appr = extraer_aproximaciones(df_raw)
    df_appr.to_parquet(PATH_APPR, index=False)
    print(f"  approaches_clean.parquet → {df_appr.shape[0]:,} filas × {df_appr.shape[1]} columnas")

    print("\nListo. Archivos guardados en data/processed/")
