from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'role',
            'is_active', 'date_joined', 'last_login'
        ]
        read_only_fields = ['id', 'is_active', 'date_joined', 'last_login']


class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=[('student', 'Student'), ('counsellor', 'Counsellor')])

    def validate_role(self, value: str) -> str:
        # Explicitly disallow creating admin via API
        if value == 'admin':
            raise serializers.ValidationError('Admin accounts cannot be created via API.')
        return value

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['role'] = self.validated_data.get('role')
        return data

    def save(self, request):
        user = super().save(request)
        user.role = self.validated_data['role']
        user.save(update_fields=['role'])
        return user
