from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from events.models import Events

from datetime import datetime, date
import json

# Create your views here.


def displayevents(request):
    if request.session['login_user'] != "":
        login_user = request.session['login_user']
        user = login_user.get('user')
        if user == "admin":
            event_years = []
            result = []
            this_day = datetime.today()
            # print(this_year)
            events = Events.objects.filter(date__gt=this_day).values().order_by('date')
            for i in events:
                if i['date'].strftime("%Y") not in event_years:
                    event_years.append(i['date'].strftime("%Y"));

            for year in event_years:
                year_month = {'year': year, 'month': []}
                month = ""
                for i in Events.objects.filter(date__year=year).values('date').order_by('date'):
                    if month != i['date'].strftime("%B"):
                        month = i['date'].strftime("%B")
                        month_events = {'month': month, 'days': []}
                        month_id = i['date'].strftime("%m")
                        getEvents = Events.objects.filter(date__year=year, date__month=month_id).values().order_by(
                            'date')
                        for ev in getEvents:
                            days = {'event_id': ev['event_id'], 'day': ev['date'].strftime("%d"), 'name': ev['body'],
                                    'date': str(ev['date'])}
                            month_events['days'].append(days)

                        year_month['month'].append(month_events)
                result.append(year_month)
            # print(result)

            if user == "admin":
                return render(request, 'events/allEvents.html', {'result': result, 'user': ['admin']})
            else:
                return render(request, 'events/allEvents.html', {'result': result, 'user': []})
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponseRedirect('/login/login')



def updateevents(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            eventId = request.POST.get('id')
            event_date = request.POST.get('date')
            event_body = request.POST.get('event')
            event = Events.objects.get(event_id=eventId)
            event.date = event_date
            event.body = event_body
            event.save()
            return HttpResponse('sta["s"]end')
        else:
            return HttpResponse('sta["uau"]end')
    else:
        return HttpResponse('sta["l"]end')


def uploadevents(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            date = request.POST.get('date')
            event = request.POST.get('event')
            
            date = datetime.strptime(date, "%Y-%m-%d")
            today = datetime.now()

            delta = date - today
            if delta.days > 0:
                obj = Events()
                obj.date = date
                obj.body = event.capitalize()
                obj.save()
                return HttpResponse('sta["s"]end')
            else:
                return HttpResponse('sta["pd"]end')
        else:
            return HttpResponse('sta["uau"]end')
    else:
        return HttpResponse('sta["l"]end')

def viewevents(request):
    today = datetime.strptime('2020-01-02', '%Y-%M-%d')
    today_event = Events.objects.filter(date__exact=today).values('date', 'body').order_by('date')
    upcoming_event = Events.objects.filter(date__gt=today).values('date', 'body').order_by('date')[0]

    if len(today_event) > 0:
        for i in today_event:
            i['date'] = i['date'].strftime("%d") + " " + i['date'].strftime("%b") + ", " + i['date'].strftime("%Y")

    upcoming_event['date'] = upcoming_event['date'].strftime("%d") + " " + upcoming_event['date'].strftime("%b") + ", " + upcoming_event['date'].strftime("%Y")
    upcoming = []
    upcoming.append(upcoming_event)
    events = {
        'today': today_event,
        'upcoming': upcoming
    }

    return render(request, 'events/viewEvents.html', events )

def addevents(request):
    if request.session['login_user'] != "":
        if request.session['login_user'].get('user') == "admin":
            return render(request, 'events/addEvents.html')
        else:
            return HttpResponse("Unauthorised user")
    else:
        return HttpResponseRedirect('/login/login')


def upcomingevent():
    today = datetime.today().strftime('%Y-%m-%d')
    if Events.objects.filter(date__gt=today).count() > 0:
        event = Events.objects.filter(date__gte=today).values('date', 'body').order_by('date')
        for ev in event:
            noOfdays = (ev['date'] - date.today()).days

            if noOfdays > 7 and noOfdays < 30:
                ev['left'] = str((ev['date'] - date.today()).days//7) + ' weeks left'
            elif noOfdays >= 30:
                ev['left'] = str((ev['date'].year - date.today().year)*12+( ev['date'].month - date.today().month ) ) + ' months left'
            elif noOfdays == 0:
                ev['left'] = 'Today'
            else:
                ev['left'] = str((ev['date'] - date.today()).days) + ' days left'


            # print( (ev['date'] - date.today()).days//7 )
            # print((ev['date'] - date.today()).days)
            # print( (ev['date'].year - date.today().year)*12+( ev['date'].month - date.today().month ) )
        return event
    else:
        return []