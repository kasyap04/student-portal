from django.conf.urls import url
from events import views

urlpatterns = [
    url('view', views.viewevents),
    url('add', views.addevents),
    url('uploadevents', views.uploadevents),
    url('displayevents', views.displayevents),
    url('updateevents', views.updateevents)
]