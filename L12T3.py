import sys
import jsonpickle

class TIEDOT:
        Nimike = None
        Tekija = None
        ISBN = None
        Varauksia = None
        Niteita = None
        Lisakappaleita = None
        VarauksiaPerNide = None

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue CSV tiedosto")
    print("2) Lue JSON tiedosto")
    print("3) Kirjoita CSV tiedosto")
    print("4) Kirjoita JSON tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def lueCSV(Lista):
    try:
        #Tyhjennetää lista:
        Lista.clear()
        
        #Kysytyään luettavan tiedoston nimi:
        TiedostonNimi = input("Anna luettavan CSV tiedoston nimi: ")
        
        #Avataan tiedosto lukemista varten:
        Tiedosto = open(TiedostonNimi, "r", encoding="utf-8")
        
        #Luetaan ensimmäinen otsikkotietoja sisältävä rivi:
        Tiedosto.readline()
        
        #Luetaan tiedosto rivi kerrallaan ja tallennetaan tiedot olioihin ja oliot listaan:
        while True:
            rivi = Tiedosto.readline()
            rivi = rivi[:-1]
            if len(rivi) == 0:
                break
            RivinTiedot = rivi.split(";")
            Tiedot = TIEDOT()
            Tiedot.Nimike = RivinTiedot[0]
            Tiedot.Tekija = RivinTiedot[1]
            Tiedot.ISBN = RivinTiedot[2]
            Tiedot.Varauksia = int(RivinTiedot[3])
            Tiedot.Niteita = int(RivinTiedot[4])
            Tiedot.Lisakappaleita = int(RivinTiedot[5])
            Tiedot.VarauksiaPerNide = float(RivinTiedot[6].replace(",", "."))
            Lista.append(Tiedot)
            
        #Suljetaan tiedosto:    
        Tiedosto.close()   
         
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)    
                 
    print("Luettu " + str(len(Lista)) + " kirjan tiedot.")
    print("")   
    return Lista
        
    
    
def lueJSON(Lista):
    #tyhjennetään lista:
    Lista.clear()
    
    #Kysytään luettavan JSON tiedoston nimi:
    TiedostonNimi = input("Anna luettavan JSON tiedoston nimi: ")
    
    try:
        #Avataan tiedosto lukemista varten:
        Tiedosto = open(TiedostonNimi, "r", encoding="UTF-8")
        
        #Luetaan tiedosto ja tallennetaan se listaan:
        KoodattuData = Tiedosto.read()
        Lista = jsonpickle.decode(KoodattuData)
        
        #Suljetaan tiedosto:
        Tiedosto.close()
       
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)  
     
    print("Luettu " + str(len(Lista)) + " kirjan tiedot.") 
    print("")   
    return Lista
 
 
    
def kirjoitaCSV(Lista):
    #kysytään kirjoitettavan CVS tiedoston nimi:
    TiedostonNimi = input("Anna kirjoitettavan CSV tiedoston nimi: ")
    
    try:
        #Avataan tiedosto kirjoittamista varten:
        Tiedosto = open(TiedostonNimi, "w", encoding="UTF-8")
        
        #Kirjoitetaan tiedosto:
        Tiedosto.write("Nimike;Tekijä;ISBN;Varauksia;Niteitä;Tilattuja lisäkappaleita;Varauksia / nide\n")
        
        for i in Lista:
            KirjoitettavaRivi = i.Nimike + ";" + i.Tekija + ";" + i.ISBN + ";" + str(i.Varauksia) + ";" + str(i.Niteita) + ";" + str(i.Lisakappaleita) + ";" + str(i.VarauksiaPerNide) + "\n"
            Tiedosto.write(KirjoitettavaRivi)     
            
        #Suljetaan tiedosto:
        Tiedosto.close()
       
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)  
    
    print("Tiedosto {0:s} kirjoitettu.".format(TiedostonNimi))   
    print("")
    return None



def kirjoitaJSON(Lista):
    #Kysytään kirjoitettavan JSON tiedoston nimi:
    TiedostonNimi = input("Anna kirjoitettavan JSON tiedoston nimi: ")
    
    try:
        #Avataan tiedosto kirjoittamista varten:
        Tiedosto = open(TiedostonNimi, "w", encoding="utf-8")
        
        #Kirjoitetaan data tiedostoon:
        KirjoitettavaTeksti = jsonpickle.encode(Lista, indent = 4)
        Tiedosto.write(KirjoitettavaTeksti)
        Tiedosto.close()
        
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)    
    
    print("Tiedosto {0:s} kirjoitettu.".format(TiedostonNimi))   
    print("")
    return None



def paaohjelma():
    LuettuListaCVS = []
    LuettuListaJSON = []
    Valinta = 1
    
    while Valinta != 0:
        Valinta = valikko()
        if Valinta == 1:
            LuettuListaCVS = lueCSV(LuettuListaCVS)
            
        elif Valinta == 2:
            LuettuListaJSON = lueJSON(LuettuListaJSON)
            
        elif Valinta == 3:
            kirjoitaCSV(LuettuListaJSON)
            
        elif Valinta == 4:
            kirjoitaJSON(LuettuListaCVS)
            
        elif Valinta == 0:
            print("")
            
        else:
            print("Tuntematon valinta, yritä uudestaan")
    
    #Tyhjennetään listat:
    LuettuListaCVS.clear()
    LuettuListaJSON.clear()
    
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
