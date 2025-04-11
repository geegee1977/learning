current_movies={'Jaws':'18:30',
               'slasher':'17:30',
               'goonies':'20:00'}

print('The current mvoies are')
for yu in current_movies:
    print(yu)

user_choice = input('enter the movie name:')
                    
showtime = current_movies.get(user_choice)

if showtime:
    print('showtime for movie:', user_choice,'is ', showtime)
elif showtime == None:
    print('movie not found')




