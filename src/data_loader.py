from pathlib import Path

import pandas as pd
import streamlit as st

_BASE = Path(__file__).parent.parent / "data" / "processed"
_PATH_ASTEROIDES   = _BASE / "asteroids_clean.parquet"
_PATH_APROXIMACIONES = _BASE / "approaches_clean.parquet"


@st.cache_data
def cargar_asteroides() -> pd.DataFrame:
    return pd.read_parquet(_PATH_ASTEROIDES)


@st.cache_data
def cargar_aproximaciones() -> pd.DataFrame:
    return pd.read_parquet(_PATH_APROXIMACIONES)
