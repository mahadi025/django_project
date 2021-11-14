from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^Sylhet',views.destination_name,name='Sylhet')
]
