from django.shortcuts import render
from department.models import Department
from teachers.models import Teachers, ClassTeacher
from login.models import Login
from django.http import HttpResponse, HttpResponseRedirect

import json

# Create your views here.


def addteachers(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == "POST":
                number = request.POST.get('num').strip()
                if Teachers.objects.filter(mobile=number).count() == 0:
                    obj = Teachers()
                    obj.name = request.POST.get('name').title().strip()
                    obj.mobile = number
                    obj.email = request.POST.get('email').strip()
                    obj.dob = request.POST.get('dob')
                    obj.gender = request.POST.get('gender')
                    obj.qualification = request.POST.get('qual').strip()
                    obj.experiance = request.POST.get('exp').strip()
                    obj.dep_id = request.POST.get('dep')
                    obj.save()

                    login = Login()
                    login.username = request.POST.get('num').strip()
                    login.password = request.POST.get('name').lower().replace(' ', '') + "@donbosco"
                    login.type = "teacher"
                    login.u_id = Teachers.objects.latest('teacher_id').teacher_id
                    login.save()
                    return HttpResponse('sta["s"]end')
                else:
                    return HttpResponse('sta["te"]end')

            else:
                dep = Department.objects.all()
                return render(request, 'teachers/addTeachers.html', {'dep': dep})
        else:
            return HttpResponse('Unauthorised user')
    else:
        return HttpResponseRedirect('/login/login')


def viewteachers(request):
    return render(request, 'teachers/viewTeachers.html')


def editteacher(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == "POST":
                number = request.POST.get('num').strip()
                id = request.POST.get('teacherId')
                if Teachers.objects.filter(mobile=number).exclude(teacher_id=id).count() == 0:
                    obj = Teachers.objects.get(teacher_id=id)
                    obj.name = request.POST.get('name').title().strip()
                    obj.mobile = request.POST.get('num').strip()
                    obj.email = request.POST.get('email').strip()
                    obj.dob = request.POST.get('dob')
                    obj.gender = request.POST.get('gender')
                    obj.qualification = request.POST.get('qual').strip()
                    obj.experiance = request.POST.get('exp').strip()
                    obj.dep_id = request.POST.get('dep')
                    obj.save()
                    return HttpResponse('sta["s"]end')
                else:
                    return HttpResponse('sta["te"]end')

            else:
                teaherId = request.GET.get('id')
                teacher = Teachers.objects.filter(teacher_id=teaherId).values()
                for i in teacher:
                    i['dob'] = str(i['dob'])
                dep = Department.objects.all()
                return render(request, 'teachers/addTeachers.html', {'dep': dep, 'teacher': teacher})
        else:
            return HttpResponse('Unauthorised user')
    else:
        return HttpResponseRedirect('/login/login')



def deleteTeacher(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            Login.objects.get(u_id=request.POST.get('teacher_id'), type="teacher").delete()
            Teachers.objects.get(teacher_id=request.POST.get('teacher_id')).delete()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["auu"]end')
    else:
        return HttpResponse('sta["l"]end')


def classteacher(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == "POST":
                swift = int(request.POST.get('swift'))
                dep = request.POST.get('dep')
                sem = request.POST.get('sem')

                if swift == 1:
                    result = []
                    dep_teachers = []
                    for t in Teachers.objects.filter(dep_id=dep).values('teacher_id', 'name'):
                        dep_teachers.append( {'teacher_id': t['teacher_id'], 'name': t['name']} )
                    include_ct = {}
                    include_ct['teachers'] = dep_teachers
                    if ClassTeacher.objects.filter(dep_id=dep, sem=sem).count() > 0:
                        ct = ClassTeacher.objects.get(dep_id=dep, sem=sem).teacher_id
                        include_ct['ct'] = ct
                    result.append(include_ct)
                    return HttpResponse('sta[' + json.dumps(result)+ ']end')

                elif swift == 2:
                    ctID = request.POST.get('ct')
                    if ClassTeacher.objects.filter(dep_id=dep, sem=sem).count() > 0:
                        classteacher = ClassTeacher.objects.get(dep_id=dep, sem=sem)
                        classteacher.teacher_id = ctID
                        classteacher.save()
                        return HttpResponse('sta["cs"]end')  # changes saved
                    else:
                        obj = ClassTeacher()
                        obj.dep_id = dep
                        obj.sem = sem
                        obj.teacher_id = ctID
                        obj.save()
                        return HttpResponse('sta["cts"]end')  # class teacher saved

            else:
                dep = Department.objects.all().values()
                return render(request, 'teachers/addClassTeacher.html', {'dep': dep})
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponseRedirect('/login/login')