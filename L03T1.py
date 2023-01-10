#Kerätään käyttäjältä tieto:
print("Anna kaksi kokonaislukua.")

luku1 = input("Anna luku 1: ")
luku2 = input("Anna luku 2: ")

#Tulostetaan tieto käyttäjälle:
print("Selvitetään, ovatko antamasi luvut parillisia.")

#Selvitetään ovatko luvut parillisia:
if (int(luku1) % 2 == 0):
    print("Luku " + luku1 + " on parillinen.")
else:
    print("Luku " + luku1 + " on pariton.")
if (int(luku2) % 2 == 0):
    print("Luku " + luku2 + " on parillinen.")
else:
    print("Luku " + luku2 + " on pariton.")
 

#Selvitetään pienempi luku tai ovatko luvut yhtä suuria:
print("Selvitetään, kumpi antamistasi luvuista on pienempi.")   
    
if(int(luku1) == int(luku2)):
    print("Luvut " + luku1 + " ja " + luku2 + " ovat yhtäsuuria.")
elif(int(luku1) > int(luku2)):
    print("Luku " + luku2 + " on pienempi.")
else:
    print("Luku " + luku1 + " on pienempi.")
    
print("Kiitos ohjelman käytöstä.")
