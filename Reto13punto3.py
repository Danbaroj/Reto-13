import json

# Ruta completa del archivo personas.json
ruta_archivo = r'C:\Users\danro\OneDrive\Documentos\Programacion\Reto_13\personas.json'

# Leer el archivo JSON desde la ruta especificada
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    personas = json.load(archivo)

# Mostrar los datos para asegurarse de que se leen correctamente
print(personas)

# Ejemplo simple para filtrar personas por deporte
deporte = input("Ingrese un deporte: ")
for usuario in personas:
    if deporte in personas[usuario]["deportes"]:
        print(f'{personas[usuario]["nombres"]} {personas[usuario]["apellidos"]}')