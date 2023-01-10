print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")

alaraja = int(input("Anna lukualueen alaraja: "))
ylaraja = int(input("Anna lukualueen yläraja: "))

LukuNotFound = True

for i in range(alaraja, ylaraja + 1):
    if (i % 5 == 0):
        if( i % 7 == 0):
            print("Luku " + str(i) + " on jaollinen 5:llä ja 7:llä.")
            print("Lopetetaan etsintä.")
            LukuNotFound = False
            break
        else:
            print(str(i) + " ei ole jaollinen seitsemällä, hylätään.")
    else:
        print(str(i) + " ei ole jaollinen viidellä, hylätään.")

if (LukuNotFound):
    print("Alueelta ei löytynyt sopivaa lukua.")
    
print("Kiitos ohjelman käytöstä.")
