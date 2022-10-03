from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from login.models import Login

from notifications.views import createnotification

import datetime
import random

def login(request):
    if request.method == "POST":
        un = request.POST.get("userid")
        ps = request.POST.get("pass")
        if Login.objects.filter(username=un, password=ps).count() > 0:
            logn = Login.objects.get(username=un, password=ps)
            login_user = {'user': logn.type, 'id': logn.u_id, 'key': logn.login_key}
            request.session['login_user'] = login_user
            # request.set_cookie('login_user', login_user)
            lastlogin = Login.objects.get(username=un, password=ps)
            lastlogin.last_login = datetime.datetime.now()
            lastlogin.save()
            print(request.session['login_user'])
            if login_user.get('user') == "student":
                return HttpResponse('sta["stu"]end')  # redirect to student
            elif login_user.get('user') == "teacher":
                return HttpResponse('sta["tea"]end')
            elif login_user.get('user') == "admin":
                return HttpResponse('sta["adm"]end')
            elif login_user.get('user') == "principal":
                return HttpResponse('sta["pri"]end')
            else:
                return HttpResponse('sta["iu"]end')  #invalid user
        else:
            return HttpResponse('sta["e"]end')
    else:
        return render(request, 'login/login.html')

def action(request):
    swift = int(request.POST.get('swift'))
    if swift == 1:  # check is user is login
        if request.session['login_user'] != "":
            login_user = request.session['login_user']
            if login_user.get('user') == "student":
                return HttpResponse('sta["stu"]end')  # redirect to student
            elif login_user.get('user') == "teacher":
                return HttpResponse('sta["tea"]end')
            elif login_user.get('user') == "admin":
                return HttpResponse('sta["adm"]end')
            elif login_user.get('user') == "principal":
                return HttpResponse('sta["pri"]end')
            else:
                return HttpResponse('sta["e"]end')
        else:
            return HttpResponse('sta["n"]end')  # do nothing
    elif swift == 2:
        request.session['login_user'] = ""
        return HttpResponse('sta["s"]end')


def changepassword(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        oldPassword = request.POST.get('old')
        newPassword = request.POST.get('n')

        USER = login_user.get('user')
        USER_ID = login_user.get('id')

        if Login.objects.filter(type=USER, u_id=USER_ID, password=oldPassword).count() > 0:
            login = Login.objects.get(type=USER, u_id=USER_ID)
            login.password = newPassword
            login.save()

            if USER == "student":
                time_now = str(datetime.datetime.now().strftime("%I:%M %p"))
                date_today = datetime.date.today().strftime("%b %d %Y")
                createnotification({'user': 'System', 'id': 1}, [{'stu_id': USER_ID}], "You changed your password at " + date_today + ", " + time_now)

            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["wp"]end') #wrong password
    else:
        return HttpResponse('sta["l"]end')


def changestudentpassword(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            stu = request.POST.get('stu')
            password = request.POST.get('n')
            login = Login.objects.get(u_id=stu, type="student")
            login.password = password
            login.save()  #TODO: create login key = > change login key while changing password

            time_now = str(datetime.datetime.now().strftime("%I:%M %p"))
            date_today = datetime.date.today().strftime("%b %d %Y")
            createnotification({'user': 'System', 'id': 1}, [{'stu_id': stu}],"Admin changed your password at " + date_today + ", " + time_now)

            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('uau')
    else:
        return HttpResponse('sta["l"]end')


    # request.set_cookie(name, value)
# request.session["uid"] = uid

# rand = random.randint(11111, 99999)
#         print(rand)


def islogin(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        id = login_user.get('id')
        user = login_user.get('user')
        key = login_user.get('key')
        if Login.objects.filter(u_id=id, type=user, login_key=key).count() > 0:
            return True
        else:
            del request.session['login_user']
            return False
    else:
        return False



def changeforgotpassword(request):
    swift = int(request.POST.get('s'))
    if swift == 1:
        nmbr = request.POST.get('num')
        if Login.objects.filter(username=nmbr).count() > 0:
            rand = random.randint(111111, 999999)
            request.session['otp'] = {'id': Login.objects.get(username=nmbr).login_id, 'otp': rand}

            msg = "Dear user,\n\nOTP to change password of Student Portal is: " + str(rand)

            import requests

            url = "https://www.fast2sms.com/dev/bulkV2"

            payload = "sender_id=StudentPortal&message=" + msg + "&language=english&route=q&numbers=" + str(nmbr)
            headers = {
                'authorization': "B6KmmvWor7quLPMzRGdRaQaJUsBN7pbA1gEqD7P3XMi4c9ujx5LWaKXM8ssa",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }

            response = requests.request("POST", url, data=payload, headers=headers)

            print(response.text)

            return HttpResponse('sta["s", "' + str(rand) + '"]end')
        else:
            return HttpResponse('sta["nnf"]end')  # number not found

    elif swift == 2:
        otp = int(request.POST.get('otp'))
        if otp == int(request.session['otp'].get('otp')):
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["io"]end') # incorrect otp

    elif swift == 3:
        password = request.POST.get('p')
        # rand = random.randint(11111, 99999)
        login = Login.objects.get(login_id=request.session['otp'].get('id'))
        login_key = str(login.u_id) + login.type[0:2] + str(random.randint(11111, 99999))
        request.session['login_user'] = {'user': login.type, 'id': login.u_id, 'key': login_key}
        print(request.session['login_user'])
        login.password = password
        login.login_key = login_key
        login.save()
        del request.session['otp']

        # request.session['login_user'] = {'user'}

        return HttpResponse('sta["s"]end')

    # return HttpResponse('hey')


# abhila@donbosco