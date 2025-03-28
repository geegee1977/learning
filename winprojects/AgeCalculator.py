question = "How old Are you? "

Age = int(input(question))

Decades = Age//10

Years = Age%10

print("You are " + str(Decades) + " decades old\nand " + str(Years) + " year(s) old.")
