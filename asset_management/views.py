from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import AssetType, Asset
from .forms import AssetTypeForm, AssetForm,AssetImage,AssetImageFormSet
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Asset Type Views
def create_asset_type(request):
    if request.method == 'POST':
        form = AssetTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_asset_types')
    else:
        form = AssetTypeForm()
    return render(request, 'asset_management/create_asset_type.html', {'form': form})

def list_asset_types(request):
    asset_types = AssetType.objects.all().order_by('-created_at')
    return render(request, 'asset_management/list_asset_types.html', {'asset_types': asset_types})

def update_asset_type(request, pk):
    asset_type = get_object_or_404(AssetType, pk=pk)
    print(asset_type)
    if request.method == 'POST':
        print("-------")
        form = AssetTypeForm(request.POST, instance=asset_type)
        if form.is_valid():
            print("--------")
            form.save()
            return redirect('list_asset_types')
    else:
        form = AssetTypeForm(instance=asset_type)
    return render(request, 'asset_management/update_asset_type.html', {'form': form,'asset_type': asset_type})

def delete_asset_type(request, pk):
    asset_type = get_object_or_404(AssetType, pk=pk)
    if request.method == 'POST':
        asset_type.delete()
        return redirect('list_asset_types')
    return render(request, 'asset_management/delete_asset_type.html', {'asset_type': asset_type})

# # Asset Views
# def create_asset(request):
#     if request.method == 'POST':
#         form = AssetForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('list_assets')
#     else:
#         form = AssetForm()
#     return render(request, 'asset_management/create_asset.html', {'form': form})

def create_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        formset = AssetImageFormSet(request.POST, request.FILES, instance=Asset())
        print(formset)
        print(form.is_valid())
        print(formset.is_valid())
        if form.is_valid() and formset.is_valid():
            asset = form.save()
            formset.instance = asset
            formset.save()
            return redirect('list_assets')
    else:
        form = AssetForm()
        formset = AssetImageFormSet()

    return render(request, 'asset_management/create_asset.html', {'form': form, 'formset': formset})
    #return render(request, 'asset_management/create_asset.html', {'form': form})

def list_assets(request):
    assets = Asset.objects.all().order_by('-created_at').prefetch_related('images').all()
    return render(request, 'asset_management/list_assets.html', {'assets': assets})

def update_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        print(asset.images.all().values('image'))
        form = AssetForm(request.POST, request.FILES, instance=asset)
        print(form)
        formset = AssetImageFormSet(request.POST, request.FILES, instance=Asset())
        if form.is_valid() and formset.is_valid():
            asset = form.save()
            formset.instance = asset
            formset.save()
            delete_image_ids = request.POST.getlist('delete_images')
            print(delete_image_ids)
            for image_id in delete_image_ids:
                image = get_object_or_404(AssetImage,id=image_id)
                image.delete()

            return redirect('list_assets')
    else:
        form = AssetForm(instance=asset)
        formset = AssetImageFormSet()
    return render(request, 'asset_management/update_asset.html', {'form': form, 'formset': formset})

def delete_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('list_assets')
    return render(request, 'asset_management/delete_asset.html', {'asset': asset})

def download_assets(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=assets.csv'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Code', 'Asset Type', 'Is Active'])

    for asset in Asset.objects.all():
        writer.writerow([asset.name, asset.code, asset.asset_type.name, asset.is_active])

    return response

