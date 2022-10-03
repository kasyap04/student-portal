from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from subject.views import viewsubject_student
from notifications.views import getmynotifications
from events.views import upcomingevent
from classroom.views import today_classwork
from subject.views import viewsubject_teacher
from login.views import islogin
from student.models import Student

from department.views import viewdepartment

from teachers.models import ClassTeacher, Teachers


def login():
    return '/login/login'


# Create your views here.
def student(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "student":
            STUDENT_ID = request.session['login_user'].get('id')
            stu_name = Student.objects.get(stu_id=STUDENT_ID).name
            # print(today_classwork(STUDENT_ID))
            return render(request, 'temp/student.html',
                          {'subjects': viewsubject_student(STUDENT_ID), 'notifications': getmynotifications(request),
                           'events': upcomingevent(), 'today_classwork': today_classwork(STUDENT_ID),
                           'myname': stu_name})
        else:
            return HttpResponseRedirect(login())
    else:
        return HttpResponseRedirect(login())


def classroom(request):
    if request.session['login_user'] != "":
        return render(request, 'temp/classroom.html')
    else:
        return HttpResponseRedirect(login())


def teacher(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        if login_user.get('user') == "teacher":
            if ClassTeacher.objects.filter(teacher_id=login_user.get('id')).count() > 0:
                ct = ClassTeacher.objects.get(teacher_id=login_user.get('id'))
                context = {
                    'sub': viewsubject_teacher(login_user.get('id')),
                    'events': upcomingevent(),
                    'dep_id': ct.dep_id,
                    'sem': ct.sem,
                    'my_name': Teachers.objects.get(teacher_id=login_user.get('id')).name
                }
            else:
                context = {
                    'sub': viewsubject_teacher(login_user.get('id')),
                    'events': upcomingevent(),
                    'my_name': Teachers.objects.get(teacher_id=login_user.get('id')).name
                }
            return render(request, 'temp/teachers.html', context)
        else:
            return HttpResponseRedirect(login())
    else:
        return HttpResponseRedirect(login())


def admin(request):
    if islogin(request):
        if request.session['login_user'].get('user') == "admin":
            context = {
                'departments': viewdepartment(request)
            }
            # print(viewdepartment(request))
            return render(request, 'temp/admin.html', context)
        else:
            return HttpResponseRedirect(login())
    else:
        return HttpResponseRedirect(login())


def principal(request):
    if islogin(request):
        if request.session['login_user'].get('user') == "principal":
            # print(viewdepartment(request))
            context = {
                'departments': viewdepartment(request)
            }
            return render(request, 'temp/principal.html', context)
        else:
            return HttpResponseRedirect(login())
    else:
        return HttpResponseRedirect(login())

