from django.contrib import admin
from django.urls import path
import orderapp.views as orderapp
from django.conf import settings
from django.conf.urls.static import static


app_name = 'orderapp'

urlpatterns = [
    path('', orderapp.OrderList.as_view(), name='order_list'),
    path('create/', orderapp.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<pk>/', orderapp.OrderRead.as_view(), name='order_read'),
    path('update/<pk>/', orderapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', orderapp.OrderDelete.as_view(), name='order_delete'),
    path('forming/<pk>/', orderapp.order_forming_complete, name='order_forming_complete'),
]
