import requests

buscarHaki = input("¿Qué haki quieres buscar? ").lower()

URL = "https://api.api-onepiece.com/v2/hakis/en"

# Petición
respuesta = requests.get(URL)

# Convertir respuesta a JSON (lista de hakis)
hakis = respuesta.json()

# Buscar haki por nombre
for haki in hakis:
    if buscarHaki in haki["name"].lower():
        print("Nombre:", haki["name"])
        print("Descripción:", haki["description"])
        break
else:
    print("No se encontró ese Haki.")
