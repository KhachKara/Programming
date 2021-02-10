import requests
import geocoder
import datetime


API_KEY = '1d5f5a3734be792803f3af4426182284'
HOST = 'https://api.openweathermap.org/data/2.5/'
DAYS = [
    {'num': 0, 'title': 'понедельник', 'active': False, 'color': '#FFE739', 'order': [0, 1, 2, 3, 4, 5, 6], 'temp': 0,'type': '-'}, 
    {'num': 0, 'title': 'вторник', 'active': False, 'color': '#FFE739', 'order': [1, 2, 3, 4, 5, 6, 0], 'temp': 0,'type': '-'}, 
    {'num': 0, 'title': 'среда', 'active': False, 'color': '#FFE739', 'order': [2, 3, 4, 5, 6, 0, 1], 'temp': 0,'type': '-'}, 
    {'num': 0, 'title': 'четверг', 'active': False, 'color': '#FFE739', 'order': [3, 4, 5, 6, 0, 1, 2], 'temp': 0,'type': '-'}, 
    {'num': 0, 'title': 'пятница', 'active': False, 'color': '#FFE739', 'order': [4, 5, 6, 0, 1, 2, 3], 'temp': 0,'type': '-'}, 
    {'num': 0, 'title': 'суббота', 'active': False, 'color': '#FFE772', 'order': [5, 6, 0, 1, 2, 3, 4], 'temp': 0,'type': '-'}, 
    {'num': 0, 'title': 'врскресенье', 'active': False, 'color': '#FFE772', 'order': [6, 0, 1, 2, 3, 4, 5], 'temp': 0,'type': '-'}, 
]

def today():
    g = geocoder.ip('me')
    city = g.city
    lat = g.lat
    lon = g.lng
    # print(city, lat, lon)
    req = requests.get(f"{HOST}weather?lat={lat}&lon={lon}&units=metric&lang=ru&appid={API_KEY}").json()
    res = {
        'city': req['name'],
        'description': req['weather'][0]['description'],
        'temp': int(round(req['main']['temp'])),
        'feels': str(req['main']['feels_like']) + ' C',
        'pressure': round(req['main']['pressure'] / 1000 * 750, 2),
        'wind': req['wind']['speed']
    }
    return res


def week():
    today = datetime.datetime.today()
    DAYS [today.weekday()]['actibe'] = True
    for i in DAYS:
        if i['order'][0] == today.weekday():
            order = i['order']
    g = geocoder.ip('me')
    city = g.city
    lat = g.lat
    lon = g.lng
    
    req = requests.get(f'{HOST}onecall?/exclude=daily&lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ru').json()
    res = [DAYS[i] for i in order]
    for i in req['daily']:
        index = req['daily'].index(i)
        if index == 7:
            break
        res[index]['temp'] = i['temp']['day']
        res[index]['type'] = i['weather'][0]['description']
    return res 

for i in week():
    print(i)
    
