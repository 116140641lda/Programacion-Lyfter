
import json

def agregar_pokemon(archivo_json, nuevo_pokemon):
  try:
    with open(archivo_json, 'r') as f:
      datos = json.load(f)
  except FileNotFoundError:
    print(f"Error: Archivo no encontrado: {archivo_json}")
    return
  except json.JSONDecodeError:
    print(f"Error: Archivo JSON inválido: {archivo_json}")
    return

  if not isinstance(datos, list):
    print("Error: El archivo JSON no contiene un array.")
    return

  datos.append(nuevo_pokemon)

  try:
    with open(archivo_json, 'w') as f:
      json.dump(datos, f, indent=2) 
    print(f"Pokémon {new_pokemon['nombre']} agregado exitosamente al archivo {archivo_json}")
  except Exception as e:
    print(f"Error al escribir en el archivo: {e}")




def request_pokemon ():

    while True:
        name = input('ingrese el nombre del pokemon\n')
        type = input('ingrese el tipo de pokemon\n')
        base = base_pokemon()
        return {'nombre': name, 'type': type, 'base': base}
        

def base_pokemon ():
     
    HP = input('ingrese el hp del pokemon\n')
    attack = input('ingrese el ataque del pokemon\n')
    defense = input('ingrese la defensa del pokemon\n')
    sp_attack = input('ingrese el ataque sp del pokemon\n')
    sp_defense = input('ingrese la defensa sp del pokemon\n')
    speed = input('ingrese la velocidad del pokemon\n')
    return {'hp': HP, 'attack': attack, 'defense': defense, 'sp_attack': sp_attack, 'sp_defense': sp_defense, 'speed': speed}

archivo_pokemon = 'pokemones.json' 

new_pokemon = request_pokemon()

agregar_pokemon(archivo_pokemon, new_pokemon)