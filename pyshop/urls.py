"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from itertools import product
from django.contrib import admin
from django.urls import path, include
from api.models import ProductResource
from . import views

product_resource = ProductResource()

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api/', include(product_resource.urls))
]
