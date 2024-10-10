import requests
from django.core.cache import cache
from django.shortcuts import render
from django.conf import settings 
import json

def home(request):
    cache_key = 'bitskins_data'
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
                
                # Setze die Daten in den Cache für 300 Sekunden
                cache.set(cache_key, data, timeout=300)
            else:
                data = [] 
        except requests.RequestException as e:
            print("Error during API request:", e)
            data = []
    
    limited_data = data[:50] 
    
    return render(request, 'skins/index.html', {'data': limited_data})
