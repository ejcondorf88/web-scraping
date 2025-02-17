import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import unicodedata

# Cargar datos
carreras = pd.read_csv("Carreras_Unicas.csv")
actividades = pd.read_csv("lista_completa_actividades.csv")

# Preprocesamiento de texto
def preprocess(text):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8').lower()
    return ''.join([c for c in text if c.isalnum() or c in ' -_,'])

# Generar embeddings
model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
carrera_embeddings = model.encode([preprocess(c) for c in carreras['Carrera']])
actividad_embeddings = model.encode([preprocess(a) for a in actividades['Actividad Económica']])

# Asociar por similitud semántica
asociaciones = []
for i, carrera in enumerate(carreras['Carrera']):
    similitudes = cosine_similarity([carrera_embeddings[i]], actividad_embeddings)[0]
    top_5_indices = similitudes.argsort()[-5:][::-1]
    top_actividades = actividades.iloc[top_5_indices]['Actividad Económica'].tolist()
    asociaciones.append({
        'Universidad': carreras.iloc[i]['Universidad'],
        'Carrera': carrera,
        'Actividades_Asociadas': top_actividades
    })

# Crear DataFrame y exportar
df_resultado = pd.DataFrame(asociaciones)
df_resultado.to_csv("asociaciones_carreras_actividades.csv", index=False, sep=';')