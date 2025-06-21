import requests

URL = "https://api.api-onepiece.com/v2/characters/en"

buscarPersonaje = input("Que personaje quieres buscar? ")

respuesta = requests.get(URL)
personajes = respuesta.json()

encontrado = False

for personaje in personajes:
    if buscarPersonaje.lower() in personaje["name"].lower():
        print("¡Personaje encontrado!")
        print("Nombre:", personaje["name"])
        print("Recompensa:", personaje["bounty"])

        if personaje["bounty"] == "":
            personaje["bounty"].replace("", "NS/NC")

        print("Edad", personaje["age"])
        encontrado = True
        break

if not encontrado:
    print("No se encontró ningún personaje con ese nombre.")
