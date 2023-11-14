from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api',views.movieApi,basename='bapi')

urlpatterns = [
    path('',include(router.urls)),
]
