
number = int(input('How Many Expenses do you have?: '))

expenses = []

for i in range(number):
    expenses.append(float(input('Enter Expense '+str(i)+': ')))

total = sum(expenses)



print(total)
print('You Spent £',total,sep = '')
print('You Spent £',total)