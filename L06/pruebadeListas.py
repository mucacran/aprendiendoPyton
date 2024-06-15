from array import array


def multplos():
    n = int(input("dame un numero para hacer una lista de los primeros 10 numeros multiplos: "))
    return n

def diesnumeros(n):
    lista = []
    for i in range(1,11):
        lista.append(n*i)
    return lista

def main():
    #lista = []
    num = multplos()
    lista = diesnumeros(num)
    #hago la copia de una array
    copia = array('i',lista)

    print(lista)
    print(copia)

    for a in copia:
        print(a)

    print(f"El tipo de la variable para lista es: {type(lista)}")
    print(f"El tipo de la variable para copia es: {type(copia)}")

    names = ["jimmy", "Gus", "dari","yuli"]
    presenters = names[1:3]

    print(f"El tipo de la variable para names es: {type(names)}")

    print(names)
    print(presenters)

main()