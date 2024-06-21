from rest_framework import serializers
from base.models import Item, administration, student
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # or specify fields explicitly

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = administration
        fields = '__all__'
