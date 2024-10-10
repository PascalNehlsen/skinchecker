import requests
from django.core.cache import cache
from django.shortcuts import render
from django.conf import settings 
import json

def home(request):
    cache_key = 'bitskins_data'
    # Versuch, die Daten aus dem Cache abzurufen
    data = cache.get(cache_key)
    
    if not data:
        headers = {'x-apikey': settings.API_KEY}
        try:
            res = requests.get(settings.API_URL, headers=headers)
            response = json.loads(res.text)
            print("Status Code:", res.status_code)
            if res.status_code == 200:

                if isinstance(response, dict) and 'data' in response:
                    data = response['data']['skins']
                else:
                    data = response if isinstance(response, list) else []
                
                cache.set(cache_key, data, timeout=300)
            else:
                data = [] 
        except requests.RequestException as e:
            print("Error during API request:", e)
            data = []

    return render(request, 'skins/index.html', {'data': data})
