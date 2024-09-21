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
