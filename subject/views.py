from django.shortcuts import render
from department.models import Department
from subject.models import Subject
from teachers.models import Teachers, ClassTeacher
from student.models import Student

from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.


def addsubjects(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == "POST":
                f = request.POST
                obj = Subject()
                obj.dep_id = f.get('dep')
                obj.sem = f.get('sem')
                obj.type = f.get('type')
                obj.name = f.get('sub').title().strip()
                obj.code = f.get('code').upper().strip()
                obj.teacher_id = f.get('teacher')
                obj.adm_year = f.get('year')
                obj.save()
                return HttpResponse('sta["s"]end')
            else:
                dep = request.GET.get('dep')
                dep_name = Department.objects.get(dep_id=dep).name.capitalize()
                teachers = Teachers.objects.all()
                return render(request, 'subject/addSubject.html', {'dep': dep_name, 'teachers': teachers})
    else:
        return HttpResponseRedirect('/login/login')



def viewsubject_student(id):
        STUDENT_ID = id
        student = Student.objects.filter(stu_id=STUDENT_ID).values('dep_id', 'current_sem')[0]
        stu_dep = student['dep_id']
        stu_sem = student['current_sem']
        subjects = Subject.objects.filter(dep_id=stu_dep, sem=stu_sem).values('sub_id', 'name', 'teacher_id')
        for sub in subjects:
            teacher_id = sub['teacher_id']
            sub['teacher_id'] = Teachers.objects.filter(teacher_id=teacher_id).values('name')[0]['name']
        return subjects


def viewsubject_teacher(TEACHER_ID):
    subjects = Subject.objects.filter(teacher_id=TEACHER_ID).values('sub_id', 'dep_id', 'sem', 'code', 'name')
    for sub in subjects:
        dep_id = sub['dep_id']
        sub['dep'] = Department.objects.filter(dep_id=dep_id).values('short_name')[0]['short_name']
        del sub['dep_id']
    return subjects


def viewsubject_all(request):
    if request.session['login_user'] != "":
        user = request.session['login_user'].get('user')
        dep = request.GET.get('dep')
        sem = request.GET.get('sem')

        department = Department.objects.get(dep_id=dep)
        subjects = Subject.objects.filter(dep_id=dep, sem=sem).values()
        students = Student.objects.filter(dep_id=dep, current_sem=sem).values('stu_id', 'adm_no', 'name', 'image').order_by('adm_no')

        ct = ClassTeacher.objects.get(dep_id=dep, sem=sem).teacher_id
        class_teacher = Teachers.objects.get(teacher_id=ct).name
        hod = Teachers.objects.get(teacher_id=department.hod).name

        for s in subjects:
            if Teachers.objects.filter(teacher_id=s['teacher_id']).count() > 0:
                s['teacher_id'] = Teachers.objects.get(teacher_id=s['teacher_id']).name
            else:
                s['teacher_id'] = "None"
        if user == "principal":
            context = {
                'subjects': subjects,
                'students': students,
                'ct': class_teacher,
                'hod': hod,
                'dep': department.name,
                'sem': sem,
                'dep_id': dep,
                'user': user
            }
            return render(request, 'subject/viewSublectByPrincipal.html', context)
        elif user == "admin":
            context = {
                'subjects': subjects,
                'students': students,
                'ct': class_teacher,
                'hod': hod,
                'dep': department.name,
                'sem': sem,
                'dep_id': dep
            }
            return render(request, 'subject/viewSubjectByAll.html', context)
        else:
            return HttpResponseRedirect('/login/login')
        # print(context)

    else:
        return HttpResponseRedirect('login/login')


def getSubjects(request):
    dep = request.POST.get('dep')
    sem = request.POST.get('sem')
    result = []
    subject = Subject.objects.filter(dep_id=dep, sem=sem).values('type', 'name', 'code', 'teacher_id')
    for sub in subject:
        teacher_id = sub['teacher_id']
        sub['teacher'] = Teachers.objects.filter(teacher_id=teacher_id).values('name')[0]['name']
        del sub['teacher_id']
    for res in subject:
        result.append(res)
    return HttpResponse(json.dumps(result))


def editsubjects(request):
    if request.method == "POST":
        # print(request.POST)
        if request.POST.get('swift') == '1':  # edit subject
            sub = Subject.objects.get(sub_id=request.POST.get('subId'))
            sub.type = request.POST.get('type')
            sub.name = request.POST.get('name').title()
            sub.code = request.POST.get('code').upper()
            sub.teacher_id = request.POST.get('teacher')
            sub.save()
            return HttpResponse('sta["s"]end')
        elif request.POST.get('swift') == '2':  # delete subject
            Subject.objects.get(sub_id=request.POST.get('subId')).delete()
            return HttpResponse('sta["s"]end')
    else:
        dep_id = request.GET.get('dep')
        sem = request.GET.get('sem')
        subject = Subject.objects.filter(dep_id=dep_id, sem=sem).values()
        for sub in subject:
            sub['dep_id'] = Department.objects.get(dep_id=sub['dep_id']).name
        teacher = Teachers.objects.filter(dep_id__gt=0).values('teacher_id', 'name')
        # print(subject)
        return render(request, 'subject/editSubject.html', {'subject': subject, 'teacher': teacher})