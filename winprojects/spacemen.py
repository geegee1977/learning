import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)



if response.status_code == 200:
    data=response.json()
    print('There Are ', data.get('number'), 'people in space')
    print('Their names are:')
    for person in data.get('people'):
        print(person['name'], ' is on the craft ', person['craft'])

else:
    print('Error:', response.status_code)
    print('Error message:', response.text)







