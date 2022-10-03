from attendence import views
from django.conf.urls import url

urlpatterns=[
    url('myattendence', views.viewattendence),
    url('add', views.addattendence),
    url('uploadattendence', views.uploadattendence),
    url('edit', views.editattendence),
    url('students', views.viewattendence)
]
