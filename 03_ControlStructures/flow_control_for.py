for num in (1,2,3,5,7,10,15,-10,-11,-32, 50, 100):
    if num >= 50:
        break
    else:
        if num % 2:
            print(num)
        else:
            continue
        print("Odd printed")

for letter in "Perrito bonito":
    print(letter)
else:
    print(" :)")