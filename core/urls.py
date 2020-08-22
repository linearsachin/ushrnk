from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('<slug>',views.HomeView.as_view(),name="home"),
]