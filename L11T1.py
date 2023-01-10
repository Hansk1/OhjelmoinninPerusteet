def algoritmi(Luku):
    if Luku == 0 or Luku == 1:
        return Luku
    
    x = 1
    Tulos = 1

    while Tulos <= Luku:
        x = x + 1
        Tulos = x * x

    #Tarkistetaan kumpi lähimpänä olevista luvuista on lähempänä:
    YlittavaLuku = x
    AlittavaLuku = x - 1

    #Lasketaan Lukujen potenssit:
    YlittavaPotenssi = YlittavaLuku * YlittavaLuku
    AlittavaPotenssi = AlittavaLuku * AlittavaLuku

    #Tarkistetaan, että onko kumpikaan luku sama kuin syötettyluku:
    if YlittavaPotenssi == Luku:
        return YlittavaLuku
    elif AlittavaPotenssi == Luku:
        return AlittavaLuku

    #Lasketaan erotus syötettyyn lukuun:
    YlittavaErotus = Luku - YlittavaPotenssi
    AlittavaErotus = Luku - AlittavaPotenssi

    #Muutetaan mahdolliset negatiiviset luvut positiiviseksi:
    YlittavaErotus = abs(YlittavaErotus)
    AlittavaErotus = abs(AlittavaErotus)

    #Suoritetaan Lopullinen vertailu
    Vastaus = 0
    if YlittavaErotus < AlittavaErotus:
        Vastaus = YlittavaLuku
    else:
        Vastaus = AlittavaLuku
    
    return Vastaus


def paaohjelma():
    Luku = int(input("Anna luku: "))
    Neliojuuri = algoritmi(Luku)
    print("Neliöjuuri on", Neliojuuri)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
