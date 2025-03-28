import random

user = input("Chose rock, paper, scissors: ")
computernumber = random.randint(1,3)

if computernumber == 1:
    computerchoice = "rock"
elif computernumber == 2:
    computerchoice = "scissors"
else:
    computerchoice = "paper"

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

