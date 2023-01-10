#Kerätään käyttäjältä tiedot:
auton_merkki = input("Anna auton merkki: ")
auton_malli = input("Anna auton malli: ")

#käsitellään tieto:
yhdistetty_merkkijono = auton_merkki + " " + auton_malli + "."

#Tuodaan tieto esille:
print("Auto on " + auton_merkki + ", " + yhdistetty_merkkijono)

#Kerätään käyttäjältä lisää tietoa:
sana_1 = input("\nAnna ensimmäinen sana: ")
sana_2 = input("Anna toinen sana: ")

#Käsitellään tieto:
yhdyssana = sana_1 + sana_2

#Tuodaan tieto esille:
print("Sanoista tulee yhdyssana '" + yhdyssana + "'.\nKiitos ohjelman käytöstä.")
