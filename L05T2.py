from traceback import print_tb


def tulostaOhjeet ():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.\nOhjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi\nlukujen lukumäärän.")
    print("")
    return None

def kysyLuku (kehote):
    luku = int(input(kehote))
    return luku

def vertaileLukuja (luku1, luku2):
    if luku1 > luku2:
        return luku2
    else:
        return luku1
    
def tulostaTiedot (pienempiLuku):      
    print("Annetuista luvuista pienempi oli " + str(pienempiLuku) + ".")
    return None
    
def paaohjelma():
    tulostaOhjeet()
    
    kehote1 = "Anna positiivinen kokonaisluku: "
    kehote2 = "Anna vertailtava positiivinen kokonaisluku (0 lopettaa): "
    kehote3 = "Anna uusi positiivinen kokonaisluku (0 lopettaa): "
    
    lukumaara = 0
    pieninLuku = 0
    
    while (True):
        if (lukumaara == 0):
            lukumaara = lukumaara + 1
            luku = kysyLuku(kehote1)
            lopetusEhto = luku
            pieninLuku = luku
            
        elif (lukumaara == 1):
            luku2 = kysyLuku(kehote2)
            if (luku2 == 0):
                break
            
            lukumaara = lukumaara + 1
            pienempiLuku = vertaileLukuja(luku, luku2)
            tulostaTiedot(pienempiLuku)
            pieninLuku = pienempiLuku
            
        else:
            luku = kysyLuku(kehote3)
            if (luku == 0):
                break
            
            lukumaara = lukumaara + 1
            pienempiLuku =  vertaileLukuja(luku, pienempiLuku)
            pieninLuku = pienempiLuku
            tulostaTiedot(pienempiLuku)
     
     
    print("")        
    if (lukumaara == 1):
        print("Annoit yhden luvun, joka oli " + str(pieninLuku) + ".")    
    else:      
        print("Annoit " + str(lukumaara) + " lukua.")
        print("Annetuista luvuista pienin oli " + str(pieninLuku) + ".")
        print("Kiitos ohjelman käytöstä.")
    return None
        
paaohjelma()
