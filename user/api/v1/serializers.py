from rest_framework import serializers
from user.models import HHGH


class HHGHSerializer(serializers.ModelSerializer):
    class Meta:
        model = HHGH
        fields = "__all__"
