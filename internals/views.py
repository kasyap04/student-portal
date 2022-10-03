from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from department.models import Department
from subject.models import Subject
from student.models import Student
from teachers.models import Teachers
from internals.models import Internals

import json

# Create your views here.

# TEACHER_ID = 1


def uploadinternals(request):
    data = json.loads(request.POST['internal'])
    marks = data['marks']
    if data['examname'] == 1:
        examName = "1st Internal Examination"
    elif data['examname'] == 2:
        examName = "2nd Internal Examination"
    elif data['examname'] == 3:
        examName = "Class Test"
    else:
        examName = "Unknown"

    count = 0
    for stuId in marks.keys():
        obj = Internals()
        obj.dep_id = data['dep']
        obj.sem = data['sem']
        obj.sub_id = data['sub']
        obj.stu_id = stuId
        obj.obtained_mark = marks[stuId]
        obj.total_mark = data['totalmark']
        obj.exam_name = examName
        obj.date = data['date']
        obj.save()
        count += 1

    if count == len(marks.keys()):
        return HttpResponse('sta["s"]end')
    else:
        return HttpResponse('sta["e"]end')


def fetchstudentandsubject(request):
    dep = int(request.POST.get('dep'))
    sem = int(request.POST.get('sem'))
    sub = Subject.objects.filter(dep_id=dep, sem=sem, teacher_id=TEACHER_ID).values('sub_id', 'code', 'name')
    subList = []
    for i in sub:
        subList.append(json.dumps(i))

    stuList = []
    stu = Student.objects.filter(dep_id=dep, current_sem=sem).values('stu_id', 'adm_no', 'name').order_by('adm_no')
    for i in stu:
        stuList.append( json.dumps(i) )

    allList = []
    allList.append(subList)
    allList.append(stuList)
    return HttpResponse(json.dumps(allList))


def getinternalsforstudents(reqtest):
    if reqtest.session['login_user'] != "":
        STUDENT_ID = reqtest.session['login_user'].get('id')
        sem = reqtest.POST.get('sem')
        result = []
        stu_dep = Student.objects.filter(stu_id=STUDENT_ID).values('dep_id')[0]['dep_id']
        examNames = Internals.objects.filter(dep_id=stu_dep, sem=sem, stu_id=STUDENT_ID).values('exam_name').distinct()
        for ind in examNames:
            exam_name = ind['exam_name']
            subjects = []
            getInternals = Internals.objects.filter(stu_id=STUDENT_ID, dep_id=stu_dep, sem=sem,
                                                    exam_name=exam_name).values('sub_id', 'obtained_mark', 'total_mark',
                                                                                'date')
            for internal in getInternals:
                sub_id = internal['sub_id']
                getSubjects = Subject.objects.filter(sub_id=sub_id).values('name', 'code')
                for sub in getSubjects:
                    mark = {'code': sub['code'], 'name': sub['name'], 'mark': internal['obtained_mark'],
                            'total': internal['total_mark'], 'date': str(internal['date'])}
                    subjects.append(mark)
            ind['sub'] = subjects
        for res in examNames:
            result.append(res)
        return HttpResponse(json.dumps(result))

# [
#     {
#         exam_name: "",
#         sub:[
#             {
#                 code: "",
#                 name: "",
#                 mark: "",
#                 total_mark: "",
#                 date: ""
#             },
#         ]
#     },
# ]


def viewintrnals(request):
    if request.session['login_user'] != "":
        if request.method == "POST":
            return HttpResponse("hii")
        else:
            sub_id = request.GET.get('sub')

            return render(request, 'internals/viewInternals.html')
    else:
        return HttpResponseRedirect('/login/login')


