# Sección 6 — Historia observacional y sesgo de descubrimiento
# Responsable: Alumno 6
#
# Entrada: asteroids_clean.parquet (via data_loader.cargar_asteroides)
#
# Columnas clave:
#   first_observation_date  — fecha del primer avistamiento (datetime)
#   last_observation_date   — fecha del último avistamiento (datetime)
#   observations_used       — número de observaciones acumuladas
#   data_arc_days           — arco observacional en días
#   diameter_min_m          — diámetro mínimo estimado en metros
#   diameter_max_m          — diámetro máximo estimado en metros
#
# Columnas derivadas a construir:
#   decada_descubrimiento   — décadas del primer avistamiento (ej. 1990, 2000, …)
#   arco_anios              — data_arc_days / 365.25
#
# Funciones a implementar:
#   descubrimientos_por_decada(df) -> pd.Series
#       Cuenta cuántos asteroides fueron observados por primera vez en cada década.
#
#   resumen_por_decada(df) -> pd.DataFrame
#       Agrupa por décadad y calcula media/mediana de diámetro, observaciones y arco.
#
#   anova_diametro_por_decada(df) -> tuple[float, float]
#       Prueba ANOVA de una vía: ¿difiere el diámetro promedio entre décadas?
#       Retorna (estadístico_F, p_valor).
