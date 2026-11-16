def rozsireny_euklides(a, b):
    if a < 0 or b < 0 or (a == 0 and b == 0):
        raise ValueError("Alespon jedno cislo kladne.")
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        podil = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - podil * x1
        y0, y1 = y1, y0 - podil * y1

    return a, x0, y0


if __name__ == "__main__":
    a = int(input("Zadej a: "))
    b = int(input("Zadej b: "))
    nsd, x, y = rozsireny_euklides(a, b)
    print("NSD:", nsd)
    print("Koef: x =", x, ", y =", y)
    print(f"Bezout: {a} * ({x}) + {b} * ({y}) = {nsd}")

