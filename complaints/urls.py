from django.conf.urls import url
from complaints import views

urlpatterns = [
    url('view', views.viewcomplaints),
    url('add', views.addcomplaints)
]