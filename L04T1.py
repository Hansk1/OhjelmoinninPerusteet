#Kerätään käyttäjältä tieto:
AloitusArvo = int(input("Anna aloitusarvo: "))
LopetusArvo = int(input("Anna lopetusarvo: "))

#Toteutus for lauseella:
print("")
print("Toteutus for-lauseella:")
for i in range(AloitusArvo, LopetusArvo + 1):
    print(i, end=" ")
print("\n")

#Toteutus while lauseella:
print("Toteutus while-lauseella:")
while (AloitusArvo <= LopetusArvo):
     print(AloitusArvo, end=" ")
     AloitusArvo = AloitusArvo + 1
print("\n")


print("Kiitos ohjelman käytöstä.")
