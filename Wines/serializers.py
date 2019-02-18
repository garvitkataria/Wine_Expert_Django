from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Wine

class WineSerializer(ModelSerializer):

	class Meta:
		model = Wine
		fields = [
			'id',
			'country',
			'description',
			'designation',
			'points',
			'price',
			'province',
			'region_1',
			'region_2',
			'variety',
			'winery',
			'created_at'
			]
		read_only_fields = ['id', 'created_at']