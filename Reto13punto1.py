def print_sorted_values(diccionario):
    valores = list(diccionario.values())  # Obtener los valores en una lista
    
    # Implementación del algoritmo de ordenamiento tipo burbuja
    for i in range(len(valores)):
        for j in range(0, len(valores) - i - 1):
            if valores[j] > valores[j + 1]:
                # Intercambiar si el valor actual es mayor que el siguiente
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
    
    print(valores)

# Ejemplo de uso:
diccionario = {'a': 314, 'b': 5351, 'c': 24}
print_sorted_values(diccionario)
