#rndom is a library
import random
print("This is dice stimulator")
x = "y"
if(x=="q"):
    exit()
while x == "y":
    number = random.randint(1,6)
    #random.randint is used to select random numbers from the starting range to the end
    if number == 1:
        print("----------")
        print("|        |")
        print("|    *   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|  *     |")
        print("|        |")
        print("|      * |")
        print("----------")
    if number == 3:
        print("----------")
        print("| *      |")
        print("|    *   |")
        print("|       *|")
        print("----------")
    if number == 4:
        print("----------")
        print("| *   *  |")
        print("|        |")
        print("| *   *  |")
        print("----------")
    if number == 5:
        print("----------")
        print("|*      *|")
        print("|    *   |")
        print("|*      *|")
        print("----------")
    if number == 6:
        print("----------")
        print("|*       *|")
        print("|*       *|")
        print("|*       *|")
        print("----------")
    x = input("press y to roll again")
    











