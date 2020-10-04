"""historical_games_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import basketapp.views as basketapp
from django.conf import settings
from django.conf.urls.static import static
app_name = 'basketapp'

urlpatterns = [
   path('', basketapp.basket, name='basket'),
   path('add/<int:pk>', basketapp.basket_add, name='add'),
   path('remove/<int:pk>', basketapp.basket_remove, name='remove'),
]
