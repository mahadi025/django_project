from django.urls import path
from .import views


urlpatterns = [
    path('munif.html/', views.munif, name='munif'),
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('index.html/', views.index, name='index')
]
