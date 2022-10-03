# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from classworks.models import Classwork, ClassMedia, UserShare
# from teachers.models import Teachers
# from student.models import Student
# from subject.models import Subject
#
# import json
# import datetime
#
# # Create your views here.
#
#
# def addclasswork(request):
#     if request.method == "POST":
#         data = json.loads(request.POST.get('d'))
#         obj = Classwork()
#         obj.dep_id = data.get('dep')
#         obj.sem = data.get('sem')
#         obj.sub_id = data.get('sub')
#         obj.title = data.get('title').title()
#         obj.body = data.get('body').capitalize()
#         obj.date = datetime.date.today()
#         obj.due_date = None if data.get('date') == "" else data.get('date')
#         obj.due_time = None if data.get('time') == "" else data.get('time')
#         obj.save()
#         return HttpResponse('sta["s"]end')
#     else:
#         TEACHER_ID = 1
#         dep = request.GET.get('dep')
#         sem = request.GET.get('sem')
#         sub = request.GET.get('sub')
#         return render(request, 'classworks/../classroom/templates/classroom/addClasswork.html', {'dep': dep, 'sem': sem, 'sub': sub})
#
# def viewclasswork(request):
#     return render(request, 'classworks/../classroom/templates/classroom/viewClasswork.html')
#
#
# def addusershare(request):
#     login_user = {"user": "teacher", "id": 1}
#     if request.method == "POST":
#         share = request.POST.get('userShareBody')
#         dep = request.POST.get('dep')
#         sem = request.POST.get('sem')
#         sub = request.POST.get('sem')
#
#         canShare = False
#         if login_user.get('user') == "student":
#             stu = Student.objects.get(stu_id=login_user.get('id'))
#             if Subject.objects.filter(sub_id=sub, sem=stu.current_sem, dep_id=stu.dep_id).count() > 0:
#                 canShare = True
#             else:
#                 canShare = False
#                 return HttpResponse('sta["ids"]end')  #invalid dep and sem
#         elif login_user.get('user') == "teacher":
#             if login_user.get('id') == Subject.objects.get(sub_id=sub).teacher_id:
#                 canShare = True
#             else:
#                 canShare = False
#                 return HttpResponse('sta["ids"]end')  #invalid dep and sem
#         else:
#             canShare = False
#             return HttpResponse('sta["unf"]end')  # user not found
#
#         if canShare:
#             obj = UserShare()
#             obj.dep_id = dep
#             obj.sem = sem
#             obj.sub_id = sub
#             obj.body = share
#             obj.date = datetime.date.today()
#             obj.send_user = login_user.get('user')
#             obj.user_id = login_user.get('id')
#             obj.save()
#
#             share_id = UserShare.objects.latest('share_id').share_id
#
#             files = request.FILES
#             fileNames = files.keys()
#             for fn in fileNames:
#                 myfile = files[fn]
#                 fs = FileSystemStorage()
#                 myfilename = myfile.name.replace(' ', '')
#                 file_name = fs.save(myfilename, myfile)
#                 classmedia = ClassMedia()
#                 classmedia.name = file_name
#                 classmedia.context = "usershare"
#                 classmedia.context_id = share_id
#                 classmedia.shareby = login_user.get('user')
#                 classmedia.shareby_id = login_user.get('id')
#                 classmedia.save()
#
#         return HttpResponse('sta["s"]end')
#     else:
#         dep = request.GET.get('dep')
#         sem = request.GET.get('sem')
#         sub = request.GET.get('sub')
#         return render(request, 'classworks/../classroom/templates/classroom/adduserShare.html', {'dep': dep, 'sem': sem, 'sub': sub})
#
#
# def viewclasswork(request):
#     login_user = {'user': 'teacher', 'id': 1}
#     dep = request.GET.get('dep')
#     sem = request.GET.get('sem')
#     sub = request.GET.get('sub')
#     if login_user.get('user') == "teacher":
#         if Subject.objects.filter(dep_id=dep, sem=sem, sub_id=sub, teacher_id=login_user.get('id')).count() > 0:
#             print("ok")
#         else:
#             return HttpResponse("invalid | dep | sem | sub")
#     return render(request, 'classworks/../classroom/templates/classroom/viewClasswork.html')
