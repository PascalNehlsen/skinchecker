import requests
from django.shortcuts import render
from django.conf import settings  # Django-Einstellungen importieren


def home(request):
    # Beispiel-API-URL und API-Key (bitte entsprechend anpassen)
    api_url = settings.API_URL # Ersetze dies durch deine API-URL
    api_key = settings.API_KEY  # Ersetze dies durch deinen API-Key
    
   # Anfrage an die API
    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})

    print("Status Code:", response.status_code)

    try:
        data = response.json()  # Hole die JSON-Daten
    except ValueError as e:
        print("JSON Decode Error:", e)
        data = []

    return render(request, 'skins/index.html', {'data': data})  # Übergebe data als Liste