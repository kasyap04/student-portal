from django.conf.urls import url
from home import views

urlpatterns = [
    url('home', views.home)
]