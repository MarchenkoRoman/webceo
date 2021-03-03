from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('sale_list/', views.SaleList.as_view(), name='sale_list'),
    path('change_price/', views.HistoryPrice.as_view(), name='history_price'),
]
