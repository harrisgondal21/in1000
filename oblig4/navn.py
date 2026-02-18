"""Oppgaven er å kunne bruke løkke til å skrive inn antal venner, deres navn og deres 
bursdag, hvilken dato, deretter velge deres navn for å printe ut navn og dato
"""


bursdag={"Navn":{},"Dato":{}}
antall_venner=int(input("hvor mange venn gng?"))
for i in range(0,antall_venner):
    navn = input("Skriv inn navn: ")
    dato = input("Skriv inn bursdag (dd-mm): ")

    bursdag["Navn"][i] = navn      # Legger til informasjon i bursdag dict
    
    bursdag["Dato"][i] = dato
    
velg = input("Søk navn: ").lower()
for i in range(0,antall_venner):
    if bursdag["Navn"][i].lower() == velg:
        print(bursdag["Navn"][i], bursdag["Dato"][i])
        break
else:
    print("Ikke funnet")
"""[hgondal@fedora in1000]$ /bin/python /home/hgondal/in1000/in1000/oblig4/test.py
hvor mange venn gng?2
Skriv inn navn: oslo
Skriv inn bursdag (dd-mm): 0191
Skriv inn navn: herim
Skriv inn bursdag (dd-mm): 0909
Søk navn: oslo
oslo 0191
[hgondal@fedora in1000]$ """