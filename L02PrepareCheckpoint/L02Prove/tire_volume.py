from datetime import datetime
import math

pi =  math.pi
date = datetime.now()

wTire = int(input("Enter the width of the tire in mm (ex 205): "))
arTire = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volumen = (pi * (wTire**2) * (arTire * ((wTire * arTire) + (d *2540))))/10000000000

print(f"The approximate volume is {volumen:.2f} liters")

with open('volumes.txt', 'at', encoding='utf-8') as archivo:
    print(f"{date:%Y-%m-%d}, {wTire}, {arTire}, {d}, {volumen:.2f}", file=archivo,  flush=False)

print()
res = input("You want to buy this tire? (ask 'yes' or 'not'): ")

# Evaluar la res
if res.lower() == "yes":
    ask = True
else:
    ask = False

# Precios de neumáticos (ejemplo)
prices = {
    (185, 60, 14): 100,
    (205, 55, 15): 120,
    (225, 50, 16): 150,
    (245, 45, 17): 180,
    (185, 50, 14): 130
}

# Usar la variable booleana según la res
if ask:
    # Buscar el precio correspondiente
    name = input("please, give me your name: ")
    tel = input("please, give me cell phone number: ")

    with open('volumes.txt', 'at', encoding='utf-8') as archivo:
        print(f'name: {name}, cell phone: {tel}', file=archivo,  flush=False)

    price = prices.get((wTire, arTire, d))
    if price is None:
        print("We do not have a price for your tire, it is likely that it is not in stock")
    else:
        print(f"${price}")
else:
    print("It seems like you don't want to buy any tires,\nso we'll be waiting for you another time.")
    print("Thanks for your visit")

print()