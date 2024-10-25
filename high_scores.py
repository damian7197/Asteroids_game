import csv

# Función para cargar los high scores desde el archivo CSV
def cargar_high_scores(filename):
    high_scores = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar el encabezado
        for row in reader:
            high_scores.append((row[0], int(row[1])))  # Convertir el score a entero
    return high_scores

def guardar_high_scores(high_scores, filename):
    # Ordenar los high scores en orden descendente y tomar los primeros 5
    high_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)[:5]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['nombre_usuario', 'score'])  # Escribir el encabezado
        writer.writerows(high_scores)  # Escribir los high scores
        
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
