#generáljon ki 10 db egy jegyű  nem nulla véletlen számot!
# irassa ki a számok összegét
import random 
osszeg = 0
for a in range(1,11,1):
    velSzam = random.randint(1,9) 
    osszeg += velSzam
    print(velSzam, end=" ")
    print()
print("összeg:",osszeg)
#hány db páros véletlen számot generált ki?
#melyik a legnagyobb véletlen szám?