"""
data_loader.py — Carga centralizada y cacheada de los datasets limpios.

Todas las páginas (pages/) y módulos (src/) deben importar desde aquí.
Nadie debe leer los archivos .parquet directamente.

Uso básico
----------
    from src.data_loader import cargar_asteroides, cargar_aproximaciones

    df  = cargar_asteroides()       # 2 000 filas × 32 columnas
    app = cargar_aproximaciones()   # ~64 000 filas × 9 columnas

Columnas principales de cada dataset
-------------------------------------
asteroids_clean (cargar_asteroides)
    id, name, short_name, designation, magnitude, potentially_hazardous,
    sentry, diameter_min_m, diameter_max_m, orbit_id,
    orbit_determination_date, first_observation_date, last_observation_date,
    data_arc_days, observations_used, orbit_uncertainty,
    min_orbit_intersection, jupiter_tisserand, epoch, eccentricity,
    semi_major_axis, inclination, ascending_node_longitude, orbital_period,
    perihelion_distance, perihelion_argument, aphelion_distance,
    perihelion_time, mean_anomaly, mean_motion, orbit_class_type

approaches_clean (cargar_aproximaciones)
    asteroid_id, asteroid_name, fecha (datetime),
    vel_km_s, vel_km_h,
    dist_au, dist_km, dist_lunar,
    orbiting_body

Dependencia
-----------
Los archivos .parquet los genera src/limpieza.py (Sección 0).
Si no existen, ejecuta primero:
    python -m src.limpieza
"""

from pathlib import Path

import pandas as pd
import streamlit as st

_BASE = Path(__file__).parent.parent / "data" / "processed"
_PATH_ASTEROIDES     = _BASE / "asteroids_clean.parquet"
_PATH_APROXIMACIONES = _BASE / "approaches_clean.parquet"


@st.cache_data
def cargar_asteroides() -> pd.DataFrame:
    """Devuelve el dataset limpio de asteroides (un asteroide por fila)."""
    return pd.read_parquet(_PATH_ASTEROIDES)


@st.cache_data
def cargar_aproximaciones() -> pd.DataFrame:
    """Devuelve la tabla de eventos de aproximación (un evento por fila)."""
    return pd.read_parquet(_PATH_APROXIMACIONES)
