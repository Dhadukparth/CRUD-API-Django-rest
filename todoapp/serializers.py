from rest_framework import serializers

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='Enter id')
    title = serializers.CharField(label='Enter title')
    description = serializers.CharField(label='Enter description')