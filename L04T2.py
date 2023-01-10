#Painojen keskiarvon lasku:

#Aloitetaan while loop, jonka aikana lasketaan syötettyjen painojen summa ja lukumäärä, loopista pääsee arvolla 0 ulos:
PainojenSumma = 0
SyotettyjenPainojenLukumaara = 0
LopetusArvo = True
while (LopetusArvo == True):
    Paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
    if (Paino == 0):
        LopetusArvo = False
    elif (Paino >= 30 and Paino <= 130):
        PainojenSumma = PainojenSumma + Paino
        SyotettyjenPainojenLukumaara = SyotettyjenPainojenLukumaara + 1
    else:
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
        
PainojenKeskiarvo = PainojenSumma / SyotettyjenPainojenLukumaara
print("Painojen keskiarvo on " + str(round(PainojenKeskiarvo, 1)) + ".")
print("Kiitos ohjelman käytöstä.")
