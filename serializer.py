from rest_framework import serializers
class StudentSer(serializers.Serializer):
    name = serializers.CharField(max_length=50)