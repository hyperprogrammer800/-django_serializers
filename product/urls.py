from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('mainpage', views.mainproductviews, basename='main')
router.register('colourpage', views.colourproductviews, basename='colour')
router.register('imagepage', views.imageproductviews, basename='image')

urlpatterns = [
    path('product/', include(router.urls)),
]
