#kérjen be egy számot és döntse el, hogy páros vagy páratlan

szam = int(input("adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")    

    # kérjen ba a felhasználotol egy számot es mondja meg hogy, 10-zel osztható e? Ha nem osztható 10-zel írja ki az utolsó számjegyét! 
    #pl. be :10 ki: tízzel osztható
    #pl. be : 12ki: tízzel nem osztható, utolsó számjegy 2 

if(szam % 10 == 0):
    print("tízzel oszthato")
else:
     print("tízzel nem oszthato")
     print("az utolsó számjegy:" + str(szam % 10))


# kérjen be egy másik számot és írassa ki a át szám reciprokának összegét!
szam2 = int(input("adjon meg egy számot!"))

if(szam != 0):
    if(szam2 != 0):
        rec = 1/szam
        rec2 = 1/szam2
        print(rec+rec2)
    else:
            print("a második számnak nincs reciproka")
else:
   print("az elsö számnak nincs reciproka") 

#adja meg a két szám összegének a gyökét


if(szam + szam2 >= 0):
    print(math.sqrt(szam+szam2))
else:
    print("a két szám összege negatív")

    # pythonba - ciklusk, loops, iterációk, ...

    #generáljon ki három véletlen háromjegyű számot , amely 13-al oszthatók!
    #állítsa ezeket sorrenbe!
    #adja meg az átlaguuk!
    #van-e közöttük-el végződö? 

#ottho tessék lemásolni a github-os repository tartalmát (pull)
#házi feladar elkészítése
#add, commit , push 

#páros kétjegyű [5,44]*2
#100/7 = 7,6
# 999/13 = 76,8
a = random.randit(8,76)*13
b = random.randit(8,76)*13
c = random.randit(8,76)*13

szamjegy = int(input("adjon meg egy számjegyet"))

print (a,b,c)

if(a % 10 == szamjegy or b == szamjegy or c % 10 == szamjegy):
    print("van közte "+str(szamjegy)+"-re végződő")
else:
    print("nincs közte "+str(szamjegy)+"-re végződő")



