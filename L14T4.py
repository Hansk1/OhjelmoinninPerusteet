#Tuodaan kirjastot:
import random
import sys

#Alustetaan random:
random.seed(1)

def arvoLuvut(Rajat, ArvotutLuvut):
    for i in range(int(Rajat[0])):
        while True:
            Luku = random.randint(int(Rajat[1]), int(Rajat[2]))
            LukuListassa = ArvotutLuvut.count(Luku)
            if LukuListassa == 0:
                ArvotutLuvut.append(Luku)
                break
            
    return ArvotutLuvut

def kirjoitaTiedosto(TiedostonNimi, ArvotutLuvut, Rajat):
    try:
        Tiedosto = open(TiedostonNimi, "w", encoding="utf-8")
        Tiedosto.write("Arvottu " + Rajat[0] + " lukua väliltä " + Rajat[1] + "-" + Rajat[2] + ":\n")
        for i in ArvotutLuvut:
            Tiedosto.write(str(i) + "\n")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)
    return None


def paaohjelma():
    ArvotutLuvut = []
    print("Tämä ohjelma arpoo haluamasi määrän kokonaislukuja halutulta väliltä")
    print("ja kirjoittaa ne tekstitiedostoon.")
    
    #Kysytään tiedoston nimi ja arvonnan rajat:
    TiedostonNimi = input("Anna tehtävän tiedoston nimi: ")
    Rajat = input("Anna lukujen määrä, alaraja ja yläraja, esim. 7 1 37: ").split(" ")
    
    #Arvotaan luvut annettujen rajojen mukaan:
    ArvotutLuvut = arvoLuvut(Rajat, ArvotutLuvut)
    
    #Kirjoitetaan tiedosto:
    kirjoitaTiedosto(TiedostonNimi, ArvotutLuvut, Rajat)
    
    print("Tiedosto '" + TiedostonNimi + "' luotu, kiitos ohjelman käytöstä.")
    
    
    #Tyhjennetään listat:
    ArvotutLuvut.clear()
    Rajat.clear()
    return None

paaohjelma()
