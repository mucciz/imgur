from django.shortcuts import render
from django.http  import HttpResponse,Http404
from datetime import datetime
from .models import Image,Location,Category
# Create your views here.

def home(request):
    return render(request, 'index.html')

def galleries(request):
    category = Category.objects.all()
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request, 'galleries.html',{"images":images, "category": category, "location":location})

def location(request):
    location = Location.objects.all()
    images=Image.objects.all()
    print(images)
    return render(request, 'location.html',{"images":images, "location": location})

def search_by_location(request, location):
    locations = Location.objects.all()
    images = Image.search_by_location_id(location)
    print(images)
    title = f'{location} Photos'
    return render(request, 'found.html', {'title': title, 'images': images, 'locations': locations})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
