"""Oppgave 2: Reiseplan
Filnavn: reiseplan.py
I denne oppgaven skal du lage et program som lar en bruker legge planer for en
reise. Brukeren skal få mulighet til å legge inn informasjon om flere reisemål, hva de
skal pakke til hvert sted, og når de skal reise. Problemet må løses på en måte som
er oversiktlig og gjør det lett for brukeren å hente ut informasjon etterpå.
1. Be brukeren om å legge inn informasjon for fem ulike reiser. For hver reise
trenger vi navnet på reisemålet, hvilke type klær som må pakkes og
avreisedatoen. Tenk over hvordan du lagrer denne informasjonen (gjennom
bruk av samlinger) på en effektiv og ryddig måte. Det skal være mulig å lagre
alle reisedetaljene samlet, men også hente ut informasjon om én spesifikk del
av én reise ved hjelp av indekser.
2. Bruk en enkel for-løkke for å skrive ut informasjonen for hver reise. .
3. Nå skal du la brukeren velge hva de ønsker å se ved å oppgi to tall – ett for
hvilken av de fem reiser, og ett for hvilken av de 3 kategoriene (reisemål,
klær, dato). Håndter situasjoner der brukeren gir ugyldige tall på en god måte.
Skriv ellers ut den valgte informasjonen.
4. Prøv da om du kan gjøre programmet enda mer brukervennlig ved å bruke
navn på kategoriene i stedet for tall. Hvordan finner du riktig informasjon når
brukeren spør etter klær til reise 2?
5. Litt vanskeligere: Brukeren har ombestemt seg! Utvid nå programmet ditt slik
at brukeren kan endre en allerede eksisterende reiseplan. Kanskje
avreisedatoen for turen til Frankrike blir utsatt?"""
reiseplan={"Reisemål":{}, "Klær":{}, "Dato":{}} #dict i dict
antall_reiser=5
for i in range(0,antall_reiser): #For loop for å legge inn informasjon om 5 reiser
    reisemål=input("Skriv inn reisemål: ")
    klær=input("Skriv inn klær som må pakkes: ")
    dato=input("Skriv inn avreisedato: ")

    reiseplan["Reisemål"][i]=reisemål #Legger til informasjon i reiseplan dict
    reiseplan["Klær"][i]=klær
    reiseplan["Dato"][i]=dato

for j in range(0,antall_reiser): #For loop for å skrive ut informasjonen for hver reise
    print(f"Reisemål: {reiseplan['Reisemål'][j]}, Klær: {reiseplan['Klær'][j]}, Dato: {reiseplan['Dato'][j]}")

"""valg=int(input("Velg 1-5 for Reise "))-1#input for å velge reise og kategori
print(reiseplan["Reisemål"][valg])
valg_2=int(input("Skriv inn nytt valg for kategori (1: Reisemål, 2: Klær, 3: Dato): "))-1

print(reiseplan[list(reiseplan.keys())[valg_2]][valg]) #printer ut valgt informasjon basert på listen fra valg og .keys() """
reise_string = input("Velg reise (1-2): ")
reise_in = int(reise_string) - 1  # 1→0, 2→1

kategori = input("Skriv inn kategori (Reisemål, Klær, Dato): ")
kategori = kategori.capitalize()  #Stor forbokstav for å matche nøklene i reiseplan dict

if kategori in reiseplan:
    print("Valgt info:", reiseplan[kategori][reise_in])
else:
    print("Ugyldig kategori")

endre = input("Vil du endre denne informasjonen? (j/n): ")
if endre.lower() == "j":
    endring = input(f"Skriv inn ny verdi for {kategori} på reise {reise_in + 1}: ") #input for å endre informasjonen i reiseplan dict
    reiseplan[kategori][reise_in] = endring #endrer informasjonen i reiseplan dict

    print("Oppdatert reise:")
    print(f"Reisemål: {reiseplan['Reisemål'][reise_in]}, " #printer ut oppdatert informasjon
          f"Klær: {reiseplan['Klær'][reise_in]}, "
          f"Dato: {reiseplan['Dato'][reise_in]}")

#kode for tall    
"""endre = input("Vil du endre denne informasjonen? (j/n): ") #input for å endre informasjonen i reiseplan dict
if endre.lower() == "j":
    endring = input(f"Skriv inn ny verdi for {reiseplan['Reisemål'][valg]} på reise {valg_2}: ")
    reiseplan[list(reiseplan.keys())[valg_2]][valg] = endring #legger til endringen i reiseplan dict
    print("Oppdatert reise:")
    print(f"Reisemål: {reiseplan['Reisemål'][valg]}, "
          f"Klær: {reiseplan['Klær'][valg]}, Dato: {reiseplan['Dato'][valg]}")"""


#Utskrift av programmet med to land        
"""
[hgondal@fedora in1000]$ /bin/python /home/hgondal/in1000/in1000/oblig4/reiseplan.py
Skriv inn reisemål: oslo
Skriv inn klær som må pakkes: kald
Skriv inn avreisedato: 010101
Skriv inn reisemål: kina
Skriv inn klær som må pakkes: varm
Skriv inn avreisedato: 020202
Reisemål: oslo, Klær: kald, Dato: 010101
Reisemål: kina, Klær: varm, Dato: 020202
Velg reise (1-2): 1
Skriv inn kategori (Reisemål, Klær, Dato): dato
Valgt info: 010101
Vil du endre denne informasjonen? (j/n): j
Skriv inn ny verdi for Dato på reise 1: 030303
Oppdatert reise:
Reisemål: oslo, Klær: kald, Dato: 030303
[hgondal@fedora in1000]$ """



