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





def product(request):  # Renamed function to avoid confusion
    Designers_Perfume_Oil = Perfume.objects.filter(category='Designers Perfume Oil')
    Suratti_Perfume_Oils = Perfume.objects.filter(category='Suratti Perfume Oils')
    Naseem_Oils = Perfume.objects.filter(category='Naseem Oils')

    context = {
        'Designers_Perfume_Oil': Designers_Perfume_Oil,
        'Suratti_Perfume_Oils': Suratti_Perfume_Oils,
        'Naseem_Oils': Naseem_Oils,
    }
    return render(request, 'product.html', context)  # Fixed template name


from .models import SearchEngine

def search(request):
    query = request.GET.get('search', '') 
    results = SearchEngine.objects.filter(search_term__icontains=query)  
    return render(request, 'index.html.html', {'results': results})