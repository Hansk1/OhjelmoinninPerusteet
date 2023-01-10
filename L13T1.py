import L13T1Kirjasto as kirjasto

def valikko():
    print("1) Anna tiedoston nimi")
    print("2) Lue tiedosto")
    print("3) Tulosta tiedot")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    DataLista = []
    
    Valinta = 1
    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    while (Valinta != 0):
        Valinta = valikko()
        
        if Valinta == 1:
            TiedostonNimi = kirjasto.kysyTiedostonNimi()
            
        elif Valinta == 2:
            DataLista = kirjasto.lueTiedosto(TiedostonNimi, DataLista)
            
        elif Valinta == 3:
            kirjasto.tulostaTiedot(DataLista)
            
        elif Valinta == 4:
            kirjasto.kirjoitaTiedosto(DataLista)
  
        elif Valinta == 0:
            print("Lopetetaan.")
            print("")
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")
    
    print("Kiitos ohjelman käytöstä.")
    return None
        
paaohjelma()
