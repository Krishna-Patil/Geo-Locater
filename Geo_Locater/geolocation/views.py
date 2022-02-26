from django.shortcuts import render
import json
import requests
import os


def index_view(request):
    secret_key = os.environ.get('SECRET_KEY')
    res = requests.get(f"http://api.ipstack.com/check?access_key={secret_key}")
    json_res = json.loads(res.content)
    ip = json_res['ip'],
    country = json_res['country_name'],
    city = json_res['city'],
    state = json_res['region_name'],
    continent = json_res['continent_name']
    context = {
        'ip': ip,
        'country': country,
        'city': city,
        'state': state,
        'continent': continent
    }
    return render(request, 'index.html', context)
