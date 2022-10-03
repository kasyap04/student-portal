import os

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from department.models import Department
from student.models import Student
from subject.models import Subject
from classroom.models import Classroom, Submited
from login.models import Login, Master
from teachers.models import Teachers, ClassTeacher

from notifications.views import createnotification



import datetime
import json


# Create your views here.


def uploadstudent(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            fun = request.POST
            adm_no = fun.get('adm').upper().strip()
            if Student.objects.filter(adm_no=adm_no).count() == 0:
                obj = Student()
                obj.adm_no = adm_no
                obj.name = fun.get('name').title().strip()
                obj.dob = fun.get('dob')
                obj.gender = fun.get('gender')

                obj.phone = fun.get('selfMobile').strip()
                obj.email = fun.get('email')
                obj.join_year = fun.get('year')

                obj.current_sem = "1"
                obj.dep_id = fun.get('dep')
                obj.passout = 0

                myfile = request.FILES["image"]
                # print(myfile)
                fs = FileSystemStorage()
                myfilename = 'uploads/' + myfile.name.replace(' ', '')
                file_name = fs.save(myfilename, myfile)

                obj.image = file_name
                obj.save()

                login = Login()
                login.username = fun.get('adm').upper().strip()
                login.password = fun.get('adm').lower().strip()
                login.type = "student"
                login.u_id = Student.objects.latest('stu_id').stu_id
                login.save()
                return HttpResponse('sta["s"]end')
            else:
                return HttpResponse('sta["se"]end')  #student exist
        else:
            return HttpResponse('uau')  #unauthorised user
    else:
        return HttpResponse('sta["l"]end')



def classmates(STUDENT_ID):
    stu = Student.objects.filter(stu_id=STUDENT_ID).values('dep_id', 'current_sem')[0]
    stu_dep = stu['dep_id']
    stu_sem = stu['current_sem']
    return Student.objects.filter(dep_id=stu_dep, current_sem=stu_sem).values('stu_id', 'name', 'image', 'adm_no').exclude(stu_id=STUDENT_ID).order_by('adm_no')


# def viewstudent(request):
#     user = "admin"
#     dep_id = request.GET.get('dep')
#     sem = request.GET.get('sem')
#     students = Student.objects.filter(dep_id=dep_id, current_sem=sem).values('stu_id', 'adm_no', 'name',
#                                                                              'image').order_by('adm_no')
#     if user == "admin":
#         return render(request, 'student/viewStudent.html', {'stu': students, 'user': "admin"})
#     else:
#         return render(request, 'student/viewStudent.html', {'stu': students})



def addStudents(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            dep = Department.objects.all()
            return render(request, 'student/AddStudent.html', {'dep': dep})
        else:
            return HttpResponseRedirect('login/login')
    else:
        return HttpResponseRedirect('login/login')



def deleteimage(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            stu_id = request.POST.get('stu')
            student = Student.objects.get(stu_id=stu_id)
            os.remove('static/' + student.image)
            student.image = ""
            student.save()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('uau')
    else:
        return HttpResponse('sta["l"]end')


def editstudent(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == "POST":
                fun = request.POST
                stu_id = fun.get('stuId')
                admNo = fun.get('adm').upper().strip()
                obj = Student.objects.get(stu_id=stu_id)

                if str(obj.adm_no) != str(admNo):
                    login = Login.objects.get(type="student", u_id=stu_id)
                    login.username = admNo
                    createnotification({'user': 'System', 'id': 1}, [{'stu_id': stu_id}], "Your admission number is changed to " + admNo + " by Admin")
                obj.adm_no = admNo

                obj.name = fun.get('name').title().strip()
                obj.dob = fun.get('dob')
                obj.gender = fun.get('gender')
                obj.phone = fun.get('selfMobile').strip()
                obj.email = fun.get('email')
                obj.join_year = fun.get('year')

                obj.dep_id = fun.get('dep')

                myfile = request.FILES.get("image", False)
                # image_name = Student.objects.filter(stu_id=stu_id).values('image')[0]['image']
                if myfile:
                    fs = FileSystemStorage()
                    myfilename = 'uploads/' + myfile.name.replace(' ', '')
                    file_name = fs.save(myfilename, myfile)
                    obj.image = file_name

                obj.save()
                return HttpResponse('sta["s"]end')
            else:
                stu_id = request.GET.get('stuid')
                student = Student.objects.filter(stu_id=stu_id).values()[0]
                student['dob'] = str(student['dob'])
                student['join_year'] = str(student['join_year'])
                dep = Department.objects.all()
                # print(student)
                return render(request, 'student/AddStudent.html', {'student': student, 'dep': dep})
        else:
            return HttpResponseRedirect('login/login')
    else:
        return HttpResponseRedirect('login/login')


def changepassword(request):
    stu_id = request.POST.get('stuId')
    password = request.POST.get('pass')
    login = Login.objects.get(type='student', u_id=stu_id)
    login.password = password
    login.save()
    return HttpResponse('sta["s"]end')


def profile(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        if login_user.get('user') == "student" or login_user.get('user') == "principal":
            if login_user.get('user') == "principal":
                STUDENT_ID = request.GET.get('stu')
            else:
                STUDENT_ID = login_user.get('id')
            student = Student.objects.filter(stu_id=STUDENT_ID).values()[0]
            stu_dep = student['dep_id']
            stu_sem = student['current_sem']
            works = 0
            submited = 0
            work_id = []
            sub_id = Subject.objects.filter(dep_id=stu_dep, sem=stu_sem).values('sub_id')
            for sub in sub_id:
                if Classroom.objects.filter(sub_id=sub['sub_id'], context='classwork').count() > 0:
                    works += Classroom.objects.filter(sub_id=sub['sub_id'], context='classwork').count()
                    for wk in Classroom.objects.filter(sub_id=sub['sub_id'], context='classwork').values('context_id'):
                        work_id.append(wk['context_id'])

            # print(work_id)
            for wi in work_id:
                if Submited.objects.filter(work_id=wi, stu_id=STUDENT_ID).count() > 0:
                    submited += 1
            # print(submited)
            student['works'] = works
            student['submited'] = submited
            student['pending'] = int(works) - int(submited)

            student['dep_id'] = Department.objects.get(dep_id=stu_dep).short_name
            student['academic_years'] = str(student['join_year'])[0:4] + ' - ' + str(int(str(student['join_year'])[0:4]) + 3)
            # print(classmates(STUDENT_ID))
            if login_user.get('user') == "principal":
                return render(request, 'student/viewStudent_principal.html', {'stu': student, 'classmates': classmates(STUDENT_ID)})
            elif login_user.get('user') == "student":
                return render(request, 'student/profile.html', {'stu': student, 'classmates': classmates(STUDENT_ID)})
        elif login_user.get('user') == "admin":
            stu = request.GET.get('stu')
            student = Student.objects.filter(stu_id=stu).values()
            for s in student:
                s['dob'] = s['dob'].strftime("%d %b, %Y")
                s['academic_years'] = str(s['join_year'])[0:4] + ' - ' + str(int(str(s['join_year'])[0:4]) + 3)
                s['join_year'] = s['join_year'].strftime("%d %b, %Y")
                s['dep'] = Department.objects.get(dep_id=s['dep_id']).short_name
                s['dep_dur'] = Department.objects.get(dep_id=s['dep_id']).duration
            # print(student)
            return render(request, 'student/viewStudent_admin.html', {'stu': student[0]})

    else:
        return HttpResponseRedirect('/login/login')


def getmyname(request):
    if request.session['login_user'] != "":
        user = request.session['login_user'].get('user')
        id = request.session['login_user'].get('id')
        if user == "student":
            obj = Student.objects.get(stu_id=id)
            lastLogin = Login.objects.get(u_id=obj.stu_id, type=user).last_login
            login_time = lastLogin.strftime("%b %d, %Y") + ' at ' + lastLogin.strftime("%I:%M %p")
            result = [{'name': obj.name, 'adm_no': obj.adm_no, 'image': obj.image, 'last_login': login_time}]
            return HttpResponse('sta' + json.dumps(result) + 'end')
        elif user == "teacher":
            obj = Teachers.objects.get(teacher_id=id)
            lastLogin = Login.objects.get(u_id=obj.teacher_id, type=user).last_login
            login_time = lastLogin.strftime("%b %d, %Y") + ' at ' + lastLogin.strftime("%I:%M %p")
            result = [{'name': obj.name, 'last_login': login_time, 'phone': obj.mobile, 'email': obj.email}]
            dep = Department.objects.filter(hod=obj.teacher_id)
            if dep.count() > 0:
                result[0]['hod'] = dep.values('name')[0]['name']
                result[0]['dep_id'] = dep.values('dep_id')[0]['dep_id']
                c_t = ClassTeacher.objects.filter(teacher_id=id)
                if c_t.count() > 0:
                    result[0]['sem'] = ClassTeacher.objects.get(teacher_id=obj.teacher_id).sem
                else:
                    result[0]['nosem'] = True

            ct = ClassTeacher.objects.filter(teacher_id=id)
            if ct.count() > 0:
                result[0]['ct'] = Department.objects.get(dep_id=ct.values('dep_id')[0]['dep_id']).short_name + ' ' + str(ct.values('sem')[0]['sem'])
                result[0]['dep_id'] = ClassTeacher.objects.get(teacher_id=obj.teacher_id).dep_id
                result[0]['sem'] = ClassTeacher.objects.get(teacher_id=obj.teacher_id).sem

            return HttpResponse('sta' + json.dumps(result) + 'end')
        elif user == "admin" or user == "principal":
            master = Master.objects.get(master_id=id)
            lastLogin = Login.objects.get(u_id=id, type=user).last_login
            login_time = lastLogin.strftime("%b %d, %Y") + ' at ' + lastLogin.strftime("%I:%M %p")
            result = [{'name': master.name, 'last_login': login_time}]
            return HttpResponse('sta' + json.dumps(result) + 'end')
        else:
            return HttpResponse('sta["e"]end')

    else:
        return HttpResponse('sta["l"]end')


def upgradesem(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            dep_id = request.POST.get('dep')

            duration = int(Department.objects.get(dep_id=dep_id).duration)

            students = Student.objects.filter(dep_id=dep_id, passout=0).values('stu_id')
            for s in students:
                stu = Student.objects.get(stu_id=s['stu_id'])
                sem = int(stu.current_sem)
                if (duration == 3 and sem == 6) or (duration == 2 and sem == 4):
                    stu.passout = True
                stu.current_sem = sem+1
                stu.save()

            return HttpResponse('sta["s"]end')

    else:
        return HttpResponse('sta["l"]end')


def searchstudent(request):
    search = request.POST.get('search').upper()
    name = request.POST.get('search').capitalize()
    result = []
    students = Student.objects.filter(Q(adm_no__contains=search) | Q(name__contains=name), passout=0).values('stu_id', 'adm_no', 'name').order_by('adm_no')[:5]
    for s in students:
        result.append([s['adm_no'], s['name'], s['stu_id']])
    # print(students)
    return HttpResponse(json.dumps(result))
