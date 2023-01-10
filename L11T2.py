import math

def algoritmi(KuukausienMaara):
    
    Luku1 = 0
    Luku2 = 1
    x = 0
    
    while x < KuukausienMaara:
        #Laskentaan kaksi edellistä lukua yhteen:
        UusiLuku = Luku1 + Luku2
        #Muutetaan lukujen arvot uusiksi:
        Luku1 = Luku2
        Luku2 = UusiLuku
        x = x + 1
    
    return Luku2


def paaohjelma():
    KuukausienMaara = int(input("Anna kuukausien lukumäärä: "))
    PariskuntienMaara = algoritmi(KuukausienMaara)
    print("Kanipariskuntia on", KuukausienMaara, "kuukauden kuluttua", PariskuntienMaara)
    print("Kiitos ohjelman käytöstä.")
    return None
    
    
paaohjelma()
