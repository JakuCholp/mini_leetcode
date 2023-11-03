from rest_framework import serializers  


class TodecideSerializer(serializers.Serializer):
    solution = serializers.CharField(max_length = 256)
