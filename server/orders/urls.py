from django.urls import path 
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='order_create'),
    path('admin/order/<uuid:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
]