from django.shortcuts import render
from department.models import Department
from teachers.models import Teachers
from django.http import HttpResponse, HttpResponseRedirect

import json


# Create your views here.


def viewdepartment(request):
    departments = Department.objects.values('dep_id', 'name', 'hod', 'duration')
    # print(departments)
    for dep in departments:
        if Teachers.objects.filter(teacher_id=int(dep['hod'])).count() > 0:
            dep['hod'] = Teachers.objects.get(teacher_id=int(dep['hod'])).name
        else:
            dep['hod'] = ""
    return departments


def addDepartment(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == 'POST':
                dep = json.loads(request.POST.get('dep'))
                obj = Department()
                obj.name = dep.get('name').title()
                obj.short_name = dep.get('short')
                obj.duration = dep.get('dur')
                obj.hod = 0
                obj.save()
                return HttpResponse('sta["s"]end')
            else:
                return render(request, 'department/addDepartment.html')
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponse('sta["l"]end')



def department_admin(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            count = 0
            dep = Department.objects.all().values()
            for i in dep:
                i['count'] = count
                dep_id = i['dep_id']
                hodNames = []
                for t in Teachers.objects.filter(dep_id=dep_id).values('teacher_id', 'name'):
                    teacher = {'id': t['teacher_id'], 'name': t['name']}
                    hodNames.append(teacher)
                i['hodNames'] = hodNames
                count += 1
            print(dep)
            return render(request, 'department/department_admin.html', {'dep': dep})
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponseRedirect('/login/login')



def updatedepartments(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            short_name = request.POST.get('shotname').upper()
            dep_name = request.POST.get('name').capitalize().strip()
            dur = request.POST.get('dur')
            hod = request.POST.get('hod')
            dep_id = request.POST.get('depId')
            department = Department.objects.get(dep_id=dep_id)
            department.name = dep_name
            department.short_name = short_name
            department.duration = dur
            department.hod = hod if hod != "" else 0
            department.save()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["uau"]end')  # unauthorised user
    else:
        return HttpResponse('sta["l"]end')
