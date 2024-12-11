from django.shortcuts import render
from rest_framework import generics
from .serializers import Roomserializer
from .models import Room



# from django.http import HttpResponse


# Create your views here.
# this is where we will write all our endpoint e.g /hello . it is founfd after the /

# def main(request):
#     return HttpResponse("<h1>hello</h1>")
# now we will configure the url to nkow actually how to get to this endpoint, wethwe is /hello or etc. it is done in the urls file
# we will create a file urls.py in the api app for it to store all the url local to that app

# create an api view that will alout us to view the list of room

class RoomView(generics.CreateAPIView): # this will alow us to create and view room
    queryset = Room.objects.all()
    serializer_class = Roomserializer 