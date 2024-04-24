"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
""" 
Cuando haces ejercicio físico para fortalecer tu corazón, 
debes mantener tu frecuencia cardíaca dentro de un rango durante al menos 20 
minutos. Para encontrar ese rango, resta tu edad a 220. Esta 
diferencia es tu frecuencia cardíaca máxima por minuto. Tu corazón 
simplemente no latirá más rápido que este máximo (220 - edad). 
Cuando haga ejercicio para fortalecer su corazón, debe mantener su 
frecuencia cardíaca entre el 65% y el 85% de la frecuencia cardíaca máxima 
"""

a = int(input("Please enter your age: "))
b = 220 - a;

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {int(b * 0.65)} and {int(b * 0.85)} beats per minute.")
