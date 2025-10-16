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