from django.urls import path

from products.views import (
    product_details_view,product_create_view,render_initial_data,dynamic_lookup_view,
    product_delete_view,product_list_view)


app_name="products"

urlpatterns = [
    path('' , product_list_view,name="product-list"),
    path('create/' , product_create_view,name="product-create"),
    path('<int:id>/' , render_initial_data,name="product-detail"),
    path('<int:id>/update' , dynamic_lookup_view,name="product-update"),
    path('<slug:slug>/delete' , product_delete_view,name="product-delete"),


]