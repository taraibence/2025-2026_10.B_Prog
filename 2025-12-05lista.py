"""
lista - ninamikus,
- tudunk bele uj elemet rakni, ezzel nő az elem száma
- tudunk belőle törölni, ezzel csökken az elemszáma
-lekérhetö bármelyik eleme
- mósosítható bármelyik eleme
deklarálás + inicializálás:
létrehozás + kezdőérték adás:
lista_neve = []
uj elem hozzáadása:
lista_neve.append(ujelem)
elem torlese:
lista_neve.remove(elem)
beégetett lista:
lista_neve = [3,2,5,7,1]
lista hossza :
len(lista_neve)
"""
szamok = [3,2,5,7,1]

print(szamok)
szamok.append(12)
print(szamok)
szamok.remove(3)
print("elsoelem:", szamok[0])
print("lista hossza: ", len(szamok))
print("utolso elem:", szamok[len(szamok)-1])
#print("utolso elem:", szamok[-1])

#hazi feladat
#tolts fel egy 13 elemu listat [0,20] közötti vélettlen számmal
#szamok atlaga
#hany db paros szam van a listaban
# van-e benne nulla



# a szövegben van e "sz" betü?
szoveg = "poros"
db="sz"  #duplabetű
print(szoveg)
# if "sz" in szoveg:
#     print("benne van az sz betü")
# else:
#     print("nincs benne sz betű")

index =0
while(index<len(szoveg)-1 and (szoveg[index]== db[0] and  szoveg[index+1] == db[1])):
    index+=1
if(index<len(szoveg)-1):
    print("benne van az ", db, "  sz betü")
else:
    print("nincsen benne az", db," sz betü")



#palidom-e
ujszoveg=""
for index in range(len(szoveg)-1, -1, -1):
    ujszoveg+=szoveg[index]
if ujszoveg == szoveg:
    print("a szoveg palinrom")
else:
    print("a szoveg nem palidrom")


j = 0
while (j<len(szoveg)/2 and szoveg[j]==szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print(" a szoveg palidom")
else:
    print("a szoveg nem palidom")