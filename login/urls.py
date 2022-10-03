from  django.conf.urls import url
from login import views

urlpatterns = [
    url('login', views.login),
    url('action', views.action),
    url('changepassword', views.changepassword),
    url('stupass', views.changestudentpassword),
    url('changeforgotpassword', views.changeforgotpassword),
    url('', views.login)
]