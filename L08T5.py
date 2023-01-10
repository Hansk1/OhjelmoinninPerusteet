import L08T5Kirjasto as kirjasto

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    LuetutRivit = []
    AnalysoidutRivit = []
    
    LuettavanTiedostonNimi = " "
    KirjoitettavanTiedostonNimi = " "
    
    KehoteLuettava = "luettavan"
    KehoteKirjoitettavan = "kirjoitettavan"
    
    Valinta = 1
    while (Valinta != 0):
        Valinta = valikko()
        
        if Valinta == 1:
            LuettavanTiedostonNimi = kirjasto.kysyTiedostonNimi(KehoteLuettava, LuettavanTiedostonNimi)
            LuetutRivit = kirjasto.lueTiedosto(LuettavanTiedostonNimi, LuetutRivit)
            
        elif Valinta == 2:
            AnalysoidutRivit = kirjasto.analysoi(LuetutRivit, AnalysoidutRivit)
            
        elif Valinta == 3:
            KirjoitettavanTiedostonNimi = kirjasto.kysyTiedostonNimi(KehoteKirjoitettavan, KirjoitettavanTiedostonNimi)
            kirjasto.kirjoita(KirjoitettavanTiedostonNimi ,AnalysoidutRivit)
  
                    
        elif Valinta == 0:
            print("Lopetetaan")
            print("")
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")
    
    print("Kiitos ohjelman käytöstä.")
    return None
        
paaohjelma()
