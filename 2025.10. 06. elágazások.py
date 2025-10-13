# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else: # szam % != 0
    print("páratlan")

# kérjen be a felhasználótól egy számot és mondja meg, hogy 10-zel osztható -e? Ha nem osztható 10-zel írja ki az utolsó számjegyét!
# pl. be: 10 ki: tízzel osztható
# pl. be: 12 ki: tízzel nem osztható, utolsó számjegy 2

if(szam % 10 == 0):
    print("tízzel osztható")
else: 
    print("tízzel nem osztható")
    print("az utolsó számjegy: " + str(szam % 10))

# Kérjen be egy másik számot és írassa ki a két szám reciprokának összegét!

szam2 = int(input("Adjon meg egy másik számot: "))

if(szam != 0):
    if(szam2 != 0):
        rec = 1/szam
        rec2 = 1/szam2
        print(rec+rec2)
    else:
        print("a második számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")

# Adja meg a két szám össegének gyökét!

if(szam + szam2 >= 0):
    print(math.sqrt(szam+szam2))
else:
    print("A két szám összege negatív")

# Logikai operátorok
# and, or, xor, not

if(szam != 0 or szam2 != 0):
        rec = 1/szam
        rec2 = 1/szam2
        print(rec+rec2)
else:
    print("A két szám valamelyik nulla!")

# HF: bool algebra
# HF: Kérjen be a felhasználótól 3 db számot (lehet tört is). Ez a három szám egy háromszög három oldala. 
# 1. Derékszögű-e a háromszög?
# 2. Egyenlőszarú-e a háromszög?
# 3. Szabályos-e a háromszög?

# HF python - ciklusok, loops, iterációk, ...
# Háromszög jellemzőinek vizsgálata

# Felhasználótól bekérés (lebegőpontos számként)
a = float(input("Add meg az első oldalt: "))
b = float(input("Add meg a második oldalt: "))
c = float(input("Add meg a harmadik oldalt: "))

# Háromszög létezésének ellenőrzése (háromszög-egyenlőtlenség)
if a + b > c and a + c > b and b + c > a:
    print("Ez egy létező háromszög.")

    # Derékszögű háromszög vizsgálata (Pitagorasz-tétel)
    oldal = sorted([a, b, c])  # növekvő sorrend: [rövidebb, közép, leghosszabb]
    if abs((oldal[0]**2 + oldal[1]**2) - oldal[2]**2) < 1e-6:
        print("Ez egy derékszögű háromszög.")
    else:
        print("Ez nem derékszögű háromszög.")

    # Egyenlő szárú vizsgálata (kettő oldal megegyezik)
    if a == b or b == c or a == c:
        print("Ez egy egyenlő szárú háromszög.")
    else:
        print("Ez nem egyenlő szárú háromszög.")

    # Szabályos háromszög vizsgálata (minden oldal egyenlő)
    if a == b == c:
        print("Ez egy szabályos háromszög.")
    else:
        print("Ez nem szabályos háromszög.")

else:
    print("A megadott oldalakkal nem létezik háromszög.")



# Generáljon ki három véletlen háromjegyű számot, amelyek 13-al oszthatók! 
# Adja meg az átlaguk!
# Állítsa ezeket sorrendbe!
# Van-e közöttük 4-el végződő?

import random
szam = random.randint (100; 999)
if szam = % 13 == 0 :
    print(szamok)
rendezes = sorted
    print(veletlen szamok, szamok)
    print(rendezes, sorban)