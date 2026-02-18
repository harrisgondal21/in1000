butikkvarer={"melk":14.90, "brød":24.90,"yoghurt":12.90, "pizza":39.90} #Valgte dict siden det er to type data
bv1_navn=input("Vare 1: "); bv1_pris=float(input("Pris vare 1: ")) #Nye variabler som tar inn pris og navn på nye variabler
bv2_navn=input("Vare 2: "); bv2_pris=float(input("Pris vare 2: "))

butikkvarer[bv1_navn.lower()]=bv1_pris #endrer butikkvarerordbok ved å legge inn ny pris og ny varenavn

butikkvarer[bv2_navn.lower()]=bv2_pris

print(butikkvarer)
brukerinput=input(("Hvilken vare?"))
if brukerinput in butikkvarer: # Hvis varer str er i butikkvarer så printes det ut navn og pris
    print(f"Prisen på {brukerinput} er {butikkvarer[brukerinput]} kr")
else: 
    print("Varen er ikke i butikken")

"""Vare 1: Løk
Pris vare 1: 70
Vare 2: Hamburger
Pris vare 2: 100
{'melk': 14.9, 'brød': 24.9, 'yoghurt': 12.9, 'pizza': 39.9, 'løk': 70.0, 'hamburger': 100.0}
Hvilken vare?løk
Prisen på løk er 70.0 kr

Process finished with exit code 0
"""


