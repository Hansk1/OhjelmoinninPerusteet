#Kerätään käyttäjältä tieto:
from re import L


sana = input("Anna sana: ")

#Käsitellään ja esitetään tieto:
print("Antamasi sanan kolme ensimmäistä kirjainta ovat " + sana[:3])
print("Sanan neljä viimeistä kirjainta ovat " + sana[-4:])
print("Kirjaimet 3, 4, 5 ja 6 ovat " + sana[2:6])
print("\nSanan joka kolmas kirjain alkaen ensimmäisestä kirjaimesta: " + sana[::3])
print("\nAntamasi sana '" + sana + "' on takaperin '" + sana[::-1] + "'.")

#Kerätään käyttäjältä lisää tietoa
aloitupaikka = int(input("\nAnna aloituspaikka: "))
lopetuspaikka = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))

#Esitetään tieto:
print("Antamillasi asetuksilla sana " + sana + " tulostuu näin: " + sana[aloitupaikka:lopetuspaikka:siirtyma])
print("\nAntamasi sanan pituus oli " + str(len(sana)) + " merkkiä.")
print("Kiitos ohjelman käytöstä.")
