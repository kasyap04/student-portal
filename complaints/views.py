from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from student.models import Student
from teachers.models import ClassTeacher, Teachers
from department.models import Department
from complaints.models import Complaints
import datetime

# Create your views here.


def addcomplaints(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        STUDENT_ID = login_user.get('id')
        if request.method == "POST":
            to = request.POST.get('to')
            body = request.POST.get('body')
            obj = Complaints()
            obj.stu_id = STUDENT_ID
            obj.to = to
            if to == "hod":
                stu_dep = Student.objects.filter(stu_id=STUDENT_ID).values('dep_id')[0]['dep_id']
                hod = Department.objects.filter(dep_id=stu_dep).values('hod')[0]['hod']
                obj.to_id = hod
            elif to == "t":
                stu = Student.objects.filter(stu_id=STUDENT_ID).values('dep_id', 'current_sem')[0]
                stu_dep = stu['dep_id']
                sem = stu['current_sem']
                teacher_id = ClassTeacher.objects.filter(dep_id=stu_dep, sem=sem).values('teacher_id')[0]['teacher_id']
                obj.to_id = teacher_id
            elif to == "p":
                obj.to_id = 2
            else:
                obj.to_id = 1
            obj.body = body
            obj.date = datetime.datetime.now()
            obj.save()
            return HttpResponse('sta["s"]end')
        else:
            complaints = Complaints.objects.filter(stu_id=STUDENT_ID).values().order_by('-date')
            for i in complaints:
                if i['to'] == "t" or i['to'] == "hod":
                    i['teacher_name'] = Teachers.objects.filter(teacher_id=i['to_id']).values('name')[0]['name']
                elif i['to'] == "p":
                    i['teacher_name'] = "Principal"
                else:
                    i['teacher_name'] = "unknown"

                i['date'] = i['date'].strftime("%d %b %Y, %I:%M %p")

                if i['respond_date'] is not None and i['reply'] is None:
                    i['respond_status'] = "Read"
                elif i['respond_date'] is not None and i['reply'] is not None:
                    i['respond_status'] = "Replied"
                    i['respond_date'] = i['respond_date'].strftime("%d %b %Y, %I:%M %p")
                else:
                    i['respond_status'] = "Complaint filed"

            # print(complaints)
            return render(request, 'complaints/addComplaints.html', {'complaint': complaints})
    else:
        return HttpResponseRedirect('/login/login')


def viewcomplaints(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']

        if request.method == "POST":
            reply = request.POST.get('r')
            comp_id = request.POST.get('i')
            complaint = Complaints.objects.get(complaint_id=comp_id)
            complaint.reply = reply
            complaint.respond_date = datetime.datetime.now()
            complaint.save()

            return HttpResponse('sta["s"]end')
        else:
            compl_id = request.GET.get('id')
            if login_user['user'] == "teacher":
                if Department.objects.filter(hod=login_user.get('id')).count() > 0:
                    to = "hod"
                else:
                    to = "t"
            elif login_user['user'] == "principal":
                to = "p"
            complaint = Complaints.objects.filter(to=to, to_id=login_user.get('id')).values().order_by('-date')
            for c in complaint:
                student = Student.objects.get(stu_id=c['stu_id'])
                c['stu_id'] = student.name
                c['adm_no'] = student.adm_no
                c['dep'] = Department.objects.get(dep_id=student.dep_id).short_name
                c['sem'] = student.current_sem
                c['date'] = c['date'].strftime("%d %b, %Y %I:%m %p")
                c['status'] = "unread" if c['respond_date'] is None else "read"
                del c['respond_date']
                del c['to']
                del c['to_id']
                del c['body']

            # print(complaint)

            if compl_id is None:
                context = {
                    'complaints': complaint
                }
            else:
                com = Complaints.objects.get(complaint_id=compl_id)
                if com.respond_date is None:
                    com.respond_date = datetime.datetime.now()
                com.save()
                context = {
                    'complaints': complaint,
                    'comp_body': Complaints.objects.get(complaint_id=compl_id).body,
                    'comp_id': int(compl_id),
                    'from': Student.objects.get(stu_id=Complaints.objects.get(complaint_id=compl_id).stu_id).name,
                    'reply': com.reply
                }

            if login_user.get('user') == "teacher":
                return render(request, 'complaints/viewComplaints.html', context)
            elif login_user.get('user') == "principal":
                return render(request, 'complaints/viewCompPrincipal.html', context)
            else:
                return HttpResponseRedirect('/login/login')
    else:
        return HttpResponseRedirect('/login/login')
