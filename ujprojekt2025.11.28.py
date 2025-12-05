#egy szövegben hány db szóköz van?

# szoveg = "géza kék az ég"
# print(szoveg)
# db = 0

# for karakter in szoveg:
#     if(karakter == " "):
#         db +=1

# print (db, "db szóköz  van a szövegben") 



#adja meg hogy a szövegben van e cs betü (két karakter kell egymás mellett)
#pl. alma, kacsa, filc      

szo = input("adjon meg egy szoveget!: ")

index = 0
while(index<len(szo)-1 and (szo[index] != "c" or szo[index+1] != "s")):
    index += 1
print(index) 
if(index < len(szo)-1):    
    print("van benne cs")
else:
    print("nincs benne cs")

# De morgan azonossag