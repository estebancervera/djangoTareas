from django.contrib import admin

# Register your models here.
from .models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', "updated")
    list_display = ('title',)
    ordering = ('title', 'created')
    search_fields = ('title',)
    date_hierarchy = ('created')

admin.site.register(Service, ServiceAdmin)