from django.contrib import admin
from products.models import Products,Contact
# Register your models here.
# ADD a search field
class ProductAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Products,ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Contact,ContactAdmin)
# admin.site.register(Phone_nbr)
