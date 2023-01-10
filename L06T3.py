

def tiedostoKirjoita(kirjoitettavaTiedosto, riviAlkuperainen, tarkistettuRivi):
    kirjoitettavaTiedosto.write(riviAlkuperainen + "----> " + tarkistettuRivi + "\n")

def tarkistaPalindromi(rivi):
    siistittyRivi = ""
    rivi = rivi[:-1]
    if (len(rivi) >= 2):
        for i in rivi:
            if (i != "#" and i.isdigit() != True):
                    if (i.isalpha() == True):
                        siistittyRivi = siistittyRivi + i.lower()
            else:
                print("Ei OK: '" + rivi + "'")
                return ""
        
        if (siistittyRivi[::-1] == siistittyRivi):    
            print("OK: '" + rivi + "'")
            return siistittyRivi
        else:
            print("Ei OK: '" + rivi + "'")
            return "" 
    else:
        print("Ei OK: '" + rivi + "'")
        return ""
            
def paaohjelma():
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    
    #Avataan ja suljetaan tiedosto, jotta se olisi varmasti tyhjä.
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, "w", encoding="utf-8")
    kirjoitettavaTiedosto.close()
    
    tiedosto = open(luettavaTiedostoNimi, "r", encoding="utf-8")
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, "w", encoding="utf-8")
    
    while True:
        riviAlkuperainen = tiedosto.readline()
        if len(riviAlkuperainen) == 0:
            break
        tarkistettuRivi = tarkistaPalindromi(riviAlkuperainen)
        if (len(tarkistettuRivi) >= 2):
            tiedostoKirjoita(kirjoitettavaTiedosto, riviAlkuperainen, tarkistettuRivi)
    kirjoitettavaTiedosto.close()  
    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
