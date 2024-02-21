from django.urls import path
from core import views as cv

urlpatterns = [   
    path('', cv.home, name='home'),
    path('about/', cv.about, name='about'),
    path('store/', cv.store, name='store'),
]
