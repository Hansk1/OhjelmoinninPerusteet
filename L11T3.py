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
