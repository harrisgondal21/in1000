'''temp=int(input("Hva er temperaturen?")) #Tar int input temp fra bruker
type_temp=input("Er temperaturen i Fahrenheit (F) eller Celsius (C)?. Kun velg F eller C: ") #Velg Enhet
if type_temp=="F":
    C= (temp - 32) * 5/9
    print("Temperaturen i Celsius er: ", C, "C")
elif type_temp=="C":
    F= (temp * 9/5) + 32
    print("Temperaturen i Fahrenheit er : ", F, "F")
else:
    try:
        type_temp.upper()
    except:
        pass
    print('Feil.')'''
def temp():
    temp=int(input("Hva er temperaturen?")) #Tar int input temp fra bruker
    type_temp=input("Er temperaturen i Fahrenheit (F) eller Celsius (C)?. Kun velg F eller C: ") #Velg Enhet
    if type_temp=="F":
        C= (temp - 32) * 5/9
        print("Temperaturen i Celsius er: ", C, "C")
    elif type_temp=="C":
        F= (temp * 9/5) + 32
        print("Temperaturen i Fahrenheit er : ", F, "F")
    else:
        print("Noe er feil.")

temp()
#Hvis temp str er F, konverter til C og print og motsatt. Hvis feil enhet, printes Feil.
    
