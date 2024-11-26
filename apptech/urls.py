from django.urls import path

from apptech import views

urlpatterns = [
    path('', views.home),
    path('display', views.display_home)
]
