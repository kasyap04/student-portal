from django.conf.urls import url
from teachers import views

urlpatterns = [
    url('register', views.addteachers),
    url('viewTeachers', views.viewteachers),
    url('edit', views.editteacher),
    url('deleteteacher', views.deleteTeacher),
    url('classteacher', views.classteacher)
]