import random


def dice_simulator():
    
    quit_or_not = True

    while quit_or_not:
        x = random.randint(1,6)
        if x == 0:
            print("-------")
            print("|     |")
            print("|  0  |")
            print("|     |")
            print("-------")

        if x == 2:
            print(" ----- ")
            print("|     |")
            print("| 0 0 |")
            print("|     |")
            print(" ----- ")

        if x == 3:
            print(" ----- ")
            print("|  0  |")
            print("|  0  |")
            print("|  0  |")
            print(" ----- ")

        if x == 4:
            print(" ----- ")
            print("| 0 0 |")
            print("|     |")
            print("| 0 0 |")
            print(" ----- ")
        
        if x == 5:
            print(" ----- ")
            print("| 0 0 |")
            print("|  0  |")
            print("| 0 0 |")
            print(" ----- ")

        if x == 6:
            print(" ----- ")
            print("| 0 0 |")
            print("| 0 0 |")
            print("| 0 0 |")
            print(" ----- ")

        user_input = input("You Want To Roll It Again y/n :")
        if user_input=="y".lower():
            continue
        else:
            print("------------------")
            print("Have A Nice Day...")
            break



dice_simulator()




    
