with open('volumes_copy.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)

print()

with open('volumes_copy.txt', 'a', encoding='utf-8') as archivo:
    archivo.write('\n' '¡Esto es una línea adicional!\n')

print()

with open('volumes_copy.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)

with open("volumes_copy.txt", "a", encoding='utf-8') as f:
    print("¡Hola, mundo!", file=f)

with open('volumes_copy.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)

print("¡Hola!", flush=True)

# Open a text file named cities.txt in append mode.
elevation = 45
population = 78
with open("volumes_copy.txt", "at") as cities_file:

    # Print a city's name and information to the file.
    print("Sergio Bravo", file=cities_file)
    print(f"{elevation}, {population}", file=cities_file)
