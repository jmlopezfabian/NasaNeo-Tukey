import streamlit as st

st.set_page_config(
    page_title="Asteroides NEO — Dashboard",
    page_icon="☄️",
    layout="wide",
)

st.title("☄️ Asteroides Cercanos a la Tierra (NEOs)")
st.caption("NASA Near Earth Object Web Service · 2 000 asteroides · 6 secciones de análisis")

st.markdown(
    """
    Este dashboard es el resultado de un proyecto colaborativo de análisis de datos sobre
    **asteroides cercanos a la Tierra (NEOs)** del catálogo de la NASA.

    Usa el menú lateral para navegar entre las secciones.
    """
)

st.divider()

secciones = [
    {
        "num": "0",
        "titulo": "Limpieza y dataset base",
        "desc": (
            "Transformación del CSV crudo en dos tablas limpias: una por asteroide "
            "y otra por evento de aproximación. Base de todas las demás secciones."
        ),
        "responsable": "Jesús",
        "github": "https://github.com/jesus",
    },
    {
        "num": "1",
        "titulo": "Perfil descriptivo del catálogo",
        "desc": (
            "Estadística univariada, bivariada y multivariada. Correlaciones, outliers "
            "y perfiles comparados por clase orbital."
        ),
        "responsable": "Alumno 1",
        "github": "https://github.com/usuario1",
    },
    {
        "num": "2",
        "titulo": "¿Qué distingue a un asteroide peligroso?",
        "desc": (
            "Comparación de grupos peligroso vs. no peligroso con prueba t y chi-cuadrada. "
            "¿Son estadísticamente significativas las diferencias?"
        ),
        "responsable": "Alumno 2",
        "github": "https://github.com/usuario2",
    },
    {
        "num": "3",
        "titulo": "Predicción del tamaño a partir del brillo",
        "desc": (
            "Regresión lineal simple por fórmula cerrada vs. gradiente descendente. "
            "Efecto del escalado en la convergencia."
        ),
        "responsable": "Alumno 3",
        "github": "https://github.com/usuario3",
    },
    {
        "num": "4",
        "titulo": "Modelo multivariado del riesgo orbital (MOID)",
        "desc": (
            "Regresión OLS con statsmodels, one-hot encoding, K-Fold y diagnóstico "
            "de residuos para explicar la distancia mínima de cruce con la Tierra."
        ),
        "responsable": "Alumno 4",
        "github": "https://github.com/usuario4",
    },
    {
        "num": "5",
        "titulo": "Anatomía de los encuentros cercanos",
        "desc": (
            "Frecuencia, velocidad y distancia de los ~64 000 eventos de aproximación. "
            "Evolución temporal y relaciones entre variables."
        ),
        "responsable": "Alumno 5",
        "github": "https://github.com/usuario5",
    },
]

cols = st.columns(3)
for i, s in enumerate(secciones):
    with cols[i % 3]:
        st.markdown(
            f"**Sección {s['num']} — {s['titulo']}**  \n"
            f"{s['desc']}  \n"
            f"*Responsable:* [{s['responsable']}]({s['github']})"
        )
        st.divider()

st.caption(
    "Proyecto académico · Curso NASA NEO Analysis con Python y Streamlit · 2026"
)
