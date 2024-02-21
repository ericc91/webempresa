from django.contrib import admin
from .models import Service

admin.site.site_header="Administracion del sitio"

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
