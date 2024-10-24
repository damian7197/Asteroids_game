import pandas as pd

# Función para cargar los high scores desde el archivo CSV
def cargar_high_scores(filename):
    df = pd.read_csv(filename)  
    return list(zip(df['nombre_usuario'], df['score']))  # Crear lista de tuplas (nombre_usuario, score)

def guardar_high_scores(high_scores, filename):
    # Convertir la lista a un DataFrame de Pandas
    df = pd.DataFrame(high_scores, columns=['nombre_usuario', 'score'])
    # Ordenar los high scores en orden descendente
    df = df.sort_values(by='score', ascending=False)
    
    df = df.head(5)

    df.to_csv(filename, index=False) 

def actualizar_high_scores(nombre_usuario, nuevo_score, filename):
    high_scores = cargar_high_scores(filename)  # Cargar los high scores existentes
    high_scores.append((nombre_usuario, nuevo_score))  # Agregar el nuevo score a la lista
    guardar_high_scores(high_scores, filename)  # Guardar los scores actualizados
    
def mostrar_high_scores():
    high_scores = cargar_high_scores('high_scores.csv')  # Cargar los high scores
    print("========== High Scores ==========")
    for nombre_usuario, score in high_scores:
        print(f"{nombre_usuario}: {score}")  # Imprimir cada nombre de usuario y su score
    print("==================================")
