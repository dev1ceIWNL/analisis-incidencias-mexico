import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="analisis_incidencias", user="postgres", password="990122", host="localhost"
)

query = """
SELECT estado, delito, anio, COUNT(*) as total
FROM public.incidencia
GROUP BY estado, delito, anio
ORDER BY total DESC
"""

df = pd.read_sql(query, conn)
df.to_excel("Reporte_Final_Incidencias.xlsx", index=False)

print(f"Reporte creado con {len(df)} filas")
print(df.head(10))
print("\nINSIGHTS FINALES:")
print(f"1. Estado con más casos: {df.groupby('estado')['total'].sum().idxmax()}")
print(f"2. Delito más frecuente: {df.groupby('delito')['total'].sum().idxmax()}")

conn.close()
