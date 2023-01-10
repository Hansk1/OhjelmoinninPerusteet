#Kerätään käyttäjältä tarvittavat tiedot:
print("Selvitetään tuotteen alennusprosentti ja myyntihinta.")
hinta = float(input("Mikä on tuotteen listahinta: "))


print("Lasketaanko hinta\n1) yhdellä monihaaraisella valintarakenteella\n2) useilla erillisillä valintarakenteilla?")
valinta = int(input("Anna valintasi: "))

#Käsitellään tieto:
#Valintana tapa 1:
if (valinta == 1):
    print("Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:")
    if (hinta >= 300):
        ale_prosentit = 30
        hinta = hinta * 0.7
    elif (hinta >= 200):
        ale_prosentit = 20
        hinta = hinta * 0.8
    elif (hinta >= 100):
        ale_prosentit = 10
        hinta = hinta * 0.9
    else:
        print("Tuotteen alennus on 0% ja hinnaksi jää " + str(hinta) + "e.")
    print("Tuotteen alennus on " + str(ale_prosentit) + "% ja hinnaksi jää " + str(round(hinta, 2)) + "e.")
      
#Valintana tapa 2:
elif (valinta == 2):
    print("Monella erillisellä valintarakenteella tulokset ovat seuraavat:")
    if (hinta >= 300):
        ale_prosentit = 30
        hinta = hinta * 0.7
    if (hinta >= 200):
        ale_prosentit = 20
        hinta = hinta * 0.8 
    if (hinta >= 100):
        ale_prosentit = 10
        hinta = hinta * 0.9
    else:
        print("Tuotteen alennus on 0% ja hinnaksi jää " + str(hinta) + "e.")
    print("Tuotteen alennus on " + str(ale_prosentit) + "% ja hinnaksi jää " + str(round(hinta, 2)) + "e.")
        
#Tuntematon  valinta:
else:
    print("Tuntematon valinta.")
    print("Tuotteen alennus on 0% ja hinnaksi jää " + str(hinta) + "e.")


print("Kiitos ohjelman käytöstä.")
