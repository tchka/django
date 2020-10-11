from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
   path('users/create/', adminapp.user_create, name='user_create'),
   path('users/read/', adminapp.users, name='users'),
   path('users/update/<pk>/', adminapp.user_update, name='user_update'),
   path('users/delete/<pk>/', adminapp.user_delete, name='user_delete'),

   path('categories/create/', adminapp.category_create, name='category_create'),
   path('categories/read/', adminapp.categories, name='categories'),
   path('categories/update/<pk>/', adminapp.category_update, name='category_update'),
   path('categories/delete/<pk>/', adminapp.category_delete, name='category_delete'),

   path('products/create/category/<pk>/', adminapp.product_create, name='product_create'),
   path('products/read/category/<pk>/', adminapp.products, name='products'),
   path('products/read/<pk>/', adminapp.product, name='product'),
   path('products/update/<pk>/', adminapp.product_update, name='product_update'),
   path('products/delete/<pk>/', adminapp.product_delete, name='product_delete'),
]