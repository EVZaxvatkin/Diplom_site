from django.contrib import admin
from .models import Category, Product, Promo


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "description"]
    list_filter = ["category"]

class PromoAdmin(admin.ModelAdmin):
    list_display = ["name", "product", "discription", "image", "start_data", "end_data"]
    list_filter = ["product", "start_data", "end_data"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Promo, PromoAdmin)





