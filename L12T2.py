def numeroidenMuuttaminen(Luku):
    Numero = 0
    for i in Luku:
        Numero = Numero * 2 + int(i)
        
    return Numero


def laskenta(Luku1, Luku2):
    Luku1Muutettu = numeroidenMuuttaminen(Luku1)
    Luku2Muutettu = numeroidenMuuttaminen(Luku2)
    
    print("Bittijonosi " + Luku1 + " on kymmenkantaisena kokonaislukuna " + str(Luku1Muutettu))
    print("Bittijonosi " + Luku2 + " on kymmenkantaisena kokonaislukuna " + str(Luku2Muutettu))
    print("Lukujen " + str(Luku1Muutettu) + " ja " + str(Luku2Muutettu) + " erotus on " + str(Luku1Muutettu - Luku2Muutettu))
    
    return None


def paaohjelma():
    Luku1 = input("Anna ensimmäinen binaariluku: ")
    Luku2 = input("Anna toinen binaariluku: ")
    
    #Laskenta aliohjelma hoitaa myös tulostuksen:
    laskenta(Luku1, Luku2)

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
