######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Hannes Karppinen
# Opiskelijanumero: 491936
# Päivämäärä: 26.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# ----
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T3.py
# eof

def rekursiivinenFunktio(TulostettavaSana, TulostuskertojenMaara, Tulostettu = 1):
    if TulostuskertojenMaara > 0:
        print("Sana on '" + TulostettavaSana + "',", str(Tulostettu) + ". kerta.")
        TulostuskertojenMaara = TulostuskertojenMaara - 1
        rekursiivinenFunktio(TulostettavaSana, TulostuskertojenMaara, Tulostettu + 1)
    return None

def paaohjelma():
    TulostettavaSana = input("Anna tulostettava sana: ")
    TulostuskertojenMaara = int(input("Anna tulostuskertojen määrä: "))
    rekursiivinenFunktio(TulostettavaSana, TulostuskertojenMaara)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
