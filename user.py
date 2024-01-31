import json
import os

# Obtener la ruta del script actual
script_directory = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta al archivo JSON
json_path = os.path.join(script_directory, '../config.json')

def load_json():
    # Cargar datos de ciudades desde el archivo JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        dates = json.load(file)
    return dates
