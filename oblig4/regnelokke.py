"""Oppgave 1: Regning med løkker
Filnavn: regnelokke.py
1. Lag et program som leser inn tall fra brukeren helt til brukeren taster 0, uten å
gjøre noe mer med tallene.
2. Utvid programmet slik at alle tallene brukeren taster inn lagres i en samling.
3. Når brukeren er ferdig med å legge inn tall, skriv da alle tallene ut ett etter ett
ved å iterere over samlingen.
4. La programmet regne ut summen av alle tallene brukeren har skrevet inn
(uten å bruke sum()-funksjonen).
5. Finn nå samlingens minste og største tall, og skriv disse ut i terminalen (uten
å bruke min() eller max()).
Syntes du denne oppgaven var vanskelig? Se Trix-oppgave 4.01, 4.06, 4.09 og/eller
se gjennom undervisningsmodulene Løkker, For-løkker og Kombinere løkker og
samlinger i uke 4. Syntes du denne oppgaven var enkel? Se Trix-oppgave 4.15"""
sum=0
tall_liste = [] #Definerer liste og sum variabel
while True: 
    tall=float(input("Skriv inn et tall og 0 for å avslutte:"))
    if tall==0: #Skriver inn et tall og avslutter når 0 er skrevet inn
        break
    else:
        tall_liste.append(tall) #Legger til tall i lista etter null
for i in tall_liste: #For loop for å summere tall
    print(i)
    sum+=i
print("Summen er :",sum)
"""definerer max og min som første element for å kunne sammenligne med resten av elementene i lista, og for loop for å finne max og min"""
max_tall = tall_liste[0]
min_tall = tall_liste[0]
"""For ett tall max_tall er mindre enn det neste tallet i lista, så blir max_tall det tallet. Det samme gjelder for min_tall"""
while i < len(tall_liste):
    if max_tall<tall_liste[i]:
        max_tall=tall_liste[i]
    if min_tall>tall_liste[i]:
        min_tall=tall_liste[i]
    i += 1#for å iterere gjennom lista
print(f"max_tall={max_tall}, min_tall={min_tall}")#Printer ut


"""hgondal@fedora in1000]$ /bin/python /home/hgondal/in1000/in1000/oblig4/regnelokke.py
Skriv inn et tall og 0 for å avslutte:4864
Skriv inn et tall og 0 for å avslutte:48645
Skriv inn et tall og 0 for å avslutte:444
Skriv inn et tall og 0 for å avslutte:42
Skriv inn et tall og 0 for å avslutte:0
4864.0
48645.0
444.0
42.0
Summen er : 53995.0
max_tall=4864.0, min_tall=4864.0
[hgondal@fedora in1000]$ """


    