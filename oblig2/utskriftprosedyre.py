'''
x=input("Skriv inn navn:")
y=input("Hvor kommer du fra? ")
print("Hei,",x +"!","Du er fra",y+".") 
'''
def navn():
    x=input("Skriv inn navn:")
    return x
def sted():
    y=input("Hvor kommer du fra? ")
    return y
def hilsen(navn, sted):
    print("Hei,",navn +"!","Du er fra",sted+".")


for i in range(3):
    n=navn()
    s=sted()
    hilsen(n, s)
'''funk navn() tar inn navn, sted() som innput x og y, hilsen setter dem sammen
og printer ut en hilsen. for-løkke kjører prosedyrene 3 ganger.'''


