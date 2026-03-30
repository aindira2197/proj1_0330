import random

son = random.randint(1, 100)

while True:
    taxmin = int(input("Sonni toping (1-100): "))
    
    if taxmin < son:
        print("Kattaroq son kiriting")
    elif taxmin > son:
        print("Kichikroq son kiriting")
    else:
        print("Topdingiz! 🎉")
        break
