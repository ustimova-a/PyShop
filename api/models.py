from importlib import resources
# import resource
from django.db import models
from tastypie.resources import ModelResource
from products.models import Product


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
