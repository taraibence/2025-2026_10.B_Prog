# kérjen be egy betüt és egy számot
# 0.5nézze meg van e az adott betü ha van 
# adja meg hány db betü van a szövegben 
szoveg = input("adjon meg egy szövegeget: ")
betu = input("adjon meg egy betüt: ")
db=0

index = 0
while(index <len(szoveg) and szoveg[index] != betu):
    # index = index + 1
    index+=1
    print(index)



for i in szoveg:
    if i ==betu:
        db+=1
print("A szövegben,",db,"",betu,"betű van.")




