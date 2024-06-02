from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:pk>/', views.checkout, name = 'checkout'),
    path('product/<str:product_name>/', views.product_list, name='products')
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)