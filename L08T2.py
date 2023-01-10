######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Hannes Karppinen
# Opiskelijanumero: 491936
# Päivämäärä: 7.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# ----
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py
# eof

import L08T2Kirjasto as kirjasto

#Haetaan kirjastosta kirjaston versionumero ja tallennetaan se kiintoarvoksi
VERSIONUMERO = kirjasto.VERSIONUMERO

def valikko():
    print("Minkä muunnoksen haluat tehdä?")
    print("1) Anna muunnettava tilavuus")
    print("2) Muunna litra gallon'ksi")
    print("3) Muunna litra pint'ksi")
    print("4) Muunna litra cup'ksi")
    print("5) Muunna litra fluid ounce'ksi")
    print("6) Muunna gallon litroiksi")
    print("7) Muunna pint litroiksi")
    print("8) Muunna cup litroiksi")
    print("9) Muunna fluid ounce litroiksi")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta


def paaohjelma(): 
    print("Käytetään kirjaston versiota", VERSIONUMERO)
    
    Valinta = 1
    while (Valinta != 0):
        Valinta = valikko()
             
        if Valinta == 1:
            Tilavuus = float(input("Anna muunnettava tilavuus desimaalilukuna: "))
            print("")
            
        elif Valinta == 2:
            Gallonit = round(kirjasto.litra_gallon(Tilavuus), 2)
            print("Litrat muutettuina gallon'ksi:", Gallonit)
            print("")
            
        elif Valinta == 3:
            Pintit = round(kirjasto.litra_pint(Tilavuus), 2)
            print("Litrat muutettuina pint'ksi:", Pintit)
            print("")
            
        elif Valinta == 4:
            Cups = round(kirjasto.litra_cup(Tilavuus), 2)
            print("Litrat muutettuina cup'ksi:", Cups)
            print("")
            
        elif Valinta == 5:
            FO = round(kirjasto.litra_fluidOunce(Tilavuus), 2)
            print("Litrat muutettuina fluid ounce'ksi:", FO)
            print("")
        
        elif Valinta == 6:
            Litrat = round(kirjasto.gallon_litra(Tilavuus), 2)          
            print("Gallon't muutettuina litroiksi:", Litrat)
            print("")     
                    
        elif Valinta == 7:
            Litrat = round(kirjasto.pint_litra(Tilavuus), 2)          
            print("Pint't muutettuina litroiksi:", Litrat)
            print("") 
                
        elif Valinta == 8:
            Litrat = round(kirjasto.cup_litra(Tilavuus), 2)          
            print("Cup't muutettuina litroiksi:", Litrat)
            print("") 
                
        elif Valinta == 9:
            Litrat = round(kirjasto.fluidOunce_litra(Tilavuus), 2)          
            print("Fluid ounce't muutettuina litroiksi:", Litrat)
            print("")     
        
        elif Valinta == 0:
            print("Lopetetaan")
            print("")
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")
    
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
