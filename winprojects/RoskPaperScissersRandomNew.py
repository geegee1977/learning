import random

computerchoice = random.choice(['rock','paper','scissors'])

user = input("Chose rock, paper, scissors: ")


print("You Chose: " + user)
print("Computer Chose: " + computerchoice)

if user == computerchoice:
    print("It's a Draw")
elif user == "scissors" and computerchoice == "paper":
    print("You Win")
elif user == "paper" and computerchoice == "rock":
    print("You Win")
elif user == "rock" and computerchoice == "scissors":
    print("You Win")
else:
    print("You Lose")

