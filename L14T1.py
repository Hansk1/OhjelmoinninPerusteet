######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Hannes Karppinen
# Opiskelijanumero: 491936
# Päivämäärä: 18.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# ----
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T1.py

import math

def lasku(KustannuksetLista, Kilometrit, Kulutus, PolttoaineenHinta, AutonIka, Vakuutukset, Boonusprosentti, Verot):
    
    KustannuksetLista.clear()

    for i in range(5):
        VakuutustenMaara = Vakuutukset - (Vakuutukset / 100 * Boonusprosentti)
        Summa = Kilometrit  / 100 * PolttoaineenHinta * Kulutus + VakuutustenMaara + Verot + 200 * math.sqrt(AutonIka)
        KustannuksetLista.append(Summa)
        AutonIka = AutonIka + 1
    
    return KustannuksetLista



def tulostus(KustannuksetLista):
    Kierros = 1
    for i in KustannuksetLista:
        print(str(Kierros) + ". vuosi: " + str(round(i)))
        Kierros = Kierros + 1
        
    print("Viiden vuoden aikana autoon käytettiin rahaa " + str(round(sum(KustannuksetLista))) + " euroa.")
    return None



def paaohjelma():
    #Lista johon tallennetaan vuosien käyttökustannukset:
    Kayttokustannukset = []
    
    VuotuisetKilometrit = int(input("Anna vuotuiset kilometrit: "))
    PolttoaineenKulutus = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    PolttoaineenHinta = float(input("Anna polttoaineen hinta (€/l): "))
    AutonIka = int(input("Anna auton ikä vuosissa: "))
    VakuutustenMaara = int(input("Anna vakuutusten määrä (euroissa): "))
    Boonusprosentti = int(input("Anna bonusprosentti kokonaislukuna: "))
    VerojenMaara = int(input("Anna verojen määrä: "))

    #Lasketaan kustannukset ja tulostetaan ne:
    Kayttokustannukset = lasku(Kayttokustannukset, VuotuisetKilometrit, PolttoaineenKulutus, PolttoaineenHinta, AutonIka, VakuutustenMaara, Boonusprosentti, VerojenMaara)
    tulostus(Kayttokustannukset)

    Kayttokustannukset.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()