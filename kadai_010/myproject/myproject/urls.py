"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views import ProductListView  # ProductListViewは商品一覧を表示するビュー
from crud.views import ProductDetailView

urlpatterns = [
        path('admin/', admin.site.urls),
        path('product_list/', ProductListView.as_view(), name='product_list'),
        path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
        path('product/', ProductListView.as_view(), name='product_index'),  # この行を追加
]
