"""studentportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('attendence/', include('attendence.urls')),
    url('fees/', include('fees.urls')),
    url('department/', include('department.urls')),
    url('student/', include('student.urls')),
    url('home/', include('home.urls')),
    url('events/', include('events.urls')),
    url('internals/', include('internals.urls')),
    url('notifications/', include('notifications.urls')),
    url('subject/', include('subject.urls')),
    url('login/', include('login.urls')),
    url('teachers/', include('teachers.urls')),
    url('complaints/', include('complaints.urls')),
    # url('classworks/', include('classworks.urls')),
    url('semester/', include('semester.urls')),
    url('classroom/', include('classroom.urls')),
    url('temp/',include('temp.url')),
    url('',include('login.urls'))
]

