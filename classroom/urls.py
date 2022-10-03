from django.conf.urls import url
from classroom import views


urlpatterns = [
    url('addclasswork', views.addclasswork),
    url('usershare', views.addusershare),
    url('viewclassroom', views.viewclassroom),
    url('submit', views.submitclasswork),
    url('undoclasswork', views.unsubmit)
]