# Változó deklarálása és inicializálása
# Változó létrehozása és kezdőérték adása
# valtozoNev = "kezdoertek"
nev = "Tarai Bence"
osztaly = '10.b'
datum = "2025.09.08"
# "'"
# '"'
print(nev,osztaly, datum,sep="\n")

# operátor

# konkatenálás, concat, összefűzés - két szöveget!!!!! 
osszefuzes = nev+osztaly
print(osszefuzes)

#többszörözées
soknev= nev 
print(soknev)

"""
-Szöveg -string -str
-karakter
-szám - egész lebegőpontos (tört)(float)
-logikai -true, false
"""

aEgesz = 123
bTort=34.23
szSzam = "12"
logikai =True

print("a Egész:", aEgesz)
print("b Tört:", bTort)
print("sz Szam:",szSzam)
print("logikai",logikai)

# Egesz operatorok
print("a + 2=",aEgesz + 2)
print("a - 2=",aEgesz - 2)
print("a * 2=",aEgesz * 2)
print("a / 2=",aEgesz / 2)

# Div - egeszrész, Mód - modulus(maradék)
# div - //
# mod - %

print("a div 8=", aEgesz // 8)
print("a div 8=", aEgesz % 8)

print(int(szSzam)+aEgesz)
print(str(aEgesz)+szSzam)

print(aEgesz+int(szSzám))
print(szSzám+str(aEgesz))

15%7