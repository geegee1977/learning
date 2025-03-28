current_movies={'Jaws':'18:30',
               'slasher':'17:30',
               'goonies':'20:00'}

print('The current mvoies are')
for yu in current_movies:
    print(yu)

user_choice = input('enter the movie name:')
                    

print(current_movies[user_choice])

