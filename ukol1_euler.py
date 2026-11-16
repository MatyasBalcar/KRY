def eulerova_funkce(n):
    vysledek = n
    delitel = 2
    while delitel * delitel <= n:
        if n % delitel == 0:
            vysledek -= vysledek // delitel
            while n % delitel == 0:
                n //= delitel
        delitel += 1

    if n > 1:
        vysledek -= vysledek // n
    return vysledek


if __name__ == "__main__":
    try:
        n = int(input("Zadej přirozené číslo n: "))
        print("Eulerova funkce:", eulerova_funkce(n))
    except ValueError as chyba:
        print("Chyba:", chyba)
