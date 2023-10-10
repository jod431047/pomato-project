from django.urls import path
from.views import BrandList


urlpatterns = [
    path('',BrandList.as_view())
    
]
