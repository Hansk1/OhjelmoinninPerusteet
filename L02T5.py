#Kerätään käyttäjältä tieto:
print("Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.")

paino_kg = float(input("Anna paino kiloina: "))
naula = 0.4536
jalka_m = 0.3048
tuuma_mm = 25.4
metri_cm = 100

#Käsitellään ja esitetään tieto:
print("Paino on " + str(paino_kg) + " kg eli " + str(round(paino_kg/naula, 1)) + " naulaa.")

#Kerätään käyttäjältä lisää tietoa:
pituus_cm = int(input("\nAnna pituus sentteinä: "))

#Käsitellään tieto:
pituus_m = round(pituus_cm/metri_cm, 2)

#pituus amerikkalaisittain
jalat = round((pituus_m - (pituus_m % jalka_m)) / jalka_m, 1)
tuumat = round(((pituus_m % jalka_m) * 1000 ) / tuuma_mm, 1)

print("Pituus on " + str(pituus_m) + " metriä", end="")
print(" eli amerikkalaisittain " + str(jalat) + " jalkaa", end="")
print(" ja " + str(tuumat) + " tuumaa.")

print("Kiitos ohjelman käytöstä.")