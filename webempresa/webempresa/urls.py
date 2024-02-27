"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    #paths de admin
    path('admin/', admin.site.urls),

    #paths de app core
    path('', include('core.urls')),   

    #path de app services
    path('services/', include('services.urls')), 

    #path de app blog
    path('blog/', include('blog.urls')),

    #path de pages app
    path('page/', include('pages.urls')),

    #path de contact app
    path('contact/', include('contact.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Custom titles for admin
admin.site.site_header="La Caffetiera"
admin.site.index_title="Panel de administración"
admin.site.site_title= "La Caffetiera"