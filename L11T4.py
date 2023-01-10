import time
import sys

class TULOKSET:
    Suurempi = None
    Pienempi = None

def hakufunktio(Nimi, Luvut):
    try:
        #Avataan tiedosto:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        
        #Luodaan lista johon luvut tallennetaan:
        LukuLista = []

        #Kerätään luvut listaan:
        Rivi = Tiedosto.readline()[:-1]
        while (len(Rivi) > 0):
            LukuLista.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        
        #Sulejetaan tiedosto lukemisen jälkeen:
        Tiedosto.close()
        
        #Otetaan lsitan pituus ylös, josta saadaan tietää iteraatioiden mahdollinen maksimimäärä:
        Maksimaara = len(LukuLista)
        
        #Luodaan muuttuja mihinkä tallennetaan iteraatioiden määrä:
        Iteraatiot = 0
        
        #Otetaan listan ensimmäinen luku ja verrataan muut luvut siihen
        VerrattavaLuku = LukuLista[0]
        
        #Kerrotaan verrattavaluku tässä vaiheessa kolmella, jotta sitä ei tarvitsisi kertoa jokaisessa iteraatiossa uudestaan:
        VerrattavaLukuKerrottu = int(VerrattavaLuku) * 3
        

        Luvut = TULOKSET()
        while True:
            for i in range(len(LukuLista)):
                i = LukuLista[i]
                if VerrattavaLukuKerrottu < int(i):
                    Luvut.Suurempi = i
                    Luvut.Pienempi = VerrattavaLuku
                    return Luvut

            #Siiretää listan ensimmäinen numero listan viimeiseksi numeroksi jä käydään lista läpi:
            LukuLista = LukuLista + [LukuLista.pop(0)]
            #Lisätää iteraatioiden määrään yksi:
            Iteraatiot = Iteraatiot + 1
            
            #Otetaan uusi luku mihinkä verrataan:
            VerrattavaLuku = LukuLista[0]
            VerrattavaLukuKerrottu = int(VerrattavaLuku) * 3
            
            #Tarkistetaan onko kaikki mahdolliset parit käyty läpi:
            if Iteraatiot == Maksimaara:
                break
        
        return Luvut
        
        
        
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)

def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = TULOKSET()
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if ((Tulokset.Suurempi == None) and (Tulokset.Pienempi == None)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulokset.Pienempi, "ja", Tulokset.Suurempi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
