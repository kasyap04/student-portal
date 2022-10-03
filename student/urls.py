from django.conf.urls import url
from student import views

urlpatterns = [
    url('register', views.addStudents),
    url('uploadstudent', views.uploadstudent),
    # url('classmates', views.classmates),
    url('edit', views.editstudent),
    # url('viewstudent', views.viewstudent),
    url('changepassword', views.changepassword),
    url('profile', views.profile),
    url('myname', views.getmyname),
    url('searchstudent', views.searchstudent),
    url('deleteimage', views.deleteimage),
    url('upgradesem', views.upgradesem)
]