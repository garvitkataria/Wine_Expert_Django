from rest_framework.views import APIView
from .models import Wine
from .serializers import WineSerializer

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework import status	

from django.db.models import Q

class WineSizeView(APIView):
	def get(self, request, format=None):
		wines = Wine.objects.all().count()
		return Response(wines)

class WineView(APIView):
	def get(self, request, format=None):
		start = int(request.GET.get('starting'))
		end = int(request.GET.get('ending'))
		wines = Wine.objects.all()[start:end]
		serializer = WineSerializer(wines, many=True)
		return Response(serializer.data)

class WinePriceView(APIView):
	def get(self, request, format=None):
		wines = Wine.objects.order_by('price')
		serializer = WineSerializer(wines, many=True)
		return Response(serializer.data)

class WinePointsView(APIView):
	def get(self, request, format=None):
		wines = Wine.objects.order_by('points')
		serializer = WineSerializer(wines, many=True)
		return Response(serializer.data)

class WineCountryProvinceRegionSizeView(APIView):
	def get(self, request, format=None):
		value = request.GET.get('value')
		wines_count = Wine.objects.filter(Q(country=value) | Q(province=value)| Q(region_1=value) | Q(region_2=value)).count()
		return Response(wines_count)

class WineCountryProvinceRegionView(APIView):
	def get(self, request, format=None):
		value = request.GET.get('value')
		start = int(request.GET.get('starting'))
		end = int(request.GET.get('ending'))
		wines = Wine.objects.filter(Q(country=value) | Q(province=value)| Q(region_1=value) | Q(region_2=value))[start:end]
		serializer = WineSerializer(wines, many=True)
		return Response(serializer.data)


class WineVarietyOptionsView(APIView):
	def get(self, request, format=None):
		# value = request.GET.get('value')
		wines = Wine.objects.all().values("variety").distinct()
		return Response(wines)

class WineVarietyView(APIView):
	def get(self, request, format=None):
		value = request.GET.get('value')
		start = int(request.GET.get('starting'))
		end = int(request.GET.get('ending'))
		wines = Wine.objects.filter(variety=value)[start:end]
		serializer = WineSerializer(wines, many=True)
		return Response(serializer.data)

class WineVarietySizeView(APIView):
	def get(self, request, format=None):
		value = request.GET.get('value')
		wines_count = Wine.objects.filter(variety=value).count()
		return Response(wines_count)
		





