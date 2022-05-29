from django.shortcuts import render
from .models import *

# Create your views here.

def gallery(request):
    all_images = Photo.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request, 'index.html', {'all_images':all_images,'location_results':location_results,'category_results':category_results})

def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Photo.objects.filter(image_category__cat_name = category)
    return render(request,'index.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})
def get_location(request,location):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    location_result = Photo.filter_by_location(location)
    return render(request,'index.html',{'all_images':location_result,'category_results':category_results,'location_results':location_results})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})