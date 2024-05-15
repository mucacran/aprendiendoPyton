import math


def main():
    r = float(input("dame el radio: "))
    a = float(input("dame la altura: "))

    compute_storage_efficiency(r,a)



    print(f"")
    return 0

def compute_storage_efficiency(r,a):
    csa = compute_surface_area(r,a)
    return csa;

def compute_cost_efficiency():
    cv = compute_volume()
    return cv;

def compute_volume():
    return 0

def compute_surface_area():
    return 0






main()