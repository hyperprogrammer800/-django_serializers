from rest_framework import viewsets
from .models import productMainModel, productColourModel, productImageModel
from .serializer import serialMain, serialColour, serialImage

class mainproductviews(viewsets.ModelViewSet):
    queryset = productMainModel.objects.all()
    serializer_class = serialMain

class colourproductviews(viewsets.ModelViewSet):
    queryset = productColourModel.objects.all()
    serializer_class = serialColour

class imageproductviews(viewsets.ModelViewSet):
    queryset = productImageModel.objects.all()
    serializer_class = serialImage
