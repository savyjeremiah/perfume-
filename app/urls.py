from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('404/', views.error_404, name='error_404'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
