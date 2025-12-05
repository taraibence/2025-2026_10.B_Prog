import random

gondolt_szam = random.randint(10,90)
print("melyik kétjegy számra gondoltam?")
probalkozasok =1
print(str(probalkozasok)+". proalkozas:")
szam = int(input("szam: "))

while(szam != gondolt_szam):
    if(szam > 9 and szam < 100):
        if(szam > gondolt_szam):
            print("a szam nagyobb mint a gondolt szám")
        elif(szam < gondolt_szam):
            print("szam kissebb mint a gondolt szám: ")
        probalkozasok+=1
    else:
        print("nem kétjegyü számot adott meg")
        print(str(probalkozasok)+". proalkozas:")
    szam = int(input("probálkozz még egyszer: "))    

print("eltaláltad")  
print("próbálkozások száma")

    #irassa ki hány probalkozasbol
    #figyeljen arra hogyha nem kétjegyu szamot adott meg  ne legyen uj proba hanem figyelmeztesse a felhasználót
    #minden szám bekeresenel irja ki az aktuális proalkozasok szamat





