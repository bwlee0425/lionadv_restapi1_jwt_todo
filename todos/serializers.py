from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from .models import Todo

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'content', 'created_at', 'updated_at','is_completed')
        read_only_fields = ('created_at','updated_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        # Todo.objects.create(......) -> super.create
        return super().create(validated_data)
