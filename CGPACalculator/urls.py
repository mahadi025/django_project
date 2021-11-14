from .import views
from django.conf.urls import url

urlpatterns = [
    url(r'^CGPA',views.CGPA,name='CGPA')
]
