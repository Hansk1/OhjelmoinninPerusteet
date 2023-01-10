class TUOTE:
    tuotetunniste = None
    tuotteidenLukumaara = None
    hinta = None

def kysyTiedostonNimi(kehote, nimi):
    TiedostonNimi = input("Anna " + kehote + " tiedoston nimi, nykyinen on '" + nimi + "'.")
    return TiedostonNimi
     
    
def lueTiedosto(TiedostoNimi, lista):
    tiedosto = open(TiedostoNimi, "r", encoding="utf-8")
    
    while True:
        rivi = tiedosto.readline()
        rivi = rivi[:-2]
        if len(rivi) == 0:
            break
    
        tiedot = rivi.split(";")
        Tuote = TUOTE()
        Tuote.tuotetunniste = tiedot[0]
        Tuote.tuotteidenLukumaara = tiedot[1]
        Tuote.hinta = tiedot[2]
        lista.append(Tuote)
    
    print("")    
    tiedosto.close()  
    return lista
        
    
def analysoi(luettuLista, analysoituLista):
    summa = 0
    for obj in luettuLista:
        tulos = float(obj.tuotteidenLukumaara) * float(obj.hinta)
        summa = summa + tulos
        analysoituLista.append(round(tulos, 2))
    print("Tiedot on analysoity, varaston arvo on", summa, "EUR:")
    print("")
    return analysoituLista
        
    

def kirjoita(TiedostoNimi, Analysoitulista):
    tiedosto = open(TiedostoNimi, "w", encoding="utf-8")
    for i in Analysoitulista:
        tiedosto.write(str(i))
        tiedosto.write("\n")
    print("------------------------------------")
    print("")
        