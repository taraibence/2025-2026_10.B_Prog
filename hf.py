import math

# 1
a = 7
b = 11
print(a)
print(b)
print(2 * a + 2*b)
print(a * b)
# 2
c = 11
print(c * 2)
print(2 * c* 3.14)
print(c * c* 3.14)
# 3
d = 3
e = 6
f = 5
index = (d + e + f) /2
print("kerület: " + str(d + e + f))
print("területe: " + str(math.sqrt(index * ((index - d) * (index - e) * (index - f)))))
# 4
a = 8
print("Háromszög magassága: " + str(math.sqrt(7 ** 2 + (7/2) ** 2)))
# 5
a = 2
index = (math.sqrt(a ** 2 + a ** 2))
print("A lap átlója: " + str(index))
print("A kocka átlója: " + str(math.sqrt(index ** 2 + a ** 2)))
# 6
vezeteknev = str(input("Adja meg a vezetéknevét: "))
keresztnev = str(input("Adja meg a keresztnevét: "))
print(vezeteknev, end=" ")
print(keresztnev)
# 7
a = int(input("Adjon meg egy számot: "))
if(a % 2 == 0):
    print("Páros a szám")
else:
    print("Nem páros a szám")
# 8
a = int(input("Írjon egy 1-5 egy számot: "))
if(a == 1):
    print("Elégtelen")
elif(a == 2):
    print("Elégséges")
elif(a == 3):
    print("Közepes")
elif(a == 4):
    print("Jó")
else:
    print("Jeles")
# 9
a = int(input("Hány fokos a víz: "))
if(a < 0):
    print("Szilárd")
elif(a >= 100):
    print("Gáz")
else:
    print("Folyékony")
# 10
a = 4
b = 7
c = 2
if(a + b > c and a + c > b and b + c > a ):
    print("Megszerkezthető a háromszög")
else:
    print("Nem megszerkezhető a háromszög")
# 11
a = 456
print("Ennyi celsius: " + str((a - 32) * 5 / 9))
# 12
a = 125
print("Ennyi farenheit: " + str(a * (9 / 5) + 32))
# 13
a = int(input("Adjon meg a másodpercet: "))
print("Óra: " + str(a // 3600))
print("Perc: " + str((a % 3600) // 60))
print("Másodperc: " + str(a % 60))
# 14
a = str(input("Adjon meg egy szöveget: "))
b = len(a)
c = a[b - 1]
print("Az utolsó karakter: " + str(c))
# 15
a = str(input("Adjon meg egy szöveget: "))
b = len(a)
c = a[b - 1]
d = a[0]
if(c == d):
    print("Az első és az utolsó karakter megegyezik")
else:
    print("Az első és az utolsó karakter nem egyezik meg")
# 16
a = str(input("Adjon meg egy szöveget: "))
b = len(a)
for i in range(1, b, 2):
    print(a[i])
# 17
a = str(input("Adja meg a szöveget: "))
b = len(a) - 1
c = ""
while b >= 0:
    c = c + a[b]
    b = b - 1
print(str(c))
# 18
a = str(input("Adja meg a szöveget: "))
b = len(a) - 1
c = ""
while b >= 0:
    c = c + a[b]
    b = b - 1
print(c, end=" ")
print(c, end=" ")
print(c, end=" ")
# 19
print()
a = str(input("Adja meg a szöveget: "))
b = len(a) - 1
c = ""
while b >= 0:
    if b % 2 == 0:
        c += a[b]
    b = b - 1
print(c)
# 20
a = str(input("Adja meg a szöveget: "))
b = len(a) - 1
c = ""
while b >= 0:
    if a[b] != " ":
        c = a[b] + c
    b = b - 1
print(c)


