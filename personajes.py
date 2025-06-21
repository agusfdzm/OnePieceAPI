import requests

URL = "https://api.api-onepiece.com/v2/characters/en"

buscarPersonaje = input("Que personaje quieres buscar? ")

respuesta = requests.get(URL + buscarPersonaje)
datos = respuesta.json()

print(datos)