# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import Asset, AssetImage

# class AssetImageInline(admin.TabularInline):
#     model = AssetImage
#     extra = 1  # Number of empty forms to display

# @admin.register(Asset)
# class AssetAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'asset_type', 'is_active')
#     inlines = [AssetImageInline]

# @admin.register(AssetImage)
# class AssetImageAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'image', 'caption')
