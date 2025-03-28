# Get detrails of loan

money = float(input('how much money do you owe? '))

apr = float(input('what is the APR %? '))

payment = float(input('How much will your monthly payment be? '))

months = int(input('How Many Monthes will you pay back? '))

for i in range(months):
    money = money - payment
    money = round(money - (money/100*apr),2)
    print('After ',i,'mnths You now only have ',money,'left to pay')


print('You now only have ',money,'left to pay')

