#Korjattu versio

#Määritellään tieto
luku1 = 123
luku2 = 456

#Käsitellään tieto
summa = luku1 + luku2
erotus = luku2 - luku1
tulo = summa * erotus
luvun1_jj = luku1 % 2
luvun2_jj = luku2 % 2

#Muutetaan saatu tieto merkkijonoiksi
luku1 = str(luku1)
luku2 = str(luku2)
summa = str(summa)
erotus = str(erotus)
tulo = str(tulo)
luvun1_jj = str(luvun1_jj)
luvun2_jj = str(luvun2_jj)

#Esitetään tieto käyttäjälle
print(luku1 + " + " + luku2 + " = " + summa)
print(luku2 + " - " + luku1 + " = " + erotus)
print(summa + " * " + erotus + " = " + tulo)
print("( " + luku1 + " + " + luku2 + " ) " + "*" + " ( " + luku2 + " - " + luku1 + " ) " + "= " + tulo)
print("Luvun " + luku1 + " jakojäännös 2 :lla on " + luvun1_jj)
print("Luvun " + luku2 + " jakojäännös 2 :lla on " + luvun2_jj)
