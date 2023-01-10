PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'

def tulostaOhjeet():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.\nAnna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.\nMerkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.\nMerkkijonoissa ei osaa olla merkkiä ';'.\n")
    return None

def kysyMerkkijono(kehote):
    merkkijono = input(kehote + " merkkijono 5-15 merkkiä (enter lopettaa): ")
    return merkkijono

def tarkistaMerkkijono(merkkijono):
    if (len(merkkijono) < PITUUS_MIN):
        print("Liian lyhyt, " + str(len(merkkijono)) + " merkkiä.")
        return None
    if (len(merkkijono) > PITUUS_MAX):
        print("Liian pitkä, " + str(len(merkkijono)) + " merkkiä.")
        return None
    if (EROTIN in merkkijono):
        print("Merkkijonossa on kielletty merkki ';'.")
        return None
    else:
        return True      
    
def tulostaHyvaksytyt(hyvaksytyt):
    print("")
    print("Annoit seuraavat hyväksytyt merkkijonot:")
    print(hyvaksytyt, end="")
    return None
    
def paaohjelma():
    x = 1
    hyvaksytyt = ""
    kehote = "Anna"
    tarkistettavaMerkkijono = "x"
    tallennettuMerkkijono = ""
    
    tulostaOhjeet()
    
    tarkistettavaMerkkijono = kysyMerkkijono(kehote)
    while (len(tarkistettavaMerkkijono) != 0):
        tallennettuMerkkijono = tarkistettavaMerkkijono
        if (len(tarkistettavaMerkkijono) != 0):
            if (tarkistaMerkkijono(tarkistettavaMerkkijono) == True):
                hyvaksytyt = hyvaksytyt + tallennettuMerkkijono + "\n"
                kehote = "Anna seuraava"
            else:
                kehote = "Anna uusi"
        tarkistettavaMerkkijono = kysyMerkkijono(kehote)
    tulostaHyvaksytyt(hyvaksytyt)
    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
