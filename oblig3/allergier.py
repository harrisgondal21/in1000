"""Oppgaven er: Spør folk om de har allergier og utfgra det velg deres matplan."""
teller = 0
def stopp(): 
    global teller   
    teller = teller + 1 
    input(" trykk enter for å fortsette... eller ctrl+c for å avslutte programmet. ")     
    
"""mat_allergier = {
    "melk": ["yoghurt", "ost", "smør"],
    "nøtter": ["peanøttsmør", "mandler", "cashewnøtter"]}""" #Dette var min første dict


mat_allergier = { #dette var laget med ai for å ha en større liste med allergier og hva man skal unngå så det ikke bare er melk og nøtter
    "melk": ["yoghurt", "ost", "smør", "fløte", "rømme", "is", "melkesjokolade", "kesam", "créme fraiche"],
    "nøtter": ["peanøttsmør", "mandler", "cashewnøtter", "hasselnøtter", "valnøtter", "pistasj", "pekannøtter", "macadamianøtter"],
    "gluten": ["brød", "pasta", "kake", "pizza", "cookies", "bulgur", "couscous", "seitan", "pannekaker"],
    "egg": ["majones", "krem", "omelette", "pannekaker", "kaker", "pai", "meringue", "hollandaise"],
    "fisk": ["laks", "torsk", "sei", "makrell", "sild", "tunfisk", "fiskeboller", "fiskekaker", "kaviar"],
    "skalldyr": ["reker", "krabbe", "hummer", "blåskjell", "østers", "kamskjell", "sjøkreps"],
    "soya": ["tofu", "edamame", "soyasaus", "miso", "tempeh", "soyamelk", "soyabønner"],
    "sesamfrø": ["tahini", "hummus", "sesamolje", "sesamfrø", "halva"],
    "selleri": ["selleristang", "sellerirot", "sellerisalt", "selleribuljonger"],
    "sennep": ["sennepssaus", "dijon", "honningsennep", "sennepsfrø"],
    "lupin": ["lupinmel", "lupinprotein", "lupinbønner"],
    "sulfitt": ["tørket frukt", "vin", "øl", "syltetøy", "sirup"]
}
def allergier():
    allergener = input(f"Har du noen allergier? ").lower()
    if allergener in mat_allergier:
        print(f"Unngå {mat_allergier[allergener]}") #Funksjon som tar allergene input og sjekker om de er i dict og printer hva man skal unngå
    else:
        print("Ingenting å bekymre seg for!") #hvis ikke i dict 

"""
allergier()
stopp()
"""            
try:
    while True:
        allergier()
        stopp()
        #for å la programmet kjøre til brukeren avslutter det selv
        
except KeyboardInterrupt: #dersom ctrl c så avslytter programmet og printer ut hvor mange ganger det har kjørt
    print(f"Programmet avsluttet. Totalt {teller} gjennomføringer.")

"""[hgondal@MonguardWin oblig3]$ /bin/python /home/hgondal/in1000/in1000/oblig3/allergier.py
Har du noen allergier? sulfitt
Unngå ['tørket frukt', 'vin', 'øl', 'syltetøy', 'sirup']
 trykk enter for å fortsette... eller ctrl+c for å avslutte programmet. fisk
Har du noen allergier? fisk
Unngå ['laks', 'torsk', 'sei', 'makrell', 'sild', 'tunfisk', 'fiskeboller', 'fiskekaker', 'kaviar']
 trykk enter for å fortsette... eller ctrl+c for å avslutte programmet. ^CProgrammet avsluttet. Totalt 2 gjennomføringer.
[hgondal@MonguardWin oblig3]$ """