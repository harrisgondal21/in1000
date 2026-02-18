

liste_2 = []
liste_3=[]
liste_4=[]
while len(liste_2)<10: #Oppgave 1
    liste_2.append(len(liste_2))
liste=[i for i in range(0,10)]#Oppagev 2
print(f"Liste med for-løkke:{liste} og while {liste_2}")    #Printer ut
#Oppgave 3
"""While bruker betukgense at lengden er under 10 og for fordi range()
lager en liste med antall iterasjoner"""

#oppgave 4
""" range() har en samling og kan brukes og den inneholdewr samme tall som while
løkken? """
#Oppgave 5
print([k for k in range(0,20,3)]) #Kan bruke dette eller while nedenfor
#eller
tall = 0
while tall <= 20:
    liste_3.append(tall)
    tall += 3
print( liste_3)

for tre in liste_3:
    print(tre)
 



#Oppgave 7
"""fOR SÅ VI KAN Å GJENNOM EN ETTER EN også kunne enumerate
så hver element kan få ett tall før"""
for n in enumerate(liste_3):
    print(f"Posisjon {n[0]}: {n[1]}")

#oppgave 8 og 9
for l in range(len(liste_2)):
    liste_2[l] *= 10 #multipliserer hver med 10
print(liste_2)
"""[hgondal@fedora in1000]$ /bin/python /home/hgondal/in1000/in1000/oblig4/lokker_og_lister.py
Liste med for-løkke:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] og while [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 3, 6, 9, 12, 15, 18]
[0, 3, 6, 9, 12, 15, 18]
0
3
6
9
12
15
18
Posisjon 0: 0
Posisjon 1: 3
Posisjon 2: 6
Posisjon 3: 9
Posisjon 4: 12
Posisjon 5: 15
Posisjon 6: 18
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
[hgondal@fedora in1000]$ """