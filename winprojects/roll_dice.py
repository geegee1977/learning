import random

roll = random.randint(1,6)

guess = int((input('Guess the dice roll:\n')))

if roll==guess:
    print ("the computer rolled a " + str(roll) + " you were right")
else:
    print ("the computer rolled a " + str(roll) + " you were wrong")