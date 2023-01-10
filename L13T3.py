#Tuodaan kirjastot:
import sys


def valikko():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta: ")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot viikonpäivittäin")
    print("0) Lopeta")
    Valinta = int(input("Valintasi: "))
    return Valinta




def lueTiedosto(DataLista):
    try:
        #Putsataan lista:
        DataLista.clear()
        
        #Kysytään tiedoston Nimi:
        TiedostonNimi = input("Anna luettavan tiedoston nimi: ")

        #Avataan tiedosto ja luetaan ensimmäinen "turha" rivi pois:
        Tiedosto = open(TiedostonNimi, "r", encoding="utf-8")
        Rivi = Tiedosto.readline()[:-1]
        
        Rivi = Tiedosto.readline()[:-1]
        while (len(Rivi) > 0): 
            Rivi = Rivi.split(";")
            
            #Lisätään rivi datalistaan:
            DataLista.extend([Rivi[0], Rivi[1], Rivi[2], Rivi[3], Rivi[4]])
        
            #Luetaan uusi rivi:
            Rivi = Tiedosto.readline()[:-1]
        
        #Suljetaan tiedosto:
        Tiedosto.close()
        
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)

    print("Tiedosto luettu.")
    print("")
    return DataLista  




def analysoi(DataLista, ViikonpaivienLukumaarat):
    for i in DataLista:
        Data = i.split(",")
        if Data[0] == "Monday":
            ViikonpaivienLukumaarat["Monday"] = ViikonpaivienLukumaarat["Monday"] + 1
        elif Data[0] == "Tuesday":
            ViikonpaivienLukumaarat["Tuesday"] = ViikonpaivienLukumaarat["Tuesday"] + 1
        elif Data[0] == "Wednesday":
            ViikonpaivienLukumaarat["Wednesday"] = ViikonpaivienLukumaarat["Wednesday"] + 1
        elif Data[0] == "Thursday":
            ViikonpaivienLukumaarat["Thursday"] = ViikonpaivienLukumaarat["Thursday"] + 1
        elif Data[0] == "Friday":
            ViikonpaivienLukumaarat["Friday"] = ViikonpaivienLukumaarat["Friday"] + 1
        elif Data[0] == "Saturday":
            ViikonpaivienLukumaarat["Saturday"] = ViikonpaivienLukumaarat["Saturday"] + 1
        elif Data[0] == "Sunday":
            ViikonpaivienLukumaarat["Sunday"] = ViikonpaivienLukumaarat["Sunday"] + 1
        
    return ViikonpaivienLukumaarat




def tulosta(AnalysoituData):
    print(";Palautuksia viikonpäivittäin")
    for i in AnalysoituData:
        print(i + ";" + str(AnalysoituData[i]))
    #Tulostetaan lukumäärien summa:
    print("Yhteensä;" + str(sum(AnalysoituData.values())))
    print("")
    return None




def paaohjelma():
    DataLista = []
    ViikonpaivienLukumaarat = {"Monday": 0, "Tuesday":0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday":0, "Sunday":0}
    Valinta = 1
    
    while (Valinta != 0):
        Valinta = valikko()
        if Valinta == 1:
            DataLista = lueTiedosto(DataLista) 
        elif Valinta == 2:
            AnalysoitSanakirja = analysoi(DataLista, ViikonpaivienLukumaarat)
            tulosta(AnalysoitSanakirja)
        elif Valinta == 0:
            print("Lopetetaan.")
            print("")
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")
            
    print("Kiitos ohjelman käytöstä.")
    
    #Tyhjennetään listat ja sanakirjat ohjelman lopuksi:
    DataLista.clear()
    ViikonpaivienLukumaarat.clear()
    
    
    return None

paaohjelma()
