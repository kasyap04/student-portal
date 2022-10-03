from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from attendence.models import Attendence
from student.models import Student
from department.models import Department
from teachers.models import Teachers, ClassTeacher

import json
import datetime
from calendar import monthrange

# Create your views here.

# TEACHER_ID = 6
# STUDENT_ID = 1


# def fetchstudents(request):
#     dep = int(request.POST.get('dep'))
#     sem = int(request.POST.get('sem'))
#     # return HttpResponse(str(dep))
#     test = []
#     stu = Student.objects.filter(dep_id=dep, current_sem=sem).values('adm_no', 'name').order_by('adm_no')
#     for i in stu:
#         test.append(json.dumps(i))
#     return HttpResponse(json.dumps(test))



def uploadattendence(request):
    if request.session['login_user'] != "":
        TEACHER_ID = request.session['login_user'].get('id')
        data = json.loads(request.POST['a'])
        attend = data["att"]
        sel_dep = int(data["dep"])
        sel_sem = int(data["sem"])
        sel_date = data["date"]

        canAddAttendence = True

        teacher_dep = int(Teachers.objects.get(teacher_id=TEACHER_ID).dep_id)

        if teacher_dep != sel_dep:
            canAddAttendence = False
            return HttpResponse("sta['e']end")

        for stu_id in attend.keys():
            stu_dep = int(Student.objects.get(stu_id=stu_id).dep_id)
            stu_sem = int(Student.objects.get(stu_id=stu_id).current_sem)
            if stu_dep != teacher_dep or sel_sem != stu_sem:
                canAddAttendence = False
                break

        count = 0
        if (canAddAttendence):
            for stu_id in attend.keys():
                obj = Attendence()
                stuId = Student.objects.get(stu_id=stu_id).stu_id
                obj.stu_id = stuId
                obj.dep_id = sel_dep
                obj.sem = data["sem"]
                obj.date = datetime.date.today() if sel_date == "" else sel_date
                obj.attend = attend[stu_id]
                obj.save()
                count = count + 1
        else:
            return HttpResponse('sta["e"]end')

        if count == len(attend.keys()):
            return HttpResponse('sta["s"]end')
    else:
        return HttpResponse('sta["l"]end')



