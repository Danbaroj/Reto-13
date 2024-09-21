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
