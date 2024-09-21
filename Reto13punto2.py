# Definir los diccionarios
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Crear un diccionario vacío para almacenar el resultado
result = {}

# Agregar todos los elementos del segundo diccionario al resultado
for key in dict2:
    result[key] = dict2[key]

# Sobrescribir o agregar las claves del primer diccionario
for key in dict1:
    result[key] = dict1[key]  # Sobrescribe si la clave ya existe

# Imprimir el diccionario resultante
print(result)
