def valikko():
    print("Valitse haluamasi toiminto:\n1) Syötä tiedot\n2) Laske\n3) Tulosta tulokset\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyLuku(kehote):
    luku = int(input(kehote))
    return luku

def Summa(luku1, luku2):
    summa = luku1 + luku2
    return summa

def Erotus(luku1, luku2):
    erotus = luku1 - luku2
    return erotus

def tulostaTulokset(luku1, luku2 ,summa, erotus):
    print("Tulosta tulokset")
    print("Luvut ovat " + str(luku1) + " ja " + str(luku2) + ".")
    print("Lukujen summa on " + str(summa) + " ja erotus on " + str(erotus) + ".")
    return None


def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    valinta = 1
    while (valinta != 0):
        valinta = valikko()
        if (valinta == 1):
            kehote1 = "Anna kokonaisluku 1: "
            kehote2 = "Anna kokonaisluku 2: "
            print("Syötä tiedot")
            luku1 = kysyLuku(kehote1)
            luku2 = kysyLuku(kehote2)
            print("")
        elif (valinta == 2):
            print("Laske")
            summa = Summa(luku1, luku2)
            erotus = Erotus(luku1, luku2)
            print("")
        elif (valinta == 3):
            tulostaTulokset(luku1, luku2, summa, erotus)
            print("")
        elif (valinta == 0):
            print("Lopetetaan.")
        else:
            print("Tuntematon valinta, yritä uudestaan.") 
            print("")
    print("\nKiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