def addinternals(request):
    if request.session['login_user'] != "":
        if request.method == "POST":
            data = json.loads(request.POST.get('i'))
            marks = data.get('marks')

            exam_no = int(data.get('exam_name'))

            if exam_no == 1:
                examName = "1st internal examination"
            elif exam_no == 2:
                examName = "2nd internal examination"
            elif exam_no == 3:
                examName = "Class test"
            else:
                examName = "unknown"

            subject = Subject.objects.get(sub_id=data.get('sub'))
            dep_id = subject.dep_id
            sem = subject.sem
            for m in marks:
                obj = Internals()
                obj.dep_id = dep_id
                obj.sem = sem
                obj.sub_id = data.get('sub')
                obj.stu_id = m['stu_id']
                obj.obtained_mark = m['mark']
                obj.total_mark = data.get('total_mark')
                obj.exam_name = examName
                obj.date = data.get('date')
                obj.save()

            return HttpResponse('sta["s"]end')
        else:
            sub_id = request.GET.get('sub')
            subject = Subject.objects.get(sub_id=sub_id)
            sub = subject.name + ' (' + subject.code + ')'
            sem = subject.sem
            dep = Department.objects.get(dep_id=subject.dep_id).short_name
            students = Student.objects.filter(dep_id=subject.dep_id, current_sem=sem).values('stu_id', 'adm_no', 'name', 'image').order_by('adm_no')

            context = {
                'dep': dep,
                'sem': sem,
                'sub': sub,
                'sub_id': sub_id,
                'students': students
            }
        return render(request, 'internals/addInternals.html', context)
    else:
        return HttpResponseRedirect('/login/login')




