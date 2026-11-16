from pomocne import ABECEDA, je_pismeno, nacti_volbu, preved_text


def over_klic(klic):
    if len(klic) != 26 or not all(je_pismeno(znak) for znak in klic):
        raise ValueError("Klic musi mit 26 pismen.")
    klic = klic.upper()
    if len(set(klic)) != 26:
        raise ValueError("Unique pismena v klici.")
    return klic


def zasifruj(text, klic):
    return preved_text(text, over_klic(klic))


def desifruj(text, klic):
    klic = over_klic(klic)
    nova_abeceda = ""
    for znak in ABECEDA:
        nova_abeceda += ABECEDA[klic.index(znak)]
    return preved_text(text, nova_abeceda)


if __name__ == "__main__":
    volba = nacti_volbu()
    text = input("Text: ")
    klic = input("Prehazena abeceda : ")
    if volba == "s":
        print(zasifruj(text, klic))
    else:
        print(desifruj(text, klic))
