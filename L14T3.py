#Tuodaan kirjastot:
import datetime

def paaohjelma():
    Vuosi = int(input("Anna vuosi: "))
    Kuukausi = int(input("Anna kuukausi: "))
    
    #Selvitetään kuukauden ensimmäinen päivä:
    EnsimmainenPaiva = datetime.date(Vuosi, Kuukausi, 1)
    EnsimmainenPaiva = EnsimmainenPaiva.weekday()
    #selvitetään kuukauden päivien määrä:
    if Kuukausi < 12:
        PaivienMaara = (datetime.date(Vuosi, Kuukausi + 1, 1) - datetime.date(Vuosi, Kuukausi, 1)).days
    else:
        PaivienMaara = (datetime.date(Vuosi + 1, 1, 1) - datetime.date(Vuosi, Kuukausi, 1)).days
    #Tulostetaan kalenteri:
    print("Kalenteri näyttää seuraavalle:")
    
    #Tulostetaan viikonpäivien lyhenteet:
    print(" Ma Ti Ke To Pe La Su")
    
    #Tulostetaan päivät:
    for i in range(1, PaivienMaara + 1):
        #Tulostetaan ensimmäisen viikon välilyönnit:
        if i == 1:
            Tuloste =  "   " * EnsimmainenPaiva
            print(Tuloste, end="")
            
        #Tulostetaan 9 ensimmäistä päivää:
        if i < 10:
            print("  " + str(i), end="")
        
        #Tulostetaan loput päivät:
        elif i >= 10:
            print(" " + str(i), end="")
        
        #Tarkistetaan ollaanko sunnuntaissa:
        if (i + EnsimmainenPaiva) % 7 == 0:
            print("\n", end="")

    return None

paaohjelma()
