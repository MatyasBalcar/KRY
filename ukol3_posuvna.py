from pomocne import ABECEDA, nacti_volbu, preved_text


def zasifruj(text, posun):
    nova_abeceda = ""
    for i in range(26):
        nova_abeceda += ABECEDA[(i + posun) % 26]
    return preved_text(text, nova_abeceda)


def desifruj(text, posun):
    return zasifruj(text, -posun)


if __name__ == "__main__":
    volba = nacti_volbu()
    text = input("Text: ")
    posun = int(input("Posun: "))
    if volba == "s":
        print(zasifruj(text, posun))
    else:
        print(desifruj(text, posun))

