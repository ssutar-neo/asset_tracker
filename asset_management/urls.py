from django.urls import path
from .views import (create_asset_type, list_asset_types, update_asset_type, delete_asset_type,
                    create_asset, list_assets, update_asset, delete_asset, download_assets)

urlpatterns = [
    path('asset-types/create/', create_asset_type, name='create_asset_type'),
    path('asset-types/', list_asset_types, name='list_asset_types'),
    path('asset-types/update/<int:pk>/', update_asset_type, name='update_asset_type'),
    path('asset-types/delete/<int:pk>/', delete_asset_type, name='delete_asset_type'),
    
    path('assets/create/', create_asset, name='create_asset'),
    path('assets/', list_assets, name='list_assets'),
    path('assets/update/<int:pk>/', update_asset, name='update_asset'),
    path('assets/delete/<int:pk>/', delete_asset, name='delete_asset'),
    path('assets/download/', download_assets, name='download_assets'),
]
