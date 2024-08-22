from django.urls import path
from .views import MaterialRequirementView, ProductListView, ProductDetailView, MaterialListView, MaterialDetailView, \
    ProductMaterialListView, ProductMaterialDetailView, WarehouseListView, WarehouseDetailView

urlpatterns = [
    path('materials/', MaterialRequirementView.as_view(), name='product-materials'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('materials/', MaterialListView.as_view(), name='material-list'),
    path('materials/<int:pk>/', MaterialDetailView.as_view(), name='material-detail'),

    path('product-materials/', ProductMaterialListView.as_view(), name='product-material-list'),
    path('product-materials/<int:pk>/', ProductMaterialDetailView.as_view(), name='product-material-detail'),

    path('warehouses/', WarehouseListView.as_view(), name='warehouse-list'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),
]
