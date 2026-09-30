import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    dbname="analisis_incidencias", user="postgres", password="990122", host="localhost"
)

# filtro/grafico por estado
df_estado = pd.read_sql(
    "SELECT estado, COUNT(*) as total FROM public.incidencia GROUP BY estado ORDER BY total DESC",
    conn,
)
plt.figure()
plt.bar(df_estado["estado"], df_estado["total"])
plt.title("Incidencias por Estado")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafica_estados.png")
print("Grafica 1 guardada: grafica_estados.png")

# filtro/grafica por delito
df_delito = pd.read_sql(
    "SELECT delito, COUNT(*) as total FROM public.incidencia GROUP BY delito ORDER BY total DESC",
    conn,
)
plt.figure()
plt.bar(df_delito["delito"], df_delito["total"])
plt.title("Top Delitos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafica_delitos.png")
print("Grafica 2 guardada: grafica_delitos.png")

# tendencia anual
df_anio = pd.read_sql(
    "SELECT anio, COUNT(*) as total FROM public.incidencia GROUP BY anio ORDER BY anio",
    conn,
)
plt.figure()
plt.plot(df_anio["anio"], df_anio["total"], marker="o")
plt.title("Tendencia por Año - Incidencias")
plt.tight_layout()
plt.savefig("grafica_tendencia.png")
print("Grafica 3 guardada: grafica_tendencia.png")

conn.close()
