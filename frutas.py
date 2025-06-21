import requests

URL = "https://api.api-onepiece.com/v2/fruits/en"

buscarFruta = input("Que fruta estás buscando? ")

respuesta = requests.get(URL)
frutas = respuesta.json()

encontrado = False

for fruta in frutas:
    if buscarFruta.lower() in fruta["name"].lower():
        print("Fruta encontrada!")
        print("Nombre", fruta["name"])