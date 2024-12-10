from rest_framework import serializers

from .models import Room

"""
serializer take our python model and translate the code to a json respond

"""

class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause','votes_to_skip','created_at')
        