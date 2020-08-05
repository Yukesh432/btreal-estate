from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    liat_display_link = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 20



admin.site.register(Realtor, RealtorAdmin)
