from django.urls import path,include
from. import views
from django.conf.urls import include

urlpatterns = [
    path('home/',views.home),
]