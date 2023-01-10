def paaohjelma():
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(tiedostonNimi, "r", encoding="utf-8")
    nimienMaara = 0
    merkkienMaara = 0
    
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        nimienMaara = nimienMaara + 1
        merkkienMaara = merkkienMaara + len(rivi)
    
    print("Tiedostossa oli " + str(nimienMaara) + " nimeä ja " + str(merkkienMaara) + " merkkiä.")
    print("Keskimäärin nimen pituus oli " + str(round((merkkienMaara - nimienMaara) / nimienMaara)) + " merkkiä.")
    print("Kiitos ohjelman käytöstä.")
    tiedosto.close()
    return None
        
        
paaohjelma()
