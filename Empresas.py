import pandas as pd

import pandas as pd

# Configuración inicial
file_path = 'EMPRESAS_periodo_2023.csv'  # Cambiar por tu ruta real
encoding_type = 'latin-1'  # Alternativas: 'utf-8' o 'ISO-8859-1'

try:
    # Cargar solo la columna necesaria
    df = pd.read_csv(
        file_path,
        usecols=['clase'],
        sep=';',  # Delimitador es ;
        encoding=encoding_type,
        dtype={'clase': 'category'},
        on_bad_lines='warn'
    )
    
    # Limpiar y obtener actividades únicas
    actividades = df['clase'].dropna().unique()
    
    # Mostrar resultados
    print(f"\nActividades económicas únicas encontradas: {len(actividades)}\n")
    print("Ejemplos destacados:")
    for idx, act in enumerate(actividades[:10], 1):  # Primeras 10
        print(f"{idx}. {act}")
    
    # Guardar en archivo
    pd.Series(actividades).to_csv('lista_completa_actividades.csv', 
                                index=False, 
                                header=['Actividad Económica'])
    print("\nArchivo 'lista_completa_actividades.csv' generado")

except UnicodeDecodeError:
    print(f"Error de encoding. Prueba con encoding='ISO-8859-1' o 'utf-8'")