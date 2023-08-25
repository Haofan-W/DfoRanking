from django import forms


class CharacterSearchForm(forms.Form):
    character_search_query = forms.CharField(label='Search Character', max_length=20)