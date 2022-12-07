from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_product, name='new_product'),
    path('details/<int:product_id>', views.product_details, name='product_details'),
]
