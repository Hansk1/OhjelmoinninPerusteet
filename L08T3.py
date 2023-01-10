import datetime


def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnista aika-olion komponentit")
    print("2) Laske ikä päivinä")
    print("3) Tulosta viikonpäivät")
    print("4) Tulosta kuukaudet")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta


def aikaOlionKomponentit():
    PaivamaaraJaKello = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    PaivamaaraJaKello = datetime.datetime.strptime(PaivamaaraJaKello, "%d.%m.%Y %H:%M")
    Vuosi = PaivamaaraJaKello.year
    Kuukausi = PaivamaaraJaKello.month
    Paiva = PaivamaaraJaKello.day
    Tunti = PaivamaaraJaKello.hour
    Minuutti = PaivamaaraJaKello.minute
    print("Annoit vuoden", Vuosi)
    print("Annoit kuukauden", Kuukausi)
    print("Annoit päivän", Paiva)
    print("Annoit tunnin", Tunti)
    print("Annoit minuutin", Minuutti)
    print("")
    return None


def ikaPaivina():
    Paivamaara = input("Anna syntymäpäivä muodossa pp.kk.vvvv: ")
    Paivamaara = datetime.datetime.strptime(Paivamaara, "%d.%m.%Y")
    Paiva = Paivamaara.date()
    VerrattavaPaiva = datetime.date(2000, 1, 1)
    ikaPaivissa = VerrattavaPaiva - Paiva
    ikaPaivissa = ikaPaivissa.days
    print("1.1.2000 henkilö oli", ikaPaivissa, "päivää vanha.")
    print("")
    return None


def tulostaViikonpaivat():
    Paiva = datetime.date(2022, 10, 31)
    i = 0
    while i < 7:
        print(Paiva.strftime("%A"))
        Paiva = Paiva + datetime.timedelta(days=+1)
        i = i +1
    print("")
    return None


def tulostaKuukaudet():
    Paiva = datetime.date(2000, 1, 10)
    i = 0
    while i < 12:
        print(Paiva.strftime("%b"))
        Paiva = Paiva + datetime.timedelta(days=+31)
        i = i + 1
    print("")
    return None


def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    Valinta = 1
    while (Valinta != 0):
        Valinta = valikko()
        
        if Valinta == 1:
            aikaOlionKomponentit()
            
        elif Valinta == 2:
            ikaPaivina()
            
        elif Valinta == 3:
            tulostaViikonpaivat()
            
        elif Valinta == 4:
            tulostaKuukaudet()
                    
        elif Valinta == 0:
            print("Lopetetaan.")
            print("")
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")
    
    print("Kiitos ohjelman käytöstä.")
    return None
        
paaohjelma()
