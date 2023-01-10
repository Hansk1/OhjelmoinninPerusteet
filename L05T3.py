def valikko():
    print("Valitse haluamasi toiminto:\n1) Anna merkkijono\n2) Määritä askel\n3) Tulosta merkkijono\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyMerkkijono():
    merkkijono = input("Anna merkkijono: ")
    print("")
    return merkkijono

def kysyAskel():
    askel = int(input("Anna tulostuksessa käytettävä askel: "))
    print("")
    return askel

def tulostaMerkkijono(merkkijono, askel):
    if (askel != 0):
        print(merkkijono[::askel])
        print("")
    else:
        askel = -1
        print(merkkijono)
        for i in merkkijono:
            print(merkkijono[:askel:])
            askel = askel - 1
        print("")
    return None


def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    valinta = 1
    while (valinta != 0):
        valinta = valikko()
        if (valinta == 1):
            merkkiJono = kysyMerkkijono()
        elif (valinta == 2):
            askel = kysyAskel()
        elif (valinta == 3):
            tulostaMerkkijono(merkkiJono, askel)
        elif (valinta == 0):
            print("Lopetetaan.")
        else:
            print("Tuntematon valinta, yritä uudestaan") 
    print("\nKiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
