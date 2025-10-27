import random
while True:
    dice = (input("Press z to roll the dice(if you want to leave,press e) "))
    x = random.randint(1,6)
    if dice == "z":
        print(f"Your number is {x}")
    elif dice == "e":
        con = input("Do you want to leave?(y/n) ")
        if con != "n":
            print("Goodbye!")
            break
    else:
        print("Please press z or e keys!")
        continue