from pomocne import ABECEDA, je_pismeno, nacti_volbu


def preved(text, klic, smer):
    if not klic or not all(je_pismeno(znak) for znak in klic):
        raise ValueError("klic nesmi byt prazdny a musi byt a-z.")
    klic = klic.upper()
    vysledek = ""
    poradi = 0

    for znak in text:
        if je_pismeno(znak):
            pozice = ABECEDA.index(znak.upper())
            posun = ABECEDA.index(klic[poradi % len(klic)])
            novy_znak = ABECEDA[(pozice + smer * posun) % 26]
            if znak.islower():
                novy_znak = novy_znak.lower()
            vysledek += novy_znak
            poradi += 1
        else:
            vysledek += znak
    return vysledek


def zasifruj(text, klic):
    return preved(text, klic, 1)


def desifruj(text, klic):
    return preved(text, klic, -1)


if __name__ == "__main__":
    volba = nacti_volbu()
    text = input("Zadej text: ")
    klic = input("Zadej klíčové slovo: ")
    if volba == "s":
        print(zasifruj(text, klic))
    else:
        print(desifruj(text, klic))