def viewattendence(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        date = request.GET.get('date')
        if login_user.get('user') == "principal":
            dep = request.GET.get('dep')
            sem = request.GET.get('sem')
            stu = request.GET.get('stu')
            # print(date)

            if stu == None:
                if date == None:
                    date = datetime.date.today()
                else:
                    date = datetime.datetime.strptime(date, "%Y-%m")
                this_month = date.strftime("%m")
                this_year = date.strftime("%Y")
                attend = Attendence.objects.filter(dep_id=dep, sem=sem, date__month=this_month).values()
                # print(attend)
                students = Student.objects.filter(dep_id=dep, current_sem=sem).values('stu_id', 'adm_no', 'name', 'image')
                for a in attend:
                    a['date'] = str(a['date'])

                num_days = monthrange(int(this_year), int(this_month))

                month_days = []
                for i in range(1, num_days[1] + 1):
                    sel_day = i if i >= 10 else '0' + str(i)
                    week = datetime.datetime.strptime(this_year + '-' + this_month + '-' + str(sel_day),
                                                      "%Y-%m-%d").strftime("%a")
                    days = {'day': sel_day, 'week': week }
                    month_days.append(days)

                # print(students)
                # print(attend)

                month_attend = []
                for s in students:
                    stu = {'stu_id': s['stu_id'], 'name': s['name'], 'adm': s['adm_no'], 'image': s['image'], 'days': []}
                    for i in range(num_days[0], num_days[1] + 1):
                        sel_day = i if i >= 10 else '0' + str(i)
                        days = {'day': sel_day, 'attend': ''}

                        for a in attend:
                            if s['stu_id'] == a['stu_id']:
                                if str(a['date'][-2:]) == str(sel_day):
                                    days['attend'] = a['attend']
                        stu['days'].append(days)
                    month_attend.append(stu)
                # print(month_attend)

                context = {
                    'context': 'class',
                    'attendence': month_attend,
                    'days' : month_days,
                    'm': this_month,
                    'y': this_year
                }
                return render(request, 'attendence/viewAttendencePrincipal.html', context)

        else:
            STUDENT_ID = login_user.get('id')

            if date == None:
                date = datetime.date.today()
            else:
                date = datetime.datetime.strptime(date, "%Y-%m")

            # print(date)
            this_month = date.strftime("%m")
            this_year = date.strftime("%Y")
            num_days = monthrange(int(this_year), int(this_month))

            weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

            week = datetime.datetime.strptime(this_year + '-' + this_month + '-01', "%Y-%m-%d").strftime("%a")

            week_start = weeks.index(week)

            dep = int(Student.objects.get(stu_id=STUDENT_ID).dep_id)
            attend = Attendence.objects.filter(stu_id=STUDENT_ID, dep_id=dep, date__month=this_month, date__year=this_year).values('date', 'attend')
            for a in attend:
                a['date'] = a['date'].strftime("%d")
            # print(attend)

            days = []
            month_days = 1
            count = 1
            while count <= 42:
                if count > week_start and month_days <= num_days[1]:
                    sel_day = month_days if month_days >= 10 else '0' + str(month_days)
                    days.append(str(sel_day))
                    month_days += 1
                else:
                    days.append('')
                count += 1
            # print(days)

            context = {
                'attend': attend,
                'days': days,
                'weeks': weeks,
                'm': this_month,
                'y': this_year
            }

            return render(request, 'attendence/attendence.html', context)
    else:
        return HttpResponseRedirect('/login/login')


def addattendence(request):
    if request.session['login_user'] != "":
        TEACHER_ID = request.session['login_user'].get('id')
        dep = request.GET.get('dep')
        sem = request.GET.get('sem')
        if ClassTeacher.objects.filter(dep_id=dep, sem=sem, teacher_id=TEACHER_ID).count() > 0 or Department.objects.filter(hod=TEACHER_ID).count() > 0 :
            students = Student.objects.filter(dep_id=dep, current_sem=sem).values('stu_id', 'adm_no', 'name', 'dep_id', 'current_sem', 'image').order_by('adm_no')

            if Department.objects.filter(hod=TEACHER_ID).count() > 0:
                context = {
                    'stu': students,
                    'dep_id': dep,
                    'sem': sem,
                    'dep_name': Department.objects.get(dep_id=dep).short_name
                }
            else:
                context = {
                    'stu': students,
                    'dep_name': Department.objects.get(dep_id=dep).short_name
                }
            # print(students)

            return render(request, 'attendence/addAttendence.html', context)

        else:
            return HttpResponse("Only authorised user can upload attendence")
    else:
        return HttpResponseRedirect('/login/login')


def editattendence(request):
    if request.session['login_user'] != "":
        TEACHER_ID = request.session['login_user'].get('id')
        if request.method == "POST":
            attend_id = request.POST.get('id')
            attend = request.POST.get('attend')
            att = Attendence.objects.get(attend_id=attend_id)
            att.attend = attend
            att.save()
            return HttpResponse('sta["s"]end')
        else:
            department = Department.objects.filter(hod=TEACHER_ID).values('dep_id')
            if department.count() > 0:
                dep_id = department[0]['dep_id']
                sem = request.GET.get('sem')
                date = request.GET.get('date')
                if Attendence.objects.filter(dep_id=dep_id, sem=sem, date=date).count() > 0:
                    attendence = Attendence.objects.filter(dep_id=dep_id, sem=sem, date=date).values()
                    # print(attendence)
                    for att in attendence:
                        student = Student.objects.get(stu_id=att['stu_id'])
                        att['name'] = student.name
                        att['image'] = student.image
                        att['adm_no'] = student.adm_no
                        att['date'] = str(att['date'])
                        att['current_sem'] = att['sem']
                        del att['sem']
                    print(attendence)
                    return render(request, 'attendence/addAttendence.html', {'stu': attendence, 'user': "hod", 'date': date, 'dep_name': Department.objects.get(dep_id=dep_id).short_name})
                else:
                    return render(request, 'attendence/addAttendence.html', {'noAtt': True, 'date': date, 'dep_name': Department.objects.get(dep_id=dep_id).short_name})
            else:
                return HttpResponse("authorised person only")
    else:
        return HttpResponseRedirect('/login/login')


