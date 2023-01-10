def tiedostoKirjoita(tiedostonNimi):
    tiedosto = open(tiedostonNimi, "w")
    while True:
        kirjoitettavaNimi = input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        if (len(kirjoitettavaNimi) != 0):
            tiedosto.write(kirjoitettavaNimi + "\n")
        else:
            tiedosto.close()
            break
    return None
    
def tiedostoLue(tiedostonNimi):
    print("Tiedostoon '" + tiedostonNimi + "' on tallennettu seuraavat nimet:")
    tiedosto = open(tiedostonNimi, "r")
    tuloste = tiedosto.read()
    print(tuloste, end="")
    tiedosto.close()   
    return None
        
    
def paaohjelma():
    tiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(tiedostonNimi)
    tiedostoLue(tiedostonNimi)
    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()   
