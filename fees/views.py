from django.shortcuts import render
from department.models import Department
from fees.models import Fees, FeePaid
from student.models import Student

from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.

def viewfee_all(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        # login_user = {'user': 'principal', 'id': 1}

        dep = request.GET.get('dep')
        sem = request.GET.get('sem')



        if login_user.get('user') == "student":
            dep = Student.objects.get(stu_id=login_user.get('id')).dep_id
            sem = Student.objects.get(stu_id=login_user.get('id')).current_sem

        dep_name = Department.objects.get(dep_id=dep).name

        fees = Fees.objects.filter(dep_id=dep, sem=sem).values()
        for f in fees:
            f['due_date'] = str(f['due_date'])

        # fees_names = Fees.objects.filter(dep_id=dep, sem=sem).values('fee_name')

        if login_user.get('user') == "principal":
            students = Student.objects.filter(dep_id=dep, current_sem=sem).values('stu_id', 'adm_no', 'name', 'image').order_by(
                'adm_no')
            for stu in students:
                stu_id = stu['stu_id']
                stu['paid_details'] = []
                if FeePaid.objects.filter(stu_id=stu_id).count() > 0:
                    stu['status'] = 'paid'
                    fee_paid = FeePaid.objects.filter(stu_id=stu_id).values()
                    for fp in fee_paid:
                        allFees = Fees.objects.get(fee_id=fp['fee_id'])
                        if int(allFees.dep_id) == int(dep) and int(allFees.sem) == int(sem):
                            paid_details = {
                                'name': allFees.fee_name,
                                'paid': fp['amount'],
                                'balance': float(allFees.fee_amount) - float(fp['amount']),
                                'fee_amount': allFees.fee_amount,
                                'date': fp['date']
                            }
                            stu['paid_details'].append(paid_details)
                else:
                    stu['status'] = "pending"
            # print(students)
            # print(fees)
            return render(request, 'fees/viewFee_principal.html', {'fee': fees, 'students': students, 'dep': dep_name})
        elif login_user.get('user') == "student":
            STUDENT_ID = login_user.get('id')

            stu_dep = Student.objects.get(stu_id=STUDENT_ID).dep_id
            # print(allFee)


            feeDetails = []
            for stu_sem in range(1, 7):
                allFee = Fees.objects.filter(dep_id=stu_dep, sem=stu_sem).values('fee_id', 'fee_name', 'fee_amount', 'due_date')
                for a in allFee:
                    # print(a['fee_id'])
                    if FeePaid.objects.filter(stu_id=STUDENT_ID, fee_id=a['fee_id']).count() > 0:
                        paid = FeePaid.objects.get(stu_id=STUDENT_ID, fee_id=a['fee_id'])
                        print(paid.amount)
                        a['paid_amount'] = paid.amount
                        a['paid_date'] = paid.date
                        a['balance'] = float(a['fee_amount']) - float(paid.amount)

                fe = {'sem': stu_sem, 'fee': allFee}
                feeDetails.append(fe)
            print(feeDetails)

            # for f in fees:
            #     fee_paid = FeePaid.objects.get(fee_id=f['fee_id'])
            #     f['s_paid_amount'] = fee_paid.amount
            #     f['s_paid_date'] = str(fee_paid.date)
            #     f['s_balance'] = float(f['fee_amount']) - float(fee_paid.amount)

            # print(fees)
            return render(request, 'fees/viewFee_all.html', {'stu_fee': feeDetails})
        else:
            return HttpResponse("Unauthorized user")
    else:
        return HttpResponseRedirect('/login/login')




        # def viewFees_student(request):
#     return render(request, 'fees/viewFee.html')


def addFees(request):
    if request.session['login_user'] != "":
        if request.session['login_user'] .get('user') == "admin":
            dep = Department.objects.all()
            return render(request, 'fees/addFee.html', {'dep': dep})
        else:
            return HttpResponse('Unauthorised user')
    else:
        return HttpResponseRedirect('/login/login')


def postfee(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            data = json.loads(request.POST.get('det'))
            obj = Fees()
            obj.dep_id = data.get('dep')
            obj.sem = data.get('sem')
            obj.fee_amount = data.get('amount')
            obj.fee_name = data.get('name')
            obj.due_date = "null" if data.get('due') == "" else data.get('due')
            obj.save()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["uau"]end')
    else:
        return HttpResponse('sta["l"]end')


def editFees(request):
    if request.session['login_user'] != "":
        if request.session['login_user'] .get('user') == "admin":
            if request.method == "POST":
                feeId = request.POST.get('feeId')
                amount = request.POST.get('fee')
                due = request.POST.get('due')
                # print(request.POST)

                fee = Fees.objects.get(fee_id=feeId)
                fee.fee_amount = amount
                fee.due_date = None if due == "" else due
                fee.save()
                return HttpResponse('sta["s"]end')
            else:
                dep = request.GET.get('dep')
                sem = request.GET.get('sem')
                fee = Fees.objects.filter(dep_id=dep, sem=sem).values()
                for i in fee:
                    i['dep_id'] = Department.objects.filter(dep_id=i['dep_id']).values('short_name')[0]['short_name']
                    i['due_date'] = str(i['due_date'])
                # print(fee)
                return render(request, 'fees/editFee.html', {'fee': fee})
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponseRedirect('/login/login')


def deletefee(request):
    if request.session['login_user'] != "":
        if request.session['login_user'] .get('user') == "admin":
            feeId = request.POST.get('feeId')
            Fees.objects.get(fee_id=feeId).delete()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["uau"]end')
    else:
        return HttpResponse('sta["l"]end')


def updatestudentfee(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            if request.method == "POST":

                if int(request.POST.get('swift')) == 1:
                    obj = FeePaid()
                    obj.fee_id = request.POST.get('feeId')
                    obj.stu_id = request.POST.get('stu')
                    obj.date = request.POST.get('date')
                    obj.amount = request.POST.get('amount')
                    obj.save()
                    return HttpResponse('sta["s"]end')
                elif int(request.POST.get('swift')) == 2:
                    fee_paid = FeePaid.objects.get(paid_id=request.POST.get('paidId'))
                    old_amount = float(fee_paid.amount)
                    fee_paid.amount = float(request.POST.get('amount')) + old_amount
                    fee_paid.date = request.POST.get('date')
                    fee_paid.save()
                    return HttpResponse('sta["s"]end')
            else:
                depid = request.GET.get('dep')
                sem = request.GET.get('sem')
                stuId = request.GET.get('stu')
                fee = Fees.objects.filter(dep_id=depid, sem=sem).values()
                for i in fee:
                    feePaid = FeePaid.objects.filter(stu_id=stuId, fee_id=i['fee_id'])
                    if feePaid.count() > 0:
                        i['paid'] = float(feePaid.values('amount')[0]['amount'])
                        i['paid_date'] = str(feePaid.values('date')[0]['date'])
                        i['balance'] = float(i['fee_amount']) - float(feePaid.values('amount')[0]['amount'])
                        i['paid_id'] = feePaid.values('paid_id')[0]['paid_id']
                    else:
                        i['paid'] = 0
                        i['paid_date'] = "null"
                        i['balance'] = float(i['fee_amount'])
                # print(fee)
                stu = Student.objects.filter(stu_id=stuId).values('stu_id', 'name', 'adm_no', 'image', 'dep_id', 'current_sem')[0]
                stu['dep'] = Department.objects.get(dep_id=stu ['dep_id']).short_name
                # print(stu)
                return render(request, 'fees/updateStudentFee.html', {'fee': fee, 'stu': stu})
        else:
            return HttpResponseRedirect('/login/login')
    else:
        return HttpResponseRedirect('/login/login')

