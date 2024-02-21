from django.urls import path
from blog import views 

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:id>/', views.category, name='category')
]
