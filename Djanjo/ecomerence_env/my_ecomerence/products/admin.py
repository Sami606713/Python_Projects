from django.contrib import admin
from products.models import Products,Contact,Address
# Register your models here.
# ADD a search field
class ProductAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Products,ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Contact,ContactAdmin)

class AddressAdmin(admin.ModelAdmin):
    search_fields=(["name","city"])
admin.site.register(Address)
