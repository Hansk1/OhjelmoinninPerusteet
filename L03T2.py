#Kerätään käyttäjältä tieto:
print("Selvitetään sanojen aakkosjärjestys.")
sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

#Selvitetään kumpi sana on aakkosissa aikaisemmin:
if(sana1 < sana2):
    print("'" + sana1 + "' on aakkosissa aiemmin kuin '" + sana2 + "'.")
elif(sana1 > sana2):
    print("'" + sana2 + "' on aakkosissa aiemmin kuin '" + sana1 + "'.")
else:
    print("Sanat ovat samoja, '" + sana1 + "'.")
    
    
#Selvitetään merkin sisältyminen merkkijonoon.
print("\nSelvitetään merkin sisältyminen merkkijonoon.")

merkkijono = input("Anna merkkijono: ")
etsittava_merkki = input("Anna etsittävä merkki: ")

if(etsittava_merkki in merkkijono):
    print("Merkki '" + etsittava_merkki + "' sisältyy merkkijonoon '" + merkkijono + "'." )
else:
    print("Merkki '" + etsittava_merkki + "' ei sisälly merkkijonoon '" + merkkijono + "'." )
    

#Tutkitaan onko sana palindromi:
print("\nSelvitetään, onko sana palindromi.")

sana = input("Anna testattava sana: ")

if(sana == sana[::-1]):
    print("Sana '" + sana + "' on palindromi.")
else:
    print("Sana ei ole palindromi.")
    print("Sana on etuperin '" + sana + "' ja takaperin '" + sana[::-1] + "'.")
    
print("Kiitos ohjelman käytöstä.")
