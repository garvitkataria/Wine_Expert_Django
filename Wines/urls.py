from django.conf.urls import url
from .views import WineView, WinePriceView,WineVarietySizeView, WinePointsView, WineCountryProvinceRegionView,WineCountryProvinceRegionSizeView, WineVarietyView, WineVarietyOptionsView, WineSizeView

app_name = 'Wines'

urlpatterns = [
	url(r'^$', WineView.as_view(), name='wine_view'),
	url(r'size/', WineSizeView.as_view(), name='wine_size_view'),
	url(r'price/', WinePriceView.as_view(), name='wine_price_view'),
	url(r'points/', WinePointsView.as_view(), name='wine_points_view'),
	url(r'search/', WineCountryProvinceRegionView.as_view(), name='wine_country_province_region_view'),
	url(r'searchsiz/', WineCountryProvinceRegionSizeView.as_view(), name='wine_country_province_region_size_view'),
	url(r'varietyoptions/', WineVarietyOptionsView.as_view(), name='wine_variety_options_view'),
	url(r'variety/', WineVarietyView.as_view(), name='wine_variety_view'),
	url(r'varietysiz/', WineVarietySizeView.as_view(), name='wine_variety_size_view'),
	]