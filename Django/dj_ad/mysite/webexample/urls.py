from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'^$', admin.site.urls),
]
