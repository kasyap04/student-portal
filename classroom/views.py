from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from classroom.models import Classwork, ClassMedia, UserShare, Classroom, Submited
from teachers.models import Teachers
from student.models import Student
from subject.models import Subject
from department.models import Department

import json
import datetime
import os


# Create your views here.


def addclasswork(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        data = json.loads(request.POST.get('d'))
        obj = Classwork()
        dep = data.get('dep')
        sem = data.get('sem')
        sub = data.get('sub')
        if Subject.objects.filter(dep_id=dep, sem=sem, sub_id=sub, teacher_id=login_user.get('id')).count() > 0:
            obj.title = data.get('title').title()
            obj.body = data.get('body').capitalize()
            obj.date = datetime.date.today()
            obj.due_date = data.get('date')
            obj.due_time = data.get('time')
            obj.save()

            classroom = Classroom()
            # classroom.dep_id = dep
            # classroom.sem = sem
            classroom.sub_id = sub
            classroom.context = "classwork"
            classroom.context_id = Classwork.objects.latest('work_id').work_id
            classroom.save()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["e"]end')
    else:
        return HttpResponse('sta["l"]end')


def addusershare(request):
    # login_user = {"user": "teacher", "id": 1}
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        if request.method == "POST":
            share = request.POST.get('userShareBody')
            dep = request.POST.get('dep')
            sem = request.POST.get('sem')

            sub = request.POST.get('sub')

            canShare = False
            if login_user.get('user') == "student":
                stu = Student.objects.get(stu_id=login_user.get('id'))
                if Subject.objects.filter(sub_id=sub, sem=stu.current_sem, dep_id=stu.dep_id).count() > 0:
                    canShare = True
                else:
                    canShare = False
                    return HttpResponse('sta["is"]end')  # invalid subject
            elif login_user.get('user') == "teacher":
                if login_user.get('id') == Subject.objects.get(sub_id=sub).teacher_id:
                    canShare = True
                else:
                    canShare = False
                    return HttpResponse('sta["is"]end')  # invalid subject
            elif login_user.get('user') == "principal":
                canShare = True
            else:
                canShare = False
                return HttpResponse('sta["unf"]end')  # user not found

            if canShare:
                obj = UserShare()
                # obj.dep_id = dep
                # obj.sem = sem
                # obj.sub_id = sub

                obj.body = share
                obj.date = datetime.date.today()
                obj.send_user = login_user.get('user')
                obj.user_id = login_user.get('id')
                obj.save()

                share_id = UserShare.objects.latest('share_id').share_id

                classroom = Classroom()
                # classroom.dep_id = dep
                # classroom.sem = sem
                classroom.sub_id = sub
                classroom.context = "usershare"
                classroom.context_id = share_id
                classroom.save()

                # print(share) ;

                files = request.FILES
                print(files)
                fileNames = files.keys()
                for fn in fileNames:
                    myfile = files[fn]
                    fs = FileSystemStorage()
                    myfilename = 'uploads/' + myfile.name.replace(' ', '')
                    file_name = fs.save(myfilename, myfile)
                    classmedia = ClassMedia()
                    classmedia.name = file_name
                    classmedia.context = "usershare"
                    classmedia.context_id = share_id
                    classmedia.shareby = login_user.get('user')
                    classmedia.shareby_id = login_user.get('id')
                    classmedia.save()

                return HttpResponse('sta["s"]end')
            else:
                return HttpResponse('sta["e"]end')
        # else:
        #     dep = request.GET.get('dep')
        #     sem = request.GET.get('sem')
        #     sub = request.GET.get('sub')
        #     return render(request, 'classroom/adduserShare.html', {'dep': dep, 'sem': sem, 'sub': sub})
    else:
        return HttpResponseRedirect('/login/login');


def getFileType(fileName):
    if fileName.lower().endswith('.docx'):
        return "WordDocument"
    elif fileName.lower().endswith('.pptx'):
        return "PowerPoint"
    elif fileName.lower().endswith('.pdf'):
        return "PDF"
    elif fileName.lower().endswith(('.png', '.jpg', '.jpeg', '.img')):
        return "IMAGE"
    elif fileName.lower().endswith(('.m4a', '.mp3', '.wav', '.aac')):
        return "AUDIO"
    elif fileName.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm')):
        return "VIDEO"
    else:
        return "unknown"


def viewclassroom(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']

        sub = request.GET.get('sub')
        subject = Subject.objects.get(sub_id=sub)
        canView = False
        if login_user.get('user') == "student":
            stu = Student.objects.get(stu_id=login_user.get('id'))
            # subject = Subject.objects.get(sub_id=sub)
            if subject.dep_id == stu.dep_id and subject.sem == stu.current_sem:
                canView = True
        elif login_user.get('user') == "teacher":
            if Subject.objects.filter(sub_id=sub, teacher_id=login_user.get('id')).count() > 0:
                canView = True
        elif login_user.get('user') == "principal":
            canView = True

        if canView:
            classroom = Classroom.objects.filter(sub_id=sub).values().order_by('-classroom_id')
            for cr in classroom:
                if cr['context'] == "classwork":
                    teacher_id = Subject.objects.get(sub_id=cr['sub_id']).teacher_id
                    cr['teacher_name'] = Teachers.objects.get(teacher_id=teacher_id).name
                    classwork = Classwork.objects.get(work_id=cr['context_id'])
                    cr['work_title'] = classwork.title
                    cr['work_body'] = classwork.body
                    cr['work_date'] = classwork.date
                    cr['work_due_date'] = classwork.due_date
                    cr['work_due_time'] = classwork.due_time

                    if login_user.get('user') == "student":
                        if Submited.objects.filter(stu_id=login_user.get('id'), work_id=cr['context_id']).count() > 0:
                            submited = Submited.objects.get(stu_id=login_user.get('id'), work_id=cr['context_id'])
                            cr['work_submited_status1'] = "Handed in"
                            cr['work_submited_date'] = submited.date
                            if submited.date > cr['work_date']:
                                cr['work_submited_status2'] = "Done late"
                            elif submited.time > cr['work_due_time']:
                                cr['work_submited_status2'] = "Done late"
                        else:
                            if datetime.date.today() > cr['work_date']:
                                cr['work_submited_status1'] = "Missing"
                            elif datetime.datetime.now().strftime("%H:%M:%S") > cr['work_due_time']:
                                cr['work_submited_status1'] = "Missing"
                            else:
                                cr['work_submited_status1'] = "Pending"

                    cr['work_due_time'] = datetime.datetime.strptime(cr['work_due_time'], "%H:%M").strftime("%I:%M %p")

                if cr['context'] == "usershare":
                    usershare = UserShare.objects.get(share_id=cr['context_id'])

                    cr['share_body'] = usershare.body[0:usershare.body.find('stali[')]
                    cr['attachments'] = 0
                    if usershare.body.find('stali[') > 0:
                        links = json.loads(
                            usershare.body[usershare.body.find('stali[') + 5:usershare.body.find(']endli') + 1])
                        userShare_links = []
                        for link in links:
                            userShare_links.append({'url': link})
                        cr['links'] = userShare_links
                        cr['attachments'] += len(links)
                    cr['share_date'] = usershare.date

                    if ClassMedia.objects.filter(context_id=cr['context_id']).count() > 0:
                        cr['share_medias'] = ClassMedia.objects.filter(context_id=cr['context_id']).values('name')
                        for sm in cr['share_medias']:
                            sm['name'] = sm['name'].replace('uploads/', '')
                            sm['ext'] = getFileType(sm['name'])
                        cr['attachments'] += len(cr['share_medias'])

                    if usershare.send_user == "teacher":
                        cr['share_name'] = Teachers.objects.get(teacher_id=usershare.user_id).name
                    elif usershare.send_user == "student":
                        cr['share_name'] = Student.objects.get(stu_id=usershare.user_id).name
                    elif usershare.send_user == "principal":
                        cr['share_name'] = "Principal"
            # print(classroom)
            sub_details = {'sub_id': subject.sub_id, 'sub_name': subject.name.title(), 'sub_code': subject.code,
                           'teacher_name': Teachers.objects.get(teacher_id=subject.teacher_id).name}
            students = Student.objects.filter(dep_id=subject.dep_id, current_sem=subject.sem).values('stu_id', 'image', 'adm_no', 'name').order_by('adm_no')

            if login_user.get('user') == "student":
                return render(request, 'classroom/viewClassroom.html',
                              {'classroom': classroom, 'user': 'student', 'sub_details': sub_details, 'student': students})
            elif login_user.get('user') == "teacher" or login_user.get('user') == "principal":
                sub_details['dep_id'] = subject.dep_id
                sub_details['dep_name'] = Department.objects.get(dep_id=subject.dep_id).short_name
                sub_details['sem'] = subject.sem
                # print(sub_details)
                return render(request, 'classroom/viewClassroom.html',
                              {'classroom': classroom, 'user': login_user.get('user'), 'sub_details': sub_details, 'student': students})
        else:
            return HttpResponseRedirect('/login/login')
    else:
        return HttpResponseRedirect('/login/login')


def submitclasswork(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        # login_user = {'user': 'teacher', 'id': 1}
        if request.method == "POST":
            files = request.FILES
            fileNames = files.keys()
            if len(fileNames) > 0:
                obj = Submited()
                obj.work_id = request.POST.get('workid')
                obj.stu_id = login_user.get('id')
                obj.date = datetime.date.today()
                obj.time = datetime.datetime.now().strftime("%H:%M:%S")
                obj.save()

                for fn in fileNames:
                    myfile = files[fn]
                    print(myfile)
                    fs = FileSystemStorage()
                    myfilename = 'uploads/' + myfile.name.replace(' ', '')
                    file_name = fs.save(myfilename, myfile)
                    classmedia = ClassMedia()
                    classmedia.name = file_name
                    classmedia.context = "classwork"
                    classmedia.context_id = request.POST.get('workid')
                    classmedia.shareby = login_user.get('user')
                    classmedia.shareby_id = login_user.get('id')
                    classmedia.save()
                return HttpResponse('sta["s"]end')
            else:
                return HttpResponse('sta["mnf"]end')  # media not found
        else:
            work_id = request.GET.get('work')
            stu_id = request.GET.get('stu')

            sub = Classroom.objects.get(context="classwork", context_id=work_id).sub_id
            subject = Subject.objects.get(sub_id=sub)
            student = Student.objects.get(stu_id=login_user.get('id'))

            classwork = Classwork.objects.filter(work_id=work_id).values()[0]
            # classwork['date'] = classwork['date']
            # classwork['due_date'] = classwork['due_date']
            classwork['due_time'] = datetime.datetime.strptime(classwork['due_time'], "%H:%M").strftime("%I:%M %p")
            classwork['teacher_name'] = Teachers.objects.get(teacher_id=subject.teacher_id).name
            classwork['sub_name'] = subject.name

            if login_user.get('user') == "student":
                if subject.dep_id == student.dep_id and subject.sem == student.current_sem:
                    if Submited.objects.filter(stu_id=student.stu_id, work_id=work_id).count() > 0:
                        submited = Submited.objects.filter(stu_id=student.stu_id, work_id=work_id).values()[0]
                        submited['medias'] = ClassMedia.objects.filter(context="classwork", context_id=work_id).values(
                            'media_id', 'name')

                        for med in submited['medias']:
                            med['name'] = med['name'].replace('uploads/', '')
                            med['ext'] = getFileType(med['name'])

                        if classwork['due_date'] < submited['date']:
                            classwork['due_status'] = "Done late"
                        elif classwork['due_date'] == submited['date']:
                            if classwork['due_time'] < submited['time']:
                                classwork['due_status'] = "Done late"

                        # print(submited)
                        return render(request, 'classroom/submitClasswork.html',
                                      {'classwork': classwork, 'submited': submited})
                    else:
                        if classwork['due_date'] < datetime.date.today():
                            classwork['due_status'] = "Missing"
                        elif classwork['due_time'] < str(datetime.datetime.now()):
                            classwork['due_status'] = "Missing"
                        # print(classwork)
                        return render(request, 'classroom/submitClasswork.html', {'classwork': classwork})
                else:
                    return HttpResponse('sta["e"]end')
            else:
                dep = subject.dep_id
                sem = subject.sem
                allStudents = Student.objects.filter(dep_id=dep, current_sem=sem).values('stu_id', 'adm_no', 'name',
                                                                                         'image').order_by('adm_no')
                submitedStudents = Submited.objects.filter(work_id=work_id).values('stu_id', 'date', 'time')
                work = Classwork.objects.get(work_id=work_id)
                dueDate = work.due_date
                dueTime = work.due_time
                # print(allStudents)
                # print(submitedStudents)
                for s in allStudents:
                    s['status'] = "Missing"
                    for sub in submitedStudents:
                        if s['stu_id'] == sub['stu_id']:
                            s['status'] = "Handed in"
                            if dueDate < sub['date']:
                                s['remark'] = 'Done late'
                            elif dueDate == sub['date']:
                                if dueTime < sub['time']:
                                    s['remark'] = 'Done late'
                            s['date'] = sub['date'].strftime("%b %d, %Y") + ' ' + datetime.datetime.strptime(
                                sub['time'], "%H:%M:%S").strftime("%I:%M %p")
                            # s['time'] = datetime.datetime.strptime(sub['time'], "%H:%M:%S")
                        else:
                            s['status'] = "Missing"
                if stu_id == None:
                    print(allStudents)
                    return render(request, 'classroom/submitClasswork.html',
                                  {'classwork': classwork, 'students': allStudents})
                else:
                    # stu = Student.objects.get(stu_id=stu_id)
                    if Submited.objects.filter(work_id=work_id, stu_id=stu_id).count() > 0:
                        work_done = {'stu_id': int(stu_id),
                                     'medias': ClassMedia.objects.filter(context="classwork", context_id=work_id,
                                                                         shareby="student", shareby_id=stu_id).values(
                                         'name')}
                        for wd in work_done['medias']:
                            wd['ext'] = getFileType(wd['name'])
                            wd['file'] = wd['name'].replace('uploads/', '')
                    else:
                        work_done = {'stu_id': int(stu_id)}
                    print(work_done)
                    return render(request, 'classroom/submitClasswork.html',
                                  {'classwork': classwork, 'workdone': work_done, 'students': allStudents})
    else:
        return HttpResponseRedirect('/login/login')


def unsubmit(request):
    login_user = {'user': 'student', 'id': 1}
    if login_user.get('user') == "student":
        STUDENT_ID = login_user.get('id')
        work_id = request.POST.get('workid')
        work_sub = Classroom.objects.get(context="classwork", context_id=work_id).sub_id
        subject = Subject.objects.get(sub_id=work_sub)
        student = Student.objects.get(stu_id=STUDENT_ID)
        if student.dep_id == subject.dep_id and student.current_sem == subject.sem:
            Submited.objects.get(stu_id=STUDENT_ID, work_id=work_id).delete()
            medias = ClassMedia.objects.filter(context="classwork", context_id=work_id, shareby="student",
                                               shareby_id=STUDENT_ID).values('name', 'media_id')
            for m in medias:
                path = os.path.join('static/', m['name'])
                os.remove(path)
                ClassMedia.objects.get(media_id=m['media_id']).delete()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["e"]end')
    else:
        return HttpResponse('sta["e"]end')


def today_classwork(stu_id):
    today = datetime.date.today()
    student = Student.objects.get(stu_id=stu_id)
    stu_dep = student.dep_id
    stu_sem = student.current_sem
    today_work = []
    subjects = Subject.objects.filter(dep_id=stu_dep, sem=stu_sem).values('sub_id', 'name', 'teacher_id')
    for sub in subjects:
        if Classroom.objects.filter(sub_id=sub['sub_id'], context='classwork').count() > 0:
            work_id = Classroom.objects.filter(sub_id=sub['sub_id'], context='classwork').values('context_id').order_by(
                '-classroom_id')
            for wi in work_id:
                if Classwork.objects.filter(work_id=wi['context_id']).count() > 0 and Submited.objects.filter(
                        work_id=wi['context_id'], stu_id=stu_id).count() == 0:
                    classwork = Classwork.objects.get(work_id=wi['context_id'])
                    work = {'work_id': wi['context_id'], 'date': classwork.date, 'tile': classwork.title,
                            'body': classwork.body,
                            'teacher': Teachers.objects.get(teacher_id=sub['teacher_id']).name}
                    today_work.append(work)

    return today_work
