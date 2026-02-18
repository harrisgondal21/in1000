"""
Løsning:

1. Prorammet vil kjøre men hvis b<10 får vi error ettersom den siste linjen adder en integer med en str som ikke fungerer.
Det vil fungere dersom print(b,"Hei!"). siden else ikke er skrevet så avslutter programmet.

2. ValueError, kan ikke adderer integer med str
 test:
 a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
print (b + "Hei!")



"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")
"""

Vi får denne feilen hvis vi velger heltall 2 
/usr/bin/python3.13 /home/hgondal/in1000/in1000/kodeforstaalse.py 
Tast inn et heltall! 2
Traceback (most recent call last):
  File "/home/hgondal/in1000/in1000/kodeforstaalse.py", line 34, in <module>
    print(b + "Hei!")
          ~~^~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Process finished with exit code 1

Vi får denne feilen hvis vi velger heltall 12
/usr/bin/python3.13 /home/hgondal/in1000/in1000/kodeforstaalse.py 
Tast inn et heltall! 12

Process finished with exit code 0


"""