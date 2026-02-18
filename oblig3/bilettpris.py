teller = 0
def stopp(): # kalles for å gjøre en pause i kjøringa. Trykk 'enter' for å fortsette.
    global teller  # Jeg ønsker faktisk å endre den globale variabelen
    teller = teller + 1
    input(str(teller) + '> ')
    print()

def billet_pris(): #en funksjon som tar input alder og skriver ut om det er i en range()
    alder=int(input("Hva er alderen din?"))
    if alder in range(16):
        print("Print: Barnebilett: 30kr")
    elif alder in range(16,67):
        print("Standard: 70kr")
    elif alder in range(67,100):
        print("Senior: 50kr")
    else:
        print("Feil!")
for i in range(3): #Kjører bilett:pris() og stopp() tre ganger
    billet_pris()
    stopp()

"""/bin/python /home/hgondal/in1000/in1000/oblig3/bilettpris.py
[hgondal@MonguardWin oblig3]$ /bin/python /home/hgondal/in1000/in1000/oblig3/bilettpris.py
Hva er alderen din?67
Senior: 50kr
1> 

Hva er alderen din?21
Standard: 70kr
2> 

Hva er alderen din?1
Print: Barnebilett: 30kr
3> 

"""


