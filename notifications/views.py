from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from department.models import Department
from notifications.models import Notification, NotifConnect
from student.models import Student
from teachers.models import Teachers
from subject.models import Subject

import datetime
import json

# Create your views here.

def createnotification(login_user, stu_ids, msg):
    noti = Notification()
    noti.body = msg
    noti.send_by = login_user.get('user')
    noti.send_id = login_user.get('id')
    noti.date_time = datetime.datetime.now()
    noti.save()
    noti_id = Notification.objects.latest('notif_id').notif_id
    for s in stu_ids:
        obj = NotifConnect()
        obj.notif_id = noti_id
        obj.stu_id = s['stu_id']
        obj.save()



def viewnotifications(request):
    dep = Department.objects.all()
    return render(request, 'notifications/viewNotifications.html')


def addnotifications(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        if request.method == "POST":

            cont = json.loads(request.POST.get('cont'))
            # print(cont)
            if cont.get('cont') == "dep":
                dep_id = int(cont.get('cont_id'))
                if 'sem' in cont:
                    students = Student.objects.filter(dep_id=dep_id, current_sem=int(cont.get('sem'))).values('stu_id')
                else:
                    students = Student.objects.filter(dep_id=dep_id).values('stu_id')

            elif cont.get('cont') == "sub":
                sub_id = int(cont.get('cont_id'))
                subject = Subject.objects.get(sub_id=sub_id)
                dep_id = subject.dep_id
                sem = subject.sem
                students = Student.objects.filter(dep_id=dep_id, current_sem=sem).values('stu_id')

            elif cont.get('cont') == "stu":
                stu_id = int(cont.get('cont_id'))
                students = Student.objects.filter(stu_id=stu_id).values('stu_id')

            notif = Notification()
            notif.body = cont.get('body')
            notif.send_by = login_user.get('user')
            notif.send_id = login_user.get('id')
            notif.date_time = datetime.datetime.now()
            notif.save()
            notif_id = Notification.objects.latest('notif_id').notif_id
            for s in students:
                notif_conn = NotifConnect()
                notif_conn.notif_id = notif_id
                notif_conn.stu_id = s['stu_id']
                notif_conn.save()

            return HttpResponse('sta["s"]end')
        else:
            if login_user.get('user') == "student":
                return HttpResponseRedirect('/login/login')


            sub_id = request.GET.get('sub')
            dep_id = request.GET.get('dep')
            sem = request.GET.get('sem')
            stu_id = request.GET.get('stu')

            if stu_id is not None:
                stu = Student.objects.get(stu_id=stu_id)
                dep_id = stu.dep_id
                sem = stu.current_sem
                context = {
                    'stu': stu.name,
                    'stu_id': stu_id,
                    'adm': stu.adm_no,
                    'image': stu.image,
                    'dep': Department.objects.get(dep_id=dep_id).short_name,
                    'sem': sem
                }
                if login_user.get('user') == "admin":
                    return render(request, 'notifications/notif_admin.html', context)
                elif login_user.get('user') == "principal":
                    return render(request, 'notifications/notfi_principal.html', context)
                elif login_user.get('user') == "teacher":
                    return render(request, 'notifications/addNotifications.html', context)

            if sub_id is not None and stu_id is None:
                subject = Subject.objects.get(sub_id=sub_id)
                dep_id = subject.dep_id
                sem = subject.sem
                context = {
                    'dep': Department.objects.get(dep_id=dep_id).name,
                    'sem': sem,
                    'sub_id': sub_id
                }
                return render(request, 'notifications/addNotifications.html', context)

            elif dep_id is not None and sem is None and stu_id is None:
                dep = Department.objects.get(dep_id=dep_id)
                context = {
                    'dep': dep.name,
                    'sem': '1 - ' + str( int(dep.duration)*2 ),
                    'dep_id': dep_id
                }
                if login_user.get('user') == "admin":
                    return render(request, 'notifications/notif_admin.html', context)
                elif login_user.get('user') == "principal":
                    return render(request, 'notifications/notfi_principal.html', context)

            elif dep_id is not None and sem is not None and stu_id is None:
                dep = Department.objects.get(dep_id=dep_id)
                context = {
                    'dep': dep.name,
                    'sem': sem,
                    'dep_id': dep_id,
                    'sem_id': sem
                }
                if login_user.get('user') == "admin":
                    return render(request, 'notifications/notif_admin.html', context)
                elif login_user.get('user') == "principal":
                    return render(request, 'notifications/notfi_principal.html', context)
                # else:
                    # return HttpResponseRedirect('/login/login')
            else:
                print("not sub")
    else:
        return HttpResponseRedirect('/login/login')


def getmynotifications(request):
    STUDENT_ID = request.session['login_user'].get('id')
    notifications = []
    all_notif = []
    notif = NotifConnect.objects.filter(stu_id=STUDENT_ID).values('notif_id', 'stu_id').order_by('-connnect_id')
    for n in notif:
        noti = Notification.objects.filter(notif_id=n['notif_id']).values('body', 'send_by', 'send_id', 'date_time')
        for no in noti:
            if no['send_by'] == "teacher":
                no['send_by'] = Teachers.objects.get(teacher_id=no['send_id']).name
            no['date'] = no['date_time'].strftime("%A, %d %B")
            no['time'] = no['date_time'].strftime("%I:%M %p")
            del no['date_time']
            all_notif.append(no)

            if len(notifications) == 0:
                notifications.append({'date': no['date']})
            else:
                for i in notifications:
                    if no['date'] not in i.values():
                        notifications.append({'date': no['date']})


    for i in notifications:
        i['notif'] = []
        for j in all_notif:
            if j['date'] == i['date']:
                i['notif'].append(j)

    return notifications
