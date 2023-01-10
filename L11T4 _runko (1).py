# (c) LUT 20221120 L11T4.py un
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
###########################################################################
# Ohjelma, joka etsii sopivia numeroita

import time
import sys

class TULOKSET:
    Suurempi = None
    Pienempi = None

def hakufunktio(Nimi, Luvut):
    #####################################################
    # Lisää tarvittava koodi tämän kommentin alapuolelle.


    # Lisää tarvittava koodi tämän kommentin yläpuolelle.
    #####################################################
    return Luvut

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
###########################################################################
# eof
