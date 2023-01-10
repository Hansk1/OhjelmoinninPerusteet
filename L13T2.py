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
# Tehtävä L13T2.py

import sys

#Lista parillisille luvuille:
ParillisetLuvut = []

#Etsitään parilliset luvut:
for i in sys.argv[1:]:
    if ((int(i) % 2) == 0):
        ParillisetLuvut.append(int(i))

#Tulostetaan käyttäjälle tiedot:
print("Syötteen parilliset luvut ovat seuraavat:")

for i in ParillisetLuvut:
    print(i, end=" ")
Keskiarvo = sum(ParillisetLuvut) / len(ParillisetLuvut)
print("\nLukujen keskiarvo on {:0.2f}." .format(Keskiarvo))
print("Kiitos ohjelman käytöstä.")
