liste_tall=[8,20,63]; liste_tall.append(99)
print(liste_tall[0],liste_tall[2])



prod_tall=1
sum_tall=0
for i in liste_tall:
    sum_tall+=i;
    prod_tall*=i;
print(f"Produktet er {prod_tall} og "  f"summen er {sum_tall}")
liste_tall.append(prod_tall)
liste_tall.append(sum_tall)
print(liste_tall)

liste_navn=[]
for navn in range(3):
    navn=input("Navn: ")
    liste_navn.append(navn.lower())
if "harris" in liste_navn:
    print("Du husket meg!")
else:
    print("Glemte du meg!")

"""/usr/bin/python3.13 /home/hgondal/in1000/in1000/oblig3/lister.py 
8 63
Produktet er 997920 og summen er 190
[8, 20, 63, 99, 997920, 190]
Navn: Harris
Navn: morten
Navn: haretysnfd
Du husket meg!

Process finished with exit code"""







