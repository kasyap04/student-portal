from django.conf.urls import url
from notifications import views

urlpatterns = [
    url('viewNotifications', views.viewnotifications),
    url('add', views.addnotifications)
    # url('postnotification', views.postnotification)
]