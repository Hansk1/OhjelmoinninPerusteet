def tulostaOhjeet ():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna nimesi kahdessa osassa.")
    return None
    
def kysyNimi (x):
    print("Tämä aliohjelma kysyy nimen.")
    nimi = input("Anna " + x + "nimi: ")
    return nimi
    
def tulostaTulokset (etuNimi, sukuNimi):
    print("Tämä aliohjelma tulostaa nimesi.")
    print("Hei", etuNimi, sukuNimi)
    return None
    
def paaohjelma ():
    tulostaOhjeet()
    x = "etu"
    etuNimi = kysyNimi(x)
    x = "Suku"
    sukuNimi = kysyNimi(x)
    tulostaTulokset(etuNimi, sukuNimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    