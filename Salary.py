import pandas as pd
import ast  # Para convertir strings a listas

# Cargar los datos
df_carreras_actividades = pd.read_csv("asociaciones_carreras_actividades.csv", sep=";")  # Especificar separador
df_empresas = pd.read_csv("EMPRESAS_periodo_2023.csv", sep=";", encoding="latin-1")

# Convertir columnas numéricas
cols_numericas = ["remuneraciones", "plazas_equiv", "plazas_equiv_hombres", "plazas_equiv_mujeres"]
for col in cols_numericas:
    df_empresas[col] = pd.to_numeric(df_empresas[col].str.replace(",", "."), errors="coerce")

# Filtrar filas con plazas_equiv válidas
df_empresas = df_empresas[df_empresas["plazas_equiv"].notna() & (df_empresas["plazas_equiv"] > 0)]

# Convertir la columna "Actividades_Asociadas" de string a lista
df_carreras_actividades["Actividades_Asociadas"] = df_carreras_actividades["Actividades_Asociadas"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Explotar las listas de actividades en filas separadas
df_exploded = df_carreras_actividades.explode("Actividades_Asociadas")

# Limpiar y estandarizar nombres de actividades
def limpiar_actividad(texto):
    return (
        texto.strip().lower()
        .replace(",", "")
        .replace("ó", "o")
        .replace("í", "i")
        .replace("Ã¡", "a")
        .replace("Ã©", "e")
        .replace("Ã\xad", "i")
        .replace("Ã³", "o")
        .replace("Ãº", "u")
    )

df_exploded["Actividad_Limpia"] = df_exploded["Actividades_Asociadas"].apply(limpiar_actividad)

# Cargar datos de empresas
df_empresas["Actividad_Limpia"] = df_empresas["clase"].apply(limpiar_actividad)

# Fusionar datos
df_completo = pd.merge(
    df_exploded,
    df_empresas,
    on="Actividad_Limpia",
    how="left"
)

# Calcular estadísticas por carrera
df_completo["salario_mensual"] = (df_completo["remuneraciones"] / 12) / df_completo["plazas_equiv"]
df_completo["%_hombres"] = (df_completo["plazas_equiv_hombres"] / df_completo["plazas_equiv"]) * 100
df_completo["%_mujeres"] = (df_completo["plazas_equiv_mujeres"] / df_completo["plazas_equiv"]) * 100

# Agrupar por carrera
df_final = df_completo.groupby("Carrera").agg(
    salario_promedio=("salario_mensual", "mean"),
    porcentaje_hombres=("%_hombres", "mean"),
    porcentaje_mujeres=("%_mujeres", "mean"),
    total_empresas=("id_empresa", "nunique")
).reset_index()

# Exportar resultados
df_final.to_csv("carreras_salarios_genero.csv", index=False)