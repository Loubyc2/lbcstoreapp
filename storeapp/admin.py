from django.contrib import admin

from storeapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'slug', 'price', 'create_at')


admin.site.register(Product, ProductAdmin)
