from rest_framework import serializers

from api.models import Order, Driver, Client


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
	client = UserSerializer()
	driver = DriverSerializer()

	class Meta:
		model = Order
		# exclude = ['created_at', 'updated_at']
		fields = '__all__'
