# lebegőpontos - float - tört
a = 1.25
b = float(input("adjon meg egy tizedes törtet: "))
print(b*4)   

#generáljon ki [1,10] kozotti tort számot 2 tizedesjegyre
#pl. 1.36, 2.30


#c = random.randit(100,999)/100
c = random.random() # [0,1[
print(round(c,2))

# szövegkezelés
szoveg = input("adjon meg egy szöveget: ")
print(szoveg)
print("szöveg hossza: ",len(szoveg))
print("első karakter" ,szoveg[0])
# szöveg karakter lánc
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

a = (random.randit(97,122))

#HF
nev = input("adja meg a keresztnevét: ")
hossz = len(nev)
if hossz >= 3:
    kod1 = ord(nev[0])
    kod2 = ord(nev[1])
    kod3 = ord(nev[2])
    jelszo = kod1 * kod2 * kod3     
elif hossz == 2:
    kod1 = ord(nev[0])
    kod2 = ord(nev[1])
    jelszo = kod1 * kod2 * hossz
else:
    kod1 = ord(nev[0])
    jelszo = kod1 * (hossz ** 3)
print("a jelszava:", jelszo)
