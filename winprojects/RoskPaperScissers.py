red = input("Chose for Red: ")
blue = input("Chose for Blue: ")

if red == blue:
    print("It's a Draw")
elif red == "scissors" and blue == "paper":
    print("Red Wins")
elif blue == "scissors" and red == "paper":
    print("Blue Wins")
elif red == "paper" and blue == "rock":
    print("Red Wins")
elif blue == "paper" and red == "rock":
    print("Blue Wins")
elif red == "rock" and blue == "scissors":
    print("Red Wins")
elif blue == "rock" and red == "scissors":
    print("Blue Wins")