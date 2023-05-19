from rest_framework import serializers
from .models import api1


class API1Serializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, required=False, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, required=False, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = api1
        exclude = []
        read_only_fields = ['id', ]

