from django.urls import path
from rango import views

app_name = "rango"

urlpatterns = [
    path('', views.index, name='index'), # handles rest of URL string after urls.py in other folder
    # maps empty string to index view
    ]
