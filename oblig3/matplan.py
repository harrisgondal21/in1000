Beboer={'per': {'Frokost': 'Havregryn', 'lunsj': 'pølse', 'middag': 'kjøtt'},
    'kari': {'Frokost': 'yoghurt', 'lunsj': 'egg', 'middag': 'poteter'},
   'ole': {'Frokost': 'brød', 'lunsj': 'salat', 'middag': 'pasta'}}
#Lager en datastrukturen i dict

def matplan(): #
    beboer = input("Hvilken beboer vil du vite matplanen for?: ").lower() #input som lower det
    if beboer in Beboer: #
        for i in Beboer[beboer]: 
            print(f"{i}: {Beboer[beboer][i]}") #Hvis beboer i beboer så printes det ut Navn og str av den i dicten
    else:
        print("Ugyldig beboernavn.")
try:
    matplan()
except KeyboardInterrupt:
    print("ctrl + c activated")

"""
[hgondal@MonguardWin oblig3]$ /bin/python /home/hgondal/in1000/in1000/oblig3/matplan.py
Hvilken beboer vil du vite matplanen for?: per
Frokost: Havregryn
lunsj: pølse
middag: kjøtt
Hvilken beboer vil du vite matplanen for?: ole
Frokost: brød
lunsj: salat
middag: pasta
Hvilken beboer vil du vite matplanen for?: kari
Frokost: yoghurt
lunsj: egg
middag: poteter
Hvilken beboer vil du vite matplanen for?: Morten
Ugyldig beboernavn.
"""

"""
2.1 Brukernavn i formatet "harrisg" ville jeg valgt dict siden man som regel skal søke opp og dict er enklere
2.2 Dict igjen siden det er enklere å søke opp og legge til stp ved siden av
2.3 Liste slik at duplikater er lov rekkefølge kan være relevant mtp hvem vant først og det er enklere å legge til nye vinnere
2.4 Dict siden man kan legge til verdier som hvem som er allergisk mott hva
"""
