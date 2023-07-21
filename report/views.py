from django.shortcuts import render
from .forms import CityForm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


def index(request):
    owm = OWM('e896280004e6a25cf7074d8597dbf873')
    mgr = owm.weather_manager()
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            city = form.cleaned_data.get("city")
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temperature = w.temperature('celsius')
            temperature = temperature['temp']
            wind = w.wind()['speed']
            status = w.detailed_status
        context = {
                'city': city,
                'temperature': temperature,
                'wind': wind,
                'status': status
            }
    else:
        context = {'form': CityForm}
    return render(request, 'html/index.html', context)


def weather(request, city):

    pass
