from django.shortcuts import render
from .models import Appoint
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def check(request):
    return render(request, 'check.html')


def appointment(request):
    hard = 50 - Appoint.objects.filter(subject="硬件系统维修").count()
    soft = 50 - Appoint.objects.filter(subject="软件系统维修").count()
    return render(request, 'appointment.html', context={'advanced': hard, 'discrete': soft})


def tip(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        time = request.POST.get('time')
        name = request.POST.get('name')
        number = request.POST.get('number')
        if Appoint.objects.filter(subject=subject).count() >= 50:
            return HttpResponse('已有五十人预约了{}维修，请下次再预约'.format(subject))
        else:
            if Appoint.objects.filter(number=number).filter(subject=subject):
                return HttpResponse('你已经预约了{}维修,请不要重复预约，请前往查看你的预约情况'.format(subject))
            else:
                if Appoint.objects.filter(number=number).filter(time=time):
                    return HttpResponse('你已经预约了一场相同时间的维修，请不要再预约{}的维修'.format(time))
                else:
                    Appoint.objects.create(subject=subject, time=time, name=name, number=number)
                    return HttpResponse('你已经预约成功')
    else:
        return HttpResponse('Please visit us with POST')


def information(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        if Appoint.objects.filter(number=number):
            data = Appoint.objects.filter(number=number)
            return render(request, 'print.html', context={'data': data})
        else:
            return HttpResponse('你还没有预约维修')
    else:
        return HttpResponse('Please visit us with POST')
