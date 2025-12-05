"""

#Ciklusok - ismétlés -loop 

# számlálós - for ciklus
#végig megy a megadott  elemeken vagy intervallummon!
for elem in range(mettol, meddig hányasával):
    ismétlendő folyamat

for karakter in szöveg:
    ismétlendő folyamat

# tesztelős - while

"""
import random as r
for i in range(1,11,1):
    print(i, end=" ")
# ELSŐ 10 DB PÁROS SZÁM
print()

for elem in range (0,19,2):
    print(elem, end =" ")
print()

# szöveg betüi közé vesszőt
szoveg = "kalapács"
print (szoveg)
for karakter in szoveg:
    print(karakter, end= ",")
print()

# szoveg[0]
# szoveg[1]
# szoveg[2]
for index in range(0, len(szoveg)-1, 1):
    print(szoveg[index]+",",end="")
    print(szoveg[-1])

for a in range(32,50, 4):
    print(a, end=" ")
print()

for b in range(10,0,-1):
    print(b, end=" ")
print()
ujszoveg = ""
for index in range(len(szoveg)-1, -1, -1):
    ujszoveg += szoveg[index]
    # print(szoveg[index],end="")
print()

n = len(szoveg)
for index in range(0, n, 1):
    print(szoveg[n-index-1],end="")
print()


# írass ki a szöveget az indexével társítva!
# BE: kalapács
# KI :(1k 2a 3l.stb)
for index in range(0, n, 1):
    print(str(index+1)+szoveg[index], end =" ")
print()
    # írasson ki 5 db véletlen kaaktert a szövegböl

for db in range(0,5,1):
    szam = r.randint(0,n-1)
    print(szoveg[szam],end=" ")
print()

print(ujszoveg)
# hf 17-21 feladat
