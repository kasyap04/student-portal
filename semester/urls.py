from django.conf.urls import url
from semester import views
urlpatterns = [
    url('viewsemester', views.viewsemester)
]