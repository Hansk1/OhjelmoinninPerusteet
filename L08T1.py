import math
import random

def valikko():
    print("Mitä haluat tehdä?")
    print("1) Laske absoluuttinen arvo")
    print("2) Laske kertoma")
    print("3) Laske potenssi")
    print("4) Laske neliöjuuri")
    print("5) Arvo satunnaisluku")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    #Alustetaan randint-funktio
    random.seed(1) 
    
    Valinta = 1
    while (Valinta != 0):
        Valinta = valikko()
        
        if Valinta == 1:
            Luku = float(input("Minkä luvun absoluuttinen arvo selvitetään: "))
            AbsoluuttinenArvo = round(math.fabs(Luku), 1)
            print("Luvun absoluuttinen arvo on " + str(AbsoluuttinenArvo))
            print("")
            
        elif Valinta == 2:
            Luku = int(input("Minkä luvun kertoma lasketaan: "))
            Kertoma = math.factorial(Luku)
            print("Luvun kertoma on " + str(Kertoma))
            print("")
            
        elif Valinta == 3:
            Luku = int(input("Mikä luku korotetaan potenssiin: "))
            Eksponentti = int(input("Mitä eksponenttia käytetään: "))
            Potenssi = math.pow(Luku, Eksponentti)
            print("Luku korotettuna eksponenttiin on " + str(Potenssi))
            print("")
            
        elif Valinta == 4:
            Luku = int(input("Mikä luvun neliöjuuri lasketaan: "))
            Neliojuuri = math.sqrt(Luku)
            print("Luvun neliöjuuri on " + str(Neliojuuri))
            print("")
            
        elif Valinta == 5:
            print("Arvotaan satunnaisluku, anna rajat kokonaislukuina.")
            Min = int(input("Anna minimi (otetaan mukaan): "))
            Max = int(input("Anna maksimi (otetaan mukaan): "))
            Satunnaisluku = random.randint(Min, Max)
            print("Arvottiin satunnaisluku", Satunnaisluku)
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
