from django.urls import path
from.views import BrandList , about ,home , contact


urlpatterns = [
    path('brand/',BrandList.as_view()),
    path('about/',about),
    path('home/',home),
    path('contact/',contact),
    
]
