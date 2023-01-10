#Kerätään käyttäjältä tieto:
from ipaddress import summarize_address_range


print("Tämä ohjelma laskee neljän tenttiarvosanan keskiarvon.")

arvosana_1 = int(input("Anna 1. tenttiarvosana väliltä 0-5: "))
arvosana_2 = int(input("Anna 2. tenttiarvosana väliltä 0-5: "))
arvosana_3 = int(input("Anna 3. tenttiarvosana väliltä 0-5: "))
arvosana_4 = int(input("Anna 4. tenttiarvosana väliltä 0-5: "))

#käsitellään käyttäjältä saatu tieto:
summa = arvosana_1 + arvosana_2 +   arvosana_3 + arvosana_4
keskiarvo = summa/ 4

#Esitetään tieto käyttäjälle:
print("\nAntamiesi arvosanojen summa on " + str(summa) + ".")
print("Antamiesi arvosanojen keskiarvo on " + str(round(keskiarvo, 1)) + ".")
print("Keskiarvo on kokonaislukuna " + str(int(keskiarvo)) + ".\nKiitos ohjelman käytöstä.")
