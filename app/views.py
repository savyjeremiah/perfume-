from django.shortcuts import render

from .models import Perfume

def index(request):
    perfumes = Perfume.objects.all()
    return render(request, 'index.html',{'perfumes': perfumes})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')



def product(request):
    perfumes = Perfume.objects.all()
    return render(request, 'product.html', {'perfumes': perfumes})  

from .models import SearchEngine

def search(request):
    query = request.GET.get('search', '') 
    results = SearchEngine.objects.filter(search_term__icontains=query)  
    return render(request, 'index.html.html', {'results': results})