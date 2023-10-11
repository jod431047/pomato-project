from django.urls import path
from.views import BrandList 


urlpatterns = [
    path('brand/',BrandList.as_view())
    
]
