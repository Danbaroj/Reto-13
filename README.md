# Reto-13
1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
```python
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

```

2. Desarrollar una funci�on que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
```python
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
```

3. Cree un programa que lea de un archivo con dicho JSON y:

- Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
- Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.
```python
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
```

4. El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:
Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.
```python
import json
import datetime

# Función para convertir de timestamp UTC a fecha legible
def convertir_fecha(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

# Ruta completa del archivo JSON (ajústala según tu ubicación)
ruta_archivo = r'C:\Users\danro\OneDrive\Documentos\Programacion\Reto_13\clima.json'

# Leer el archivo JSON desde la ruta especificada
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    clima = json.load(archivo)

# Revisar alertas de precipitación
print("Alertas de precipitación:")
for dia in clima["alertPrecip"]:
    if clima["alertPrecip"][dia] == "X":
        fecha = convertir_fecha(clima["dt"][dia])
        print(f'Alerta de precipitación en {fecha}: {clima["prcp"][dia]} mm de lluvia')

# Revisar alertas de viento
print("\nAlertas de viento:")
for dia in clima["alertVelViento"]:
    if clima["alertVelViento"][dia] == "X":
        fecha = convertir_fecha(clima["dt"][dia])
        print(f'Alerta de viento en {fecha}: {clima["velViento"][dia]} m/s')

```

5. A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
```python
import requests  # Importamos la librería para hacer peticiones a las APIs

# 1. Obtener un chiste aleatorio
print("\nChiste aleatorio:")
respuesta_chiste = requests.get("https://official-joke-api.appspot.com/random_joke")
if respuesta_chiste.status_code == 200:  # Si la solicitud fue exitosa
    chiste = respuesta_chiste.json()  # Convertimos la respuesta a formato JSON
    print(chiste)  # Imprimimos el JSON completo
    # Extraemos e imprimimos los pares clave-valor
    print("Setup:", chiste['setup'])
    print("Punchline:", chiste['punchline'])
else:
    print("Error al obtener el chiste.")

# 2. Obtener el clima de una ciudad (Necesitas tu clave de API)
api_key = "YOUR_API_KEY"  # Coloca tu propia clave de API aquí
ciudad = "London"  # Cambia a la ciudad que quieras
url_clima = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
print("\nDatos del clima:")
respuesta_clima = requests.get(url_clima)
if respuesta_clima.status_code == 200:  # Si la solicitud fue exitosa
    clima = respuesta_clima.json()  # Convertimos la respuesta a formato JSON
    print(clima)  # Imprimimos el JSON completo
    # Extraemos e imprimimos los pares clave-valor más simples
    print("Ciudad:", ciudad)
    print("Temperatura:", clima['main']['temp'], "°C")
    print("Descripción:", clima['weather'][0]['description'])
else:
    print("Error al obtener el clima.")

# 3. Obtener un hecho aleatorio sobre gatos
print("\nHecho aleatorio sobre gatos:")
respuesta_gato = requests.get("https://catfact.ninja/fact")
if respuesta_gato.status_code == 200:  # Si la solicitud fue exitosa
    gato = respuesta_gato.json()  # Convertimos la respuesta a formato JSON
    print(gato)  # Imprimimos el JSON completo
    # Extraemos e imprimimos el par clave-valor
    print("Hecho sobre gatos:", gato['fact'])
else:
    print("Error al obtener el hecho sobre gatos.")

```
