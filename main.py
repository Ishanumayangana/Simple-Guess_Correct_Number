import random

def guess_number():
    Hidden_number = random.randint(1, 10)
    your_input = 0

    while your_input != Hidden_number:
        your_input = int(input("Enter another number :"))

        if your_input < Hidden_number:
            print("Too low.Try again")

        if your_input > Hidden_number:
            print("Too high.Try again")

    print("You are winner")

guess_number()



# Hidden_number = random.randint(1,10)
# your_input = 0
#
# while your_input != Hidden_number:
#     your_input = int(input("Enter another number :"))
#
#     if your_input < Hidden_number :
#         print("Too low.Try again")
#
#     if your_input > Hidden_number :
#         print("Too high.Try again")
#
# print("You are winner")