from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('recipes', views.RecepieViewSet)

app_name = 'recipe'

"""registration router from rest framework"""
urlpatterns = [
    path('', include(router.urls)),
]