from django.views.generic import ListView
from django.views.generic.detail import DetailView  # DetailViewをインポート
from .models import Product  # Productモデルをインポート

class ProductListView(ListView):
    model = Product
    template_name = 'crud/product_list.html'  # 使用するテンプレートを指定
    context_object_name = 'products'  # テンプレートで使用する変数名を指定

class ProductDetailView(DetailView):
    model = Product
    # ここにDetailViewの設定を追加する場合があります