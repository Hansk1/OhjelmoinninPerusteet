#Kerätään käyttäjältä tieto:
nimi = input("Mikä nimesi on: ")
kolmion_kanta = input("Anna kolmion kanta kokonaislukuna: ")
kolmion_korkeus = input("Anna kolmion korkeus desimaalilukuna: ")

#Käsitellään käyttäjältä saatu tieto:
kolmion_pinta_ala = str((int(kolmion_kanta) * float(kolmion_korkeus)) / 2)

#Tulostetaan tieto käyttäjälle:
print(nimi + " annoit kannaksi " + kolmion_kanta + " ja korkeudeksi " + str(float(kolmion_korkeus)))
print("Kolmion pinta-ala on tällöin " + kolmion_pinta_ala)
print("Kiitos ohjelman käytöstä.")
