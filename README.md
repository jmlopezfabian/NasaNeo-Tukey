# Asteroides NEO — Dashboard de Análisis

Proyecto colaborativo del curso **NASA NEO Analysis con Python y Streamlit**.  
Analiza el dataset de 2 000 asteroides cercanos a la Tierra (NEOs) publicado por la NASA, desde la limpieza de datos hasta modelos de regresión, visualizaciones interactivas y un dashboard multipágina desplegado en Streamlit.

---

## Equipo y asignación de secciones

| # | Sección | Responsable | Perfil |
|---|---------|-------------|--------|
| 0 | Limpieza y construcción del dataset base | Gsu | [@Gsu](https://github.com/jmlopezfabian) |
| 1 | Perfil descriptivo y estructura del catálogo | Alumno 1 | [@usuario1](https://github.com/usuario1) |
| 2 | ¿Qué distingue a un asteroide potencialmente peligroso? | Alumno 2 | [@usuario2](https://github.com/usuario2) |
| 3 | Predicción del tamaño a partir del brillo | Alumno 3 | [@usuario3](https://github.com/usuario3) |
| 4 | Modelo multivariado del riesgo orbital (MOID) | Alumno 4 | [@usuario4](https://github.com/usuario4) |
| 5 | Anatomía de los encuentros cercanos con la Tierra | Alumno 5 | [@usuario5](https://github.com/usuario5) |

---

## Descripción de las secciones

### Sección 0 — Limpieza y construcción del dataset base
**Responsable:** Jesús · [`src/limpieza.py`](src/limpieza.py) · [`notebooks/00_limpieza.ipynb`](notebooks/00_limpieza.ipynb)

Recibe el CSV crudo (`asteroids_data.csv`) y produce dos archivos limpios que todas las demás secciones consumen:

- `asteroids_clean.parquet` — un asteroide por fila, tipos normalizados, fechas parseadas, columnas constantes eliminadas.
- `approaches_clean.parquet` — un evento de aproximación por fila, extraído de la columna anidada `close_approach_data`.

**Preguntas que responde:** ¿Qué problemas de calidad tiene el dataset crudo? ¿Cuántos eventos de aproximación reales contiene? ¿Cuál es la estructura de datos correcta para alimentar el dashboard?

**Gráficas:** porcentaje de nulos por columna; número de eventos extraídos por cuerpo orbitado.

---

### Sección 1 — Perfil descriptivo y estructura del catálogo de NEOs
**Responsable:** Alumno 1 · [`src/perfil.py`](src/perfil.py) · [`notebooks/01_perfil_descriptivo.ipynb`](notebooks/01_perfil_descriptivo.ipynb)

Caracteriza el catálogo en tres niveles: **univariado** (distribuciones de tamaño, magnitud y parámetros orbitales, detección de outliers), **bivariado** (matriz de correlación de Pearson) y **multivariado** (perfiles por clase orbital con groupby). Crea una variable derivada de categoría de tamaño (pequeño / mediano / grande por cuartiles) para segmentar el catálogo.

**Habilidades:** EDA, `describe`, `value_counts`, `groupby` multinivel, `pd.cut`, correlación de Pearson, heatmaps.

**Preguntas que responde:** ¿Cómo se distribuyen el diámetro y la magnitud, y cuáles son los asteroides atípicos? ¿Qué variables numéricas están correlacionadas? ¿Difiere el perfil orbital típico entre clases APO/AMO/ATE?

**Gráficas:** histogramas y boxplots de diámetro/magnitud; heatmap de correlación; barras del perfil promedio por clase orbital y por categoría de tamaño.

---

### Sección 2 — ¿Qué distingue a un asteroide "potencialmente peligroso"?
**Responsable:** Alumno 2 · [`src/peligrosidad.py`](src/peligrosidad.py) · [`notebooks/02_peligrosidad.ipynb`](notebooks/02_peligrosidad.ipynb)

Compara los grupos **peligroso vs. no peligroso** usando inferencia estadística para validar si las diferencias observadas son significativas: prueba t para variables numéricas (MOID, tamaño, velocidad) y chi-cuadrada para la asociación entre clase orbital y peligrosidad.

**Habilidades:** filtros booleanos, `groupby`, prueba t de Student, chi-cuadrada, visualización comparativa.

**Preguntas que responde:** ¿Difieren significativamente el MOID, el tamaño o la velocidad entre grupos? ¿Hay asociación estadística entre clase orbital y peligrosidad?

**Gráficas:** boxplots comparativos por grupo; barras agrupadas de clase orbital × peligrosidad.

---

### Sección 3 — Predicción del tamaño a partir del brillo
**Responsable:** Alumno 3 · [`src/regresion_simple.py`](src/regresion_simple.py) · [`notebooks/03_regresion_simple.ipynb`](notebooks/03_regresion_simple.ipynb)

Modela la relación log-lineal entre `magnitude` y el diámetro implementando regresión lineal simple por fórmula cerrada (ECM) y comparándola con gradiente descendente, mostrando cómo el escalado de la variable afecta la convergencia.

**Habilidades:** función de pérdida ECM, fórmula cerrada, gradiente descendente, escalado de features, NumPy.

**Preguntas que responde:** ¿Se puede predecir el diámetro a partir de la magnitud? ¿Qué tan bien ajusta el modelo? ¿Cómo cambia la convergencia con y sin escalado?

**Gráficas:** scatter `magnitude` vs `log(diámetro)` con recta ajustada; curva de pérdida por iteración.

---

### Sección 4 — Modelo multivariado del riesgo orbital (MOID)
**Responsable:** Alumno 4 · [`src/modelo_orbital.py`](src/modelo_orbital.py) · [`notebooks/04_modelo_orbital.ipynb`](notebooks/04_modelo_orbital.ipynb)

Construye un modelo de **regresión múltiple** (OLS con statsmodels) para explicar `min_orbit_intersection` a partir de la geometría orbital, con one-hot encoding de la clase orbital. Evalúa con train/test split y K-Fold; diagnostica residuos y colinealidad.

**Habilidades:** OLS statsmodels, one-hot encoding, train/test split, K-Fold, diagnóstico de supuestos OLS (residuos, colinealidad).

**Preguntas que responde:** ¿Qué características orbitales explican la distancia mínima de cruce? ¿El modelo es estable entre folds? ¿Cumple los supuestos de OLS?

**Gráficas:** gráfica de coeficientes; residuos vs valores ajustados; predicho vs real.

---

### Sección 5 — Anatomía de los encuentros cercanos con la Tierra
**Responsable:** Alumno 5 · [`src/encuentros.py`](src/encuentros.py) · [`notebooks/05_encuentros_cercanos.ipynb`](notebooks/05_encuentros_cercanos.ipynb)

Analiza la tabla `approaches_clean` producida por la Sección 0: frecuencia, velocidad relativa y distancia de paso de los encuentros, su evolución temporal (serie de tiempo por década) y la relación entre velocidad y distancia.

**Habilidades:** Pandas (`groupby`, agregaciones, fechas), NumPy, matriz de correlación, series de tiempo, scatter, heatmap.

**Preguntas que responde:** ¿Qué tan frecuentes y rápidos son los encuentros cercanos? ¿Existe relación entre velocidad relativa y distancia de paso? ¿Cómo se distribuyen a lo largo del tiempo?

**Gráficas:** serie de tiempo de encuentros por década; scatter velocidad vs distancia; heatmap de correlación.

---

## Estructura del repositorio

```
asteroides-dashboard/
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── asteroids_data.csv          # CSV original — no modificar
│   └── processed/                      # generado por la Sección 0
│       ├── asteroids_clean.parquet
│       └── approaches_clean.parquet
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py                  # carga cacheada compartida
│   ├── limpieza.py                     # Sección 0 — Jesús
│   ├── perfil.py                       # Sección 1 — Alumno 1
│   ├── peligrosidad.py                 # Sección 2 — Alumno 2
│   ├── regresion_simple.py             # Sección 3 — Alumno 3
│   ├── modelo_orbital.py               # Sección 4 — Alumno 4
│   └── encuentros.py                   # Sección 5 — Alumno 5
│
├── notebooks/
│   ├── 00_limpieza.ipynb
│   ├── 01_perfil_descriptivo.ipynb
│   ├── 02_peligrosidad.ipynb
│   ├── 03_regresion_simple.ipynb
│   ├── 04_modelo_orbital.ipynb
│   └── 05_encuentros_cercanos.ipynb
│
├── app.py                              # página de inicio del dashboard
└── pages/
    ├── 1_Perfil_Descriptivo.py
    ├── 2_Peligrosidad.py
    ├── 3_Regresion_Simple.py
    ├── 4_Modelo_Orbital.py
    └── 5_Encuentros_Cercanos.py
```

---

## Setup

```bash
# 1. Clonar el repositorio
git clone https://github.com/<org>/asteroides-dashboard.git
cd asteroides-dashboard

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Generar los datos limpios (Sección 0 debe estar completa)
python -m src.limpieza

# 4. Lanzar el dashboard
streamlit run app.py
```

---

## Flujo de trabajo con Git (Git Flow)

El proyecto usa **Git Flow**. Las ramas principales son `main` (producción) y `develop` (integración). Cada sección vive en su propia rama `feature/`.

### 1. Iniciar tu feature

```bash
# Una sola vez por máquina, si no tienes git-flow instalado:
# macOS: brew install git-flow  |  Ubuntu: sudo apt install git-flow

git flow feature start seccion-2-peligrosidad
# Equivale a: git checkout -b feature/seccion-2-peligrosidad develop
```

### 2. Trabajar y hacer commits

Haz commits **frecuentes, cortos y descriptivos**. Cada commit debe representar un único cambio lógico:

```bash
# Bien — atómico y claro
git commit -m "add prueba t de Student para MOID entre grupos"
git commit -m "add boxplot comparativo peligroso vs no peligroso"
git commit -m "fix calculo de p-value con varianzas desiguales"

# Mal — vago o demasiado grande
git commit -m "avances"
git commit -m "terminar todo"
```

**Formato recomendado:** `<verbo en infinitivo> <qué> [<dónde o por qué>]`  
Verbos útiles: `add`, `fix`, `refactor`, `remove`, `update`, `rename`.

### 3. Antes de abrir el Pull Request — sincronizar con `develop`

Antes de pedir revisión, asegúrate de que tu rama tiene los últimos cambios de `develop` para evitar conflictos en el PR:

```bash
# 1. Actualiza develop local
git checkout develop
git pull origin develop

# 2. Regresa a tu rama y fusiona develop
git checkout feature/seccion-2-peligrosidad
git merge develop

# 3. Resuelve conflictos si los hay, luego sube tu rama
git push origin feature/seccion-2-peligrosidad
```

### 4. Abrir el Pull Request

Abre el PR en GitHub apuntando de `feature/seccion-2-peligrosidad` → `develop`.  
En la descripción del PR indica qué preguntas responde tu sección y qué gráficas generaste.

---

**Regla de dependencia:** la Sección 0 debe mergearse primero, ya que genera los `.parquet` que consumen las secciones 1–5. Mientras tanto, los alumnos pueden explorar el CSV crudo en sus notebooks.

**Regla de no conflictos:** cada alumno edita únicamente:
- `src/<su_modulo>.py`
- `pages/<su_pagina>.py`
- `notebooks/<su_notebook>.ipynb`

Nadie edita `app.py`, `src/data_loader.py` ni archivos de otro compañero.

---

## Dataset

**Fuente:** [NASA Near-Earth Asteroids Dataset](https://www.kaggle.com/datasets/lion8beasttmkc/nasa-near-earth-asteroids-dataset) — `asteroids_data.csv`  
2 000 asteroides cercanos a la Tierra · 39 columnas · ~64 000 eventos de aproximación anidados.
