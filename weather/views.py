from django.shortcuts import render
from weather_app import settings

import json

import urllib.request as rq


def index(request):
    if request.method == 'POST' and request.POST['city']:
        city = request.POST['city']

        source = rq.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                            city + '&appid=' + settings.WEATHER_API_KEY).read()

        list_of_data = json.loads(source)

        data = {
            'results': True,
            'city': city,
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ',  ' + str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp'] - 273),
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
        }
        print(data)

    else:
        data = {
            'results': False,
        }

    return render(request, 'weather/index.html', data)
