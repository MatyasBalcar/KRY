from pomocne import ABECEDA, nacti_volbu, preved_text
from ukol2_euklides import rozsireny_euklides


def inverze_klice(a):
    nsd, x, y = rozsireny_euklides(a % 26, 26)
    if nsd != 1:
        raise ValueError("Klic a musí být nesoudelny s 26")
    return x % 26


def zasifruj(text, a, b):
    inverze_klice(a)
    nova_abeceda = ""
    for i in range(26):
        nova_abeceda += ABECEDA[(a * i + b) % 26]
    return preved_text(text, nova_abeceda)


def desifruj(text, a, b):
    inverze = inverze_klice(a)
    nova_abeceda = ""
    for i in range(26):
        nova_abeceda += ABECEDA[(inverze * (i - b)) % 26]
    return preved_text(text, nova_abeceda)


if __name__ == "__main__":
    volba = nacti_volbu()
    text = input("Text: ")
    a = int(input("Zadej klic a: "))
    b = int(input("Zadej klic b: "))
    if volba == "s":
        print(zasifruj(text, a, b))
    else:
        print(desifruj(text, a, b))

