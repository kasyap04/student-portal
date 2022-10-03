from django.conf.urls import url
from internals import views

urlpatterns = [
    url('viewInternals', views.viewintrnals),
    url('add', views.addinternals),
    url('fetchstudentandsubject', views.fetchstudentandsubject),
    url('uploadinternals', views.uploadinternals),
    url('getinternalsforstudents', views.getinternalsforstudents),
    url('studentinternal', views.fetchinternals),
    url('edit', views.editinternals)
]