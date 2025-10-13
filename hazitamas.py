a = float(input("Adjon meg a számot: "))
b = float(input("Adjon meg a számot: "))
c = float(input("Adjon meg a számot: "))

if(a + b > c and a + c = b and b + c = a):
    print("A háromszög megszerkezhető")
else:
    print("A háromszög nem megszerkezhető")

if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
    print("Derékszög a háromszög")
else:
    print("Nem derékszög a háromszög")

if(a == b and b == c and a == c):
    print("Szabályos háromszög")
else:
    print("Nem szabályos háromszög")