def fetchinternals(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "principal":
            dep = request.GET.get('dep')
            sem = request.GET.get('sem')
            exam_no = int(request.GET.get('exam'))

            if exam_no == 1 or exam_no is None:
                examName = "1st internal examination"
            elif exam_no == 2:
                examName = "2nd internal examination"
            elif exam_no == 3:
                examName = "Class test"
            else:
                examName = "unknown"


            intExam = Internals.objects.filter(dep_id=dep, sem=sem, exam_name=examName)

            if intExam.count() > 0:
                sub_ids = []
                stu_ids = []
                for i in intExam.values():

                    if len(sub_ids) == 0:
                        sub_ids.append(i['sub_id'])
                    else:
                        if i['sub_id'] not in sub_ids:
                            sub_ids.append(i['sub_id'])

                    if len(stu_ids) == 0:
                        stu_ids.append(i['stu_id'])
                    else:
                        if i['stu_id'] not in stu_ids:
                            stu_ids.append(i['stu_id'])

                sub_names = []
                for s in sub_ids:
                    sub = Subject.objects.get(sub_id=s).name
                    sub_names.append(sub)

                # print(stu_ids)

                my_marks = []

                for s in stu_ids:
                    stu = Student.objects.get(stu_id=s)
                    stu_mark = {
                        'name': stu.name,
                        'adm_no': stu.adm_no,
                        'img': stu.image,
                        'marks': []
                    }

                    for sb in sub_ids:
                        mark_sub = Internals.objects.get(dep_id=dep, sem=sem, exam_name=examName, stu_id=s, sub_id=sb)
                        marks = {
                            'obtained': mark_sub.obtained_mark,
                            'total': mark_sub.total_mark
                        }
                        stu_mark['marks'].append(marks)
                    my_marks.append(stu_mark)
                # print(my_marks)


                    # my_exam = Internals.objects.filter(dep_id=dep, sem=sem, exam_name=examName, stu_id=s).values()
                    # for m in my_exam:
                    #     stu = Student.objects.get(stu_id=m['stu_id'])
                    #     stu_mark = {
                    #         'name': stu.name,
                    #         'adm_no': stu.adm_no,
                    #         'img': stu.image,
                    #         'marks': []
                    #     }
                    #
                    #     for sb in sub_ids:
                    #         mark_sub = Internals.objects.get(dep_id=dep, sem=sem, exam_name=examName,
                    #                                          stu_id=s, sub_id=sb)
                    #         for ms in mark_sub:
                    #             stu_mark['marks'] = {
                    #                 'obtained': mark_sub.obtained_mark,
                    #                 'total': mark_sub.total_mark
                    #             }



                # for s in sub_ids:
                #     my_exam = Internals.objects.filter(dep_id=dep, sem=sem, exam_name=examName, sub_id=s).values()
                #     for m in my_exam:
                #         stu = Student.objects.get(stu_id=m['stu_id'])
                #         m['stu_name'] = stu.name
                #         m['adm_no'] = stu.adm_no
                #         m['image'] = stu.image
                #         m['sub_name'] = Subject.objects.get(sub_id=m['sub_id']).name
                #         del m['dep_id']
                #         del m['sem']
                #         del m['stu_id']
                #         del m['sub_id']
                #         del m['exam_name']
                #     my_marks.append(my_exam)
                #
                # print(my_marks)

                context = {
                    'subjects': sub_names,
                    'marks': my_marks,
                    'exam': exam_no
                }
                return render(request, 'internals/viewStudentInternals.html', context)
            else:
                return HttpResponse('No internals found')


            # dep = request.GET.get('dep')
            # sem = request.GET.get('sem')
            # exam = request.GET.get('exam')
            # stu_id = Internals.objects.filter(dep_id=dep, sem=sem, exam_name=exam).values(
            #     'stu_id').order_by().distinct()
            # result = []
            # for s in stu_id:
            #     stu = {'stu_id': s['stu_id'],
            #            'name': Student.objects.filter(stu_id=s['stu_id']).values('name')[0]['name']}
            #     internals = Internals.objects.filter(dep_id=dep, sem=sem, exam_name=exam, stu_id=s['stu_id']).values()
            #     for i in internals:
            #         i['sub_name'] = Subject.objects.filter(sub_id=i['sub_id']).values('name')[0]['name']
            #         i['date'] = str(i['date'])
            #         del i['dep_id']
            #         del i['sem']
            #         del i['stu_id']
            #         del i['exam_name']
            #     stu['int'] = internals
            #     result.append(stu)
            #     subjects = Internals.objects.filter(dep_id=dep, sem=sem, exam_name=exam).values('sub_id').distinct()
            #     for sub in subjects:
            #         sub['sub_name'] = Subject.objects.filter(sub_id=sub['sub_id']).values('name')[0]['name']
            #         sub['date'] = str(
            #             Internals.objects.filter(dep_id=dep, sem=sem, exam_name=exam, sub_id=sub['sub_id']).values(
            #                 'date')[0]['date'])
            #     subjects[0]['count'] = len(subjects) * 2
            # print(stu_id)
            # return render(request, 'internals/viewStudentInternals.html', {'internal': result, 'subject': subjects})
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponseRedirect('/login/login')


def editinternals(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        if login_user.get('user') == "teacher":
            TEACHER_ID = login_user.get('id')
            if request.method == "POST":
                mark = request.POST.get('mark')
                int_id = request.POST.get('id')
                obj = Internals.objects.get(int_id=int_id)
                obj.obtained_mark = mark
                obj.save()
                return HttpResponse('sta["s"]end')
            else:
                sub_id = request.GET.get('sub')
                stu_id = request.GET.get('stu')

                subjects = Subject.objects.get(sub_id=sub_id)
                dep_id = subjects.dep_id
                sem = subjects.sem

                if stu_id is None:
                    students = Student.objects.filter(dep_id=dep_id, current_sem=sem).values('stu_id', 'adm_no', 'name',
                                                                                             'image').order_by('adm_no')
                    context = {
                        'students': students,
                        'sub': subjects.name,
                        'sub_id': sub_id,
                        'dep': Department.objects.get(dep_id=dep_id).short_name,
                        'sem': sem
                    }
                elif sub_id is not None and stu_id is not None:

                    internals = Internals.objects.filter(sub_id=sub_id, stu_id=stu_id).values()
                    for i in internals:
                        i['date'] = i['date'].strftime("%b %d, %Y")
                        del i['dep_id']
                        del i['sem']
                        del i['stu_id']

                    students = Student.objects.get(stu_id=stu_id)

                    context = {
                        'sub': subjects.name,
                        'dep': Department.objects.get(dep_id=dep_id).short_name,
                        'sem': sem,
                        'stu_id': stu_id,
                        'stu_name': students.name,
                        'stu_adm': students.adm_no,
                        'stu_image': students.image,
                        'internals': internals
                    }
                    print(context)
                return render(request, 'internals/editInternal.html', context)
        else:
            return HttpResponse("Unauthorized user")
    else:
        return HttpResponseRedirect('/login/login')