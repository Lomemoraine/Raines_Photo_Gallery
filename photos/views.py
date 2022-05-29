from django.shortcuts import render
from .models import *

# Create your views here.

def gallery(request):
    all_images = Photo.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request, 'index.html', {'all_images':all_images,'location_results':location_results,'category_results':category_results})