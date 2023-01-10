#Kerätään käyttäjältä tarvittavat tiedot:
print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
print("Valitse haluamasi toiminto:\n1) Tulosta merkkijono etuperin\n2) Tulosta merkkijono takaperin\n3) Tulosta merkkijonon pituus\n0) Lopeta")

valinta = int(input("Anna valintasi: "))
merkkijono = input("Anna merkkijono: ")


#Toteutetaan käyttäjän valitsema toiminto
if (valinta == 1):
    print("Merkkijono on etuperin '" + merkkijono + "'.")
elif (valinta == 2):
    print("Merkkijono on takaperin '" + merkkijono[::-1] + "'.")
elif (valinta == 3):
    print("Merkkijonon pituus on " + str(len(merkkijono)) + ".")
elif (valinta == 0):
    print("Lopetetaan")
    
print("Kiitos ohjelman käytöstä.")
