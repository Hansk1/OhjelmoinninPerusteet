#Alustetaan tiedot:
c_hinta = 79.00
b_hinta = round(c_hinta * 1.10)
a_hinta = round(c_hinta * 1.60)
sesonki_kerroin_c = 1.50
sesonki_kerroin_b = 1.75
sesonki_kerroin_a = 2.75
kanta_asiakasalennus_kerroin = 0.90

#Kerätään käyttäjältä tieto:
print("Tämä ohjelma laskee risteilyhintoja.")
hyttityyppi = input("Minkälainen hytti on kyseessä - A, B vai C-hytti: ")
hyttityyppi = hyttityyppi.lower()

aika = input("Onko sesonkiaika (k/e): ")
aika = aika.lower()

kanta_asiakkuus = input("Onko kanta-asiakas (k/e): ")
kanta_asiakkuus = kanta_asiakkuus.lower()

#Käsitellään tieto:
if (hyttityyppi == "a"):
    if (aika == "k" and kanta_asiakkuus == "k"):
        summa = a_hinta * sesonki_kerroin_a * kanta_asiakasalennus_kerroin
    elif (aika == "k"):
        summa = a_hinta * sesonki_kerroin_a
    elif (kanta_asiakkuus == "k"):
        summa = a_hinta * kanta_asiakasalennus_kerroin
    else:
        summa = a_hinta
    print("A-hytti maksaa " + str(round(float(summa), 2)) + " euroa.")    
        
elif (hyttityyppi == "b"):
    if (aika == "k" and kanta_asiakkuus == "k"):
        summa = b_hinta * sesonki_kerroin_b * kanta_asiakasalennus_kerroin
    elif (aika == "k"):
        summa = b_hinta * sesonki_kerroin_b
    elif (kanta_asiakkuus == "k"):
        summa = b_hinta * kanta_asiakasalennus_kerroin
    else:
        summa = b_hinta
    print("B-hytti maksaa " + str(round(float(summa), 2)) + " euroa.")   
        
elif (hyttityyppi == "c"):
    if (aika == "k" and kanta_asiakkuus == "k"):
        summa = c_hinta * sesonki_kerroin_c * kanta_asiakasalennus_kerroin
    elif (aika == "k"):
        summa = c_hinta * sesonki_kerroin_c
    elif (kanta_asiakkuus == "k"):
        summa = c_hinta * kanta_asiakasalennus_kerroin
    else:
        summa = c_hinta
    print("C-hytti maksaa " + str(round(float(summa), 2)) + " euroa.")    

print("Kiitos ohjelman käytöstä.")
