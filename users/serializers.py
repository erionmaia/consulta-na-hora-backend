from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'user_type',
                  'crm', 'specialty', 'birth_date', 'phone', 'password', 'password2')
        extra_kwargs = {
            'crm': {'required': False},
            'specialty': {'required': False},
            'birth_date': {'required': False},
            'phone': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        
        if attrs['user_type'] == User.UserType.DOCTOR:
            if not attrs.get('crm'):
                raise serializers.ValidationError({"crm": "CRM é obrigatório para médicos."})
            if not attrs.get('specialty'):
                raise serializers.ValidationError({"specialty": "Especialidade é obrigatória para médicos."})
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'user_type',
                  'crm', 'specialty', 'birth_date', 'phone')
        read_only_fields = ('username', 'user_type')

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password": "As senhas não coincidem."})
        return attrs 