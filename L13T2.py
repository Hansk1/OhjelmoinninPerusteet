import sys

#Lista parillisille luvuille:
ParillisetLuvut = []

#Etsitään parilliset luvut:
for i in sys.argv[1:]:
    if ((int(i) % 2) == 0):
        ParillisetLuvut.append(int(i))

#Tulostetaan käyttäjälle tiedot:
print("Syötteen parilliset luvut ovat seuraavat:")

for i in ParillisetLuvut:
    print(i, end=" ")
Keskiarvo = sum(ParillisetLuvut) / len(ParillisetLuvut)
print("\nLukujen keskiarvo on {:0.2f}." .format(Keskiarvo))
print("Kiitos ohjelman käytöstä.")
