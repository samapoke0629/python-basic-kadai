from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)

# 以下の行を削除またはコメントアウト
# admin.site.register(Product)

# ProductモデルをProductAdminとともに登録
admin.site.register(Product, ProductAdmin)
