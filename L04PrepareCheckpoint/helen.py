def main():
    name = dameNombre()
    apellido = dameApellido()

    print(f"tu te llamas {name} {apellido}")

def dameNombre():
    name = input("dame un nombre: ")
    return name

def dameApellido():
    a = input("dame tu apellido: ")
    return a

main()