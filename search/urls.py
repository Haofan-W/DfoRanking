from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.indexView, name="index"),
    path("search", views.characterResultView, name="character_result"),
]
