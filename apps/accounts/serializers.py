from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'user_type', 'first_name', 'last_name']


class LoginSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		token['uid'] = user.id
		return token


class SignupSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(
		required=True,
		validators=[UniqueValidator(queryset=User.objects.all())]
	)
	password = serializers.CharField(
		write_only=True, required=True, validators=[validate_password]
	)
	passwordTwo = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = (
			'first_name', 'last_name', 'user_type', 'email', 'password', 'passwordTwo'
		)
		extra_kwargs = {
			'first_name': {'required': True},
			'last_name': {'required': True},
			'email': {'required': True},
			'password': {'required': True},
		}

	def validate(self, attrs):
		if attrs['password'] != attrs['passwordTwo']:
			raise serializers.ValidationError(
				{"password": "Password fields didn't match."}
			)
		return attrs

	@transaction.atomic
	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['email'],
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
			user_type=validated_data['user_type']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user