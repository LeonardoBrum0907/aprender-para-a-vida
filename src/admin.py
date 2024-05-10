from django.contrib import admin
from .models import User

class DetUser(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    list_display_links = ('nome', )
    search_fields = ('nome', )

admin.site.register(User, DetUser)

# Register your models here.
