import random
from time import sleep

dice = range(1,7)


while True:
    roll_dice = input("Roll dice (Y) or (N): ").lower()
    if roll_dice == 'y':
        dice_roll = random.choice(dice)
        if dice_roll == 1:
            sleep(1)
            print("+-------+")
            print("|    0   |")
            print("+-------+")

        if dice_roll == 2:
            sleep(1)
            print('+----------+')
            print('|  0         |')
            print('|         0  |')
            print('+----------+')

        if dice_roll == 3:
            sleep(1)
            print('+-------------+')
            print('|  0             |')
            print('|       0        |')
            print('|            0   |')
            print('+-------------+')

        if dice_roll == 4:
            sleep(1)
            print('+----------+')
            print('|  0     0  |')
            print('|  0     0  |')
            print('+----------+')

        if dice_roll == 5:
            sleep(1)
            print('+--------------+')
            print('|  0         0  |')
            print('|        0       |')
            print('|  0         0  |')
            print('+-------------+')

        if dice_roll == 6:
            sleep(1)
            print('+--------------+')
            print('|   0        0  |')
            print('|   0        0  |')
            print('|   0        0  |')
            print('+--------------+')

    elif roll_dice == 'n':
        print('Thank you for playing')
        break

    else:
        print('Invalid input')