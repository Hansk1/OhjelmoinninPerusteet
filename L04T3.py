print("Ohjelma kysyy merkkijonoja ja etsii niistä pisimmän.")

MerkkiJonojenMaara = int(input("Kuinka monta merkkijonoa kysytään: "))
MerkkiJononMinimipituus = int(input("Mikä on merkkijonon minimipituus: "))
KielettyMerkki = input("Mitä merkkiä merkkijonossa ei saa olla: ")
MerkkiJonojenTodellinenMaara = 0
PisinMerkkijono = ""

while (True):   
    MerkkiJono = input("Anna merkkijono: ")
    MerkkiJonojenTodellinenMaara = MerkkiJonojenTodellinenMaara + 1
    
    if (len(MerkkiJono) > len(PisinMerkkijono)):
        PisinMerkkijono = MerkkiJono
    
    if (len(MerkkiJono) < MerkkiJononMinimipituus):
        print("Ohjelma päättyi, koska merkkijonon minimipituus ei täyttynyt.")
        break
            
    if (MerkkiJonojenTodellinenMaara == MerkkiJonojenMaara):
        print("Ohjelma päättyi, koska maksimimäärä merkkijonoja tuli täyteen.")
        break
    
    if (KielettyMerkki in MerkkiJono):
        print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
        break
else:
    print("Ohjelma päättyi tuntemattomaan syyhyn.")  
    
print("Annoit " + str(MerkkiJonojenTodellinenMaara) + " merkkijonoa.")
print("Pisin merkkijono oli '" + PisinMerkkijono + "', jossa oli " + str(len(PisinMerkkijono)) + " merkkiä.")
print("Kiitos ohjelman käytöstä.")
