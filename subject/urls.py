from django.conf.urls import url
from subject import views

urlpatterns =[
    url('addSubject', views.addsubjects),
    url('view', views.viewsubject_all),
    url('mysubjects', views.viewsubject_teacher),
    url('viewSubject_student', views.viewsubject_student),
    url('getsubjects', views.getSubjects),
    url('edit', views.editsubjects)  # by admin
]