######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Hannes Karppinen
# Opiskelijanumero: 491936
# Päivämäärä: 9.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# ----
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L13T1.py

import sys


class DATA:
    Nimi = None
    Numero = None
    Ika = None


def kysyTiedostonNimi():
    TiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    print("")
    return TiedostonNimi


def lueTiedosto(TiedostonNimi, DataLista):
    try:
        #Putsataan lista ennen käyttöä:
        DataLista.clear()
        
        Tiedosto = open(TiedostonNimi, "r", encoding="utf-8")
        Rivi = Tiedosto.readline()[:-1]
        while (len(Rivi) > 0): 
            Data = DATA()      
            Rivi = Rivi.split(";")
            
            #Tallennetaan aikatiedot datetime oliona:
            Data.Nimi = Rivi[0]
            Data.Numero = Rivi[1]
            Data.Ika = Rivi[2]

            #Lisätään tiedot sisältävä oli luettuun listaan:
            DataLista.append(Data)
            
            #Luetaan uusi rivi:
            Rivi = Tiedosto.readline()[:-1]
        
        #Suljetaan tiedosto:
        Tiedosto.close()
        
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)
    
    print("")
    return DataLista    


def tulostaTiedot(DataLista):
    for i in DataLista:
        print(i.Nimi + " on " + str(i.Ika) + " vuotta vanha ja hänen puhelinnumero on " + i.Numero + ".")
        
    #Tulostetaan yksi tyhjä rivi loppuun
    print("")
    
    return None

def kirjoitaTiedosto(DataLista):
    Ikaraja = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))
    IkaHyvaksyttyLista = []
    
    try:
        #Avataan tiedosto:
        Tiedosto = open("tulos.txt", "w", encoding="utf-8")
        
        #Käydään listan oliot läpi ja verratan niiden ikää käyttäjän syöttämään ikärajaan:
        for i in DataLista:
            if int(i.Ika) >= Ikaraja:
                IkaHyvaksyttyLista.append(i)

        #Kirjoitetaan tiedot tiedostoon:
        Tiedosto.write("Tiedostossa on mukana " + str(len(IkaHyvaksyttyLista)) + " vähintään " + str(Ikaraja) + " vuotiasta henkilöä:\n")
        for i in IkaHyvaksyttyLista:
            Tiedosto.write(i.Nimi + ";" + i.Numero + ";" + i.Ika + "\n")

        #Suljetaan tiedosto ja tyhjennetään lista:
        IkaHyvaksyttyLista.clear()
        Tiedosto.close()
    except Exception:
        print("Tiedoston 'tulos.txt' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    print("")
    return None
