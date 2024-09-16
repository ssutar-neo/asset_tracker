from django.urls import path
from .views import dashboard,asset_types_data,asset_status_data

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('api/asset-types/',asset_types_data, name='asset_types_data'),
    path('api/asset-status/', asset_status_data, name='asset_status_data'),
]
