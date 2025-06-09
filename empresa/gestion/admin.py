from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono')
    search_fields = ('nombre', 'apellidos', 'email')