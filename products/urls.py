from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('details/<int:product_id>', views.product_details, name='product_details'),
]
