from django.urls import path

from . import views

app_name = "fameRanking"
urlpatterns = [
    path("", views.indexView, name="index"),
]