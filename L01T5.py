#Kerätään käyttäjältä tieto:
tyttojen_maara = input("Anna tyttöjen lukumäärä: ")
poikien_maara = input("Anna poikien lukumäärä: ")

#Käsitellään ja tulostetaan käyttäjälle tieto:
oppilaitten_summa = int(tyttojen_maara) + int(poikien_maara)

print("Tyttöjä on " + tyttojen_maara + " ja poikia on " + poikien_maara)
print("Yhteensä luokalla on " + str(oppilaitten_summa) + " oppilasta.")
