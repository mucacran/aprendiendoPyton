from datetime import datetime

current_date_and_time = datetime.now()

#obtengo el dia en numero
day = current_date_and_time.weekday()
#day = 1

#variables
tax = 0.06
des = 0.10
salItem = float(input("Please enter the subtotal: "))



if((day == 1 or day == 2) and  salItem >= 50):
    tDes = salItem * des
    print(f"Discount amount:{tDes:.2f}")
    t = salItem - tDes
    print(f"Sales tax amount:{(t*tax):.2f}")
    print(f"Total::{t + (t*tax):.2f}")
else:
    print(f"Sales tax amount:{(salItem * tax):.2f}")
    print(f"Total::{(salItem + (salItem * tax)):.2f}")



