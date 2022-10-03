from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def viewsemester(request):
    return render(request, 'semester/view')
