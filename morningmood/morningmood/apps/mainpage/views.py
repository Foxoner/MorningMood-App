from django.shortcuts import render

from .models import Information
import runpy
import datetime


def index(request):
    date_time = datetime.datetime.today()
    data = Information.objects.latest('cur_date')
    return render(request, 'mainpage/base.html', {'data': data, 'date_time': date_time})


def start_script(request):
    date_time = datetime.datetime.today()
    data = Information.objects.latest('cur_date')
    runpy.run_path(path_name=r'F:\Developing\PortfolioUsefulThings\morningmood\morningmood\data.py')
    return render(request, 'mainpage/start.html', {'data': data, 'date_time': date_time})
