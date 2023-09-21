#1. feladat Kérjünk be a user-től 2db egész számot és vizsgáljuk meg azt hogy: melyik a nagyobb illetve ha egyenlőek akkor azt irja ki.
"""
szam1 = int(input("Adj meg egy számot"))

szam2 = int(input("Adj meg egy számot"))

if szam1 > szam2:
    print("Az első szám nagyobb mint a második")
if szam1 < szam2:
    print("A második szám nagyobb mint az első")
if szam1 == szam2:
    print("A 2 szám egyenlő")
"""



#2. feladat 5db egész szám bekérése megvizsgáljuk hogy + vagy - ki kell irnia hogy 20-nál nagyobb vagy kisebb. számold meg hány olyan van az 5 közül hogy pozitiv és 20-nál nagyobb.


a = int(input("Adj meg egy számot"))
b = int(input("Adj meg egy számot"))
c = int(input("Adj meg egy számot"))
d = int(input("Adj meg egy számot"))
e = int(input("Adj meg egy számot"))

bonusz == 0


if a > 0:
    print("Az 1. szám pozitív")
else:
    print("Az 1. szám negatív")

if a < 20:
    print("Az 1. szám kisebb mint húsz")
elif a > 20:
    print("Az 1. szám nagyobb mint 20")
    
if b > 0:
    print("A 2. szám pozitív")
else:
    print("A 2. szám negatív")

if b < 20:
    print("A 2. szám kisebb mint húsz")
elif b > 20:
    print("A  2. szám nagyobb mint 20")
    
if c > 0:
    print("A 3. szám pozitív")
else:
    print("A 3. szám negatív")

if c < 20:
    print("A 3. szám kisebb mint húsz")
elif c > 20:
    print("A 3. szám nagyobb mint 20")
    
if d > 0:
    print("A 4. szám pozitív")
else:
    print("A 4. szám negatív")

if d < 20:
    print("A 4. szám kisebb mint húsz")
elif d > 20:
    print("A 4. szám nagyobb mint 20")
    
if e > 0:
    print("Az 5. szám pozitív")
else:
    print("Az 5. szám negatív")

if e < 20:
    print("Az 5. szám kisebb mint húsz")
elif e > 20:
    print("Az 5. szám nagyobb mint 20")
    
if a > 20:
    bonusz = bonusz + 1
    
if b > 20:
    bonusz = bonusz + 1
    
if c > 20:
    bonusz = bonusz + 1
    
if d > 20:
    bonusz = bonusz + 1
    
if e > 20:
    bonusz = bonusz + 1

