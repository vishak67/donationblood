from django.contrib import admin
from . models import Centers, District
# Register your models here.


class CentersAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Centers, CentersAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(District, DistrictAdmin)


