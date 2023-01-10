def valikko():
    print("Valitse haluamasi toiminto:\n1) Anna tiedostonimet\n2) Analysoi\n3) Kirjoita tiedosto\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTiedostonNimi(kehote, aiempiNimi):
    print(kehote + " '" + aiempiNimi + "'.")
    tiedostonNimi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    return tiedostonNimi

def pieninArvo(luettavanNimi):
    tiedosto = open(luettavanNimi, "r", encoding="utf-8")
    pieninLuku = int(tiedosto.readline())
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        if int(rivi) < pieninLuku:
            pieninLuku = int(rivi)
    tiedosto.close()
    return pieninLuku

def suurinArvo(luettavanNimi):
    tiedosto = open(luettavanNimi, "r", encoding="utf-8")
    suurinLuku = int(tiedosto.readline())
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        if int(rivi) > suurinLuku:
            suurinLuku = int(rivi)
    tiedosto.close()
    return suurinLuku


def kirjoitaTiedosto(kirjoitettavaTiedosto, pieninLuku, suurinLuku):
    kirjoitettavaTiedosto.write("Analyysin tulokset ovat seuraavat:\nDatan pienin arvo on " + str(pieninLuku) + ".\n" + "Datan suurin arvo on " + str(suurinLuku) + ".")
    kirjoitettavaTiedosto.close()
    return None


def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    valinta = 1
    while (valinta != 0):
        valinta = valikko()
        if (valinta == 1):
            kehote1 = "Luettavan tiedoston nimi on"
            kehote2 = "Kirjoitettavan tiedoston nimi on"
            aiempiNimiL = ""
            aiempiNimiK = ""
            print("Anna tiedostonimet")
            luettavanNimi = kysyTiedostonNimi(kehote1, aiempiNimiL)
            aiempiNimiL = luettavanNimi
            
            kirjoitettavanNimi = kysyTiedostonNimi(kehote2, aiempiNimiK)
            aiempiNimiK = kirjoitettavanNimi
            print("")
        elif (valinta == 2):
            print("Suoritetaan analyysi")
            #tiedosto = open(luettavanNimi, "r", encoding="utf-8")
            pieninLuku = pieninArvo(luettavanNimi)
            suurinLuku = suurinArvo(luettavanNimi)
            print("")
        elif (valinta == 3):
            print("Kirjoitetaan tulokset tiedostoon")
            kirjoitettavaTiedosto = open(kirjoitettavanNimi, "w", encoding="utf-8")
            kirjoitaTiedosto(kirjoitettavaTiedosto, pieninLuku, suurinLuku)
            print("")
        elif (valinta == 0):
            print("Lopetetaan")
        else:
            print("Tuntematon valinta, yritä uudestaan.") 
            print("")
    print("\nKiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
