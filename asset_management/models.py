from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Custom user model (if needed)
# class User(AbstractUser):
#     pass

# Asset Type Model
class AssetType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Asset Model
class Asset(models.Model):
    name = models.CharField(max_length=255)
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='assets/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Asset Images Model
class AssetImage(models.Model):
    asset = models.ForeignKey(Asset, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='asset_images/',blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f'{self.asset.name} - Image'


# class AssetImage(models.Model):
#     asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='assets/')
#     caption = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.caption or 'No Caption'