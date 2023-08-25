from django.shortcuts import render
import requests
from decouple import config

from search.forms import CharacterSearchForm


def indexView(request):
    context = {}
    return render(request, "search/index.html", context)


def characterResultView(request):
    context = {}
    if request.method == 'GET':
        form = CharacterSearchForm(request.GET)
        if form.is_valid():
            api_key = config('API_KEY')
            character_search_query = form.cleaned_data['character_search_query']

            api_url = f'https://api.dfoneople.com/df/servers/cain/characters?characterName={character_search_query}&wordType=full&apikey={api_key}'
            response = requests.get(api_url)

            if response.status_code == 200:
                character = response.json()
            else:
                character = None
            context = {
                "character": character,
            }
    return render(request, "search/characterResult.html", context)
