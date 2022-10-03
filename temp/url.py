
from django.conf.urls import url
from temp import views

urlpatterns=[
    url('student/',views.student),
    url('classroom', views.classroom),
    url('teacher/', views.teacher),
    url('admin/', views.admin),
    url('principal', views.principal)
]