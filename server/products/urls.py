from django.urls import path

from .views import PlanListView, ProductDetailView, ProductListView

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name="products"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product"),
    path('plans/', PlanListView.as_view(), name="plans"),
]
