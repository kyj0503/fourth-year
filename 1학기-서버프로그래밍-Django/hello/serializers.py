from rest_framework import serializers
from .models import Hacsam

class HacsamSerializer(serializers.Serializer):
    class Meta:
        model = Hacsam
        fields = ['id', 'name', 'birthday', 'stdnum', 'major', 'email']
        read_only_fields = ['user']