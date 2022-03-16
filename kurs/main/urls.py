
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index),
   path('1',views.g2321),
   path('2',views.g2322),
   path('3',views.g2341),
   path('4',views.g2342),
   path('5',views.g2361),
   path('6', views.g2371),
   path('7', views.g2121M),
   path('8', views.g2122M),
   path('9', views.g2161M),
   path('10', views.g2171M),
   path('11', views.g2261M),
]
