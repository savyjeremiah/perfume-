
from django.shortcuts import render
from .models import Perfume

def index(request):
    perfumes = Perfume.objects.all()
    return render(request, 'index.html', {'perfumes': perfumes})

def about(request):
    return render(request, 'about.html')

def error_404(request):  
    return render(request, '404.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')



def service(request):
    return render(request, 'service.html') 

def team(request):
    return render(request, 'team.html')

def product(request):  
    Designers_Perfume_Oil = Perfume.objects.filter(category='Designers Perfume Oil')
    Suratti_Perfume_Oils = Perfume.objects.filter(category='Suratti Perfume Oils')
    Naseem_Oils = Perfume.objects.filter(category='Naseem Oils')

    context = {
        'Designers_Perfume_Oil': Designers_Perfume_Oil,
        'Suratti_Perfume_Oils': Suratti_Perfume_Oils,
        'Naseem_Oils': Naseem_Oils,
    }
    return render(request, 'product.html', context)  


# from .models import SearchEngine

# def search(request):
#     query = request.GET.get('search', '') 
#     results = SearchEngine.objects.filter(search_term__icontains=query)  
#     return render(request, 'index.html.html', {'results': results})