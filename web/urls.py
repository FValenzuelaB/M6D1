from django.contrib import admin
from .views import home,contact,about
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact)
]