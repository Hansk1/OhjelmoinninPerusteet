def tarkistus(Hetu):
    Hetu = Hetu.lower()
    
    #Luodaan lista, jossa on kaikki tarkistusmerkit:
    Tarkistusmerkit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "u", "v", "w", "x", "y"]
    
    #Otetaan henkilötunnuksesta numerot ylös, niin että niitä voidaan käyttää helposti jos ohjelmaa laajennetaan myöhemmin:
    pp = Hetu[0:2]
    kk = Hetu[2:4]
    vv = Hetu[4:6]
    TarkitstusNumero = Hetu[7:10]
    TarkistusMerkki = Hetu[10:11]
    
    #Muodostetaan tiedoista numero
    TarkistettavaNumero = int(pp+kk+vv+TarkitstusNumero)

    #Lasketaan Hetun oikea tarkistusmerkki:
    OikeaTarkistusMerkki = str(Tarkistusmerkit[(TarkistettavaNumero % 31)])

    #Tarkistetaan oliko merkki oikea:
    if OikeaTarkistusMerkki == TarkistusMerkki:
        TarkistuksenTulos = True
    else:
        TarkistuksenTulos = False    
    
    return TarkistuksenTulos

def paaohjelma():
    Hetu = input("Anna henkilötunnus: ")
    Tulos = tarkistus(Hetu)
    
    #Tulostetaan käyttäjälle hyväksyttiinkö henkilötunnus:
    if Tulos == True:
        print("Henkilötunnus hyväksytty.")
    elif Tulos == False:
        print("Henkilötunnusta ei hyväksytä.")
    
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
