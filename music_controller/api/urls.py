
from django.urls import path
from .views import main

urlpatterns = [
    path('home',main)
]

# this is saying that if we receive a url with no path , call the main function
# after this we will run the server