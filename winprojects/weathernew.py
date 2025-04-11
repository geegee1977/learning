import requests

url="http://api.weatherapi.com/v1/current.json"

response = requests.get(url, params={
    'key': '5e559dc644fe4a63b4c161454251104',
    'q': 'Edinburgh',
    'aqi': 'no'
})

weather_json = response.json()

if response.status_code == 200:
  temp = weather_json.get('current').get('temp_c')
  location = weather_json.get('location').get('name')
  print('in ', location, ' it is ', temp, ' degrees Celsius')

  
   # print(response.json())
# print(response.text)
 #print(response.json(location('name')), ' is in ', response.json(location('region')))
# print(response.json()['current']['temp_c'])
# print(response.json()['current']['temp_f'])

else:
    print("Error:", response.status_code)
