#trafikklys
def trafikklys():
    lys=input("Hva er fargen på lyset?").lower()
    if lys=="rød":
        print("Stopp")
    elif lys=="grønn":
        print("Kjør")
    elif lys=="oransj" or "gul":
        sikkerhet=input("Er det trygt å gasse på?").lower()
        
        if sikkerhet=="ja":
            print("Gass på!")
        if sikkerhet=="Nei":
            print("vent!")
        else:
            print("Vent!")
    else:
        print("Er det trafikklys?")
    
#tar     inn verdier fra input lys og lower dem så deretter svarer på hva en skal gjøre, dersom 
#gul eller oransj vil den spørre sikkerheten for å kjøre
        


    
trafikklys()