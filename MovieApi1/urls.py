from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Api.urls')),   #including Api urls when a blank request is made
]
