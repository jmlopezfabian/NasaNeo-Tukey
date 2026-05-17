# Carga centralizada y cacheada de los datasets limpios.
# Todas las páginas y módulos deben importar desde aquí; nadie lee los parquet directamente.
#
# Funciones a implementar:
#   cargar_asteroides()   -> pd.DataFrame  (asteroids_clean.parquet)
#   cargar_aproximaciones() -> pd.DataFrame  (approaches_clean.parquet)
