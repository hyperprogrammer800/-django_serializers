from django.contrib import admin
from .models import productMainModel, productColourModel, productImageModel

# Register your models here.
admin.site.register([productMainModel, productColourModel, productImageModel])
