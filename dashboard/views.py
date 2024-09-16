from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import JsonResponse
from asset_management.models import Asset, AssetType
from django.db.models import Count

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def asset_types_data(request):
    data = Asset.objects.values('asset_type__name').annotate(count=Count('id'))
    return JsonResponse(list(data), safe=False)

def asset_status_data(request):
    data = Asset.objects.values('is_active').annotate(count=Count('id'))
    return JsonResponse(list(data), safe=False)
