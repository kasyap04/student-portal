from django.conf.urls import url
from department import views

urlpatterns = [
    url('add', views.addDepartment),
    url('view', views.viewdepartment),
    url('edit', views.department_admin),
    url('changedepartment', views.updatedepartments)
]