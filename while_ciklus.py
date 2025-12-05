# elöltesztelős ciklus
# while ciklus

# -nem tudjuk, hogy hányszor fog lefutni (hányszor ismétel)
# feltételhez kötött
# -akkor ismétel, ha a feltétel igaz


# while(feltétel):
#     utasítások (szekvencia)


#generáljon véletlen számokat [0,10 között], amíg 0-át mem kapunk.

import random

velszam = random.randint(0,10)
print(velszam)
while(velszam != 0):
    velszam = random.randint(0,10)
    print(velszam,end=" ")
print()



#kerjen be számokat addig ameddig nullát nem adnak meg!


osszeg = 0
db = 0
szam = int(input("adjon meg egy számot(0-nál kilép): "))
# osszeg += szam 
# db += 1
while(szam != "0") :
      osszeg += szam
      db += 1
      szam = int(input("adjon meg egy számot(0-nál kilép): "))
print(round(osszeg/db,2))
    

# adott egy szöveg . adja meg hogy ven e benn x betü !


szoveg = (input("írjon be egy szöveget: "))
while(szoveg != "x"):
    print()
