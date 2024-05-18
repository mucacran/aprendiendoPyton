import math


def main():
    lista = [
    {"name": "#1 picnic", "r": 6.83, "a": 10.16},
    {"name": "#1 alto", "r": 7.78, "a": 11.91},
    {"name": "#2", "r": 8.73, "a": 11.59},
    {"name": "#2.5", "r": 10.32, "a": 11.91},
    {"name": "#3 Cylinder", "r": 10.79, "a": 17.78},
    {"name": "#5", "r": 13.02, "a": 14.29},
    {"name": "#6Z", "r": 5.40, "a": 8.89},
    {"name": "#8Z short", "r": 6.83, "a": 7.62},
    {"name": "#10", "r": 15.72, "a": 17.78},
    {"name": "#211", "r": 6.83, "a": 12.38},
    {"name": "#300", "r": 7.62, "a": 11.27},
    {"name": "#303", "r": 8.10, "a": 11.11}
]

    for l in lista:
        print(f"{l['name']} {compute_storage_efficiency(l["r"],l["a"]):.2f}")

def compute_storage_efficiency(r,a):
    eficiencia_almacenamiento = compute_volume(r,a) / compute_surface_area(r,a)
    return eficiencia_almacenamiento

def compute_cost_efficiency(r,a):
    cv = compute_volume(r,a)
    return cv


def compute_volume(r,a):
    volume = math.pi * r**2 * a
    return volume

def compute_surface_area(r,a):
    surf_area = 2 * math.pi * r * (r + a)
    return surf_area

"""
def compute_volume(r,a):
    compute_volume = math.pi * r**2 * a
    return compute_volume

def compute_surface_area(r,a):
    compute_surface_area = 2 * math.pi * (r + a)
    return compute_surface_area
"""
main()