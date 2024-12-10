from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # this will generate a random code of k lenght that contain only Uppercase ascii character
        if Room.objects.filter(code=code).count == 0: # to verify if the code is not existing
            break
    return code    

# Create your models here.

# part2  creating api endpoin

# creating a table is creating a model

"""
in a standart db we will have a table with row and column
in django creating a table is creating a model. django allow us to write python code and he will interprete that to make db operation
it is a layer of abstraction for us to write database

"""
# a room model. we want to group user in a room9 one person create a romm play a musique and others join that room to manipulate the misic too

class Room(models.Model):
    code = models.CharField(max_length=8, default="" , unique=True) # what is in bracket is the constrain to that field, unique=True here means that a Romm can only have one code
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

