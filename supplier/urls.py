from django.urls import path
from .import views

app_name = 'supplier'

urlpatterns = [
    path('create/', views.SupplierCreateView.as_view(), name='create'),
    path('listView/', views.SupplierListView.as_view(), name='listView'),
    path('update/<pk>/', views.SupplierUpdate.as_view(), name='updateView'),
    path('delete/<pk>/', views.SupplierDelete.as_view(), name='deleteView'),
    path('detail/<pk>/', views.SupplierDetail.as_view(), name='detailView'),
]