from rest_framework import serializers
from .models import Ipoteka


class IpotekaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipoteka
        fields = "__all__"