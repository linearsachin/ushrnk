from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('u/<slug>',views.ShrnkView.as_view(),name="clicks"),
    path('metrics/',views.ChartView.as_view(), name="metrics"),
    path('api/clicks/<xcode>',views.chart,name="chart")
]