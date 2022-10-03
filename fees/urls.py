from django.conf.urls import url
from fees import views

urlpatterns = [
    # url('viewFees', views.viewFees_student),
    url('add', views.addFees),
    url('view', views.viewfee_all),
    url('postfee', views.postfee),   #ajax
    url('editfee', views.editFees),
    url('deletefee', views.deletefee),  #ajax
    url('studentpaid', views.updatestudentfee)
]

