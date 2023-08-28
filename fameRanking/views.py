from django.shortcuts import render
from decouple import config


# Create your views here.
def indexView(request):
    context = {}
    return render(request, "fameRanking/index.html", context)


# def characterFameRankingView(request):
#     context = {}
#     if request.method == 'GET':
#         api_key = config('API_KEY')
