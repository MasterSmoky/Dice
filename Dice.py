import random

while True:

    choices = ["1", "2", "3", "4", "5", "6"]

    dice = random.choice(choices)

    player = input("Do you wanna roll the dice ?")

    if player != "Yes".lower():
        continue
    print("dice result :", dice)
