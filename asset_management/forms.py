from django import forms
from .models import AssetType, Asset,AssetImage

class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = ['name', 'description']
        #fields = ['description']

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if AssetType.objects.filter(name=name).exists():
    #         raise forms.ValidationError("Asset type already exists")
    #     return name

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'asset_type', 'is_active']


class AssetImageForm(forms.ModelForm):
    class Meta:
        model = AssetImage
        fields = ['image', 'caption']

AssetImageFormSet = forms.inlineformset_factory(
    Asset, AssetImage, form=AssetImageForm, extra=1, can_delete=True
)