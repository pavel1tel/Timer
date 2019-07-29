from django.shortcuts import render, redirect
from .models import Activity
import datetime
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    if request.user.is_authenticated != True:
        return redirect('/accounts/login')

    minute_time = 1
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    try:
        activ = 0
        active = Activity.objects.all().filter(date__range=(today_min, today_max), user=request.user, type='1')
        for a in active:
            activ += a.time
    except ObjectDoesNotExist:
        activ = 0
    return render(request, 'index.html', {
        'time_text': str(minute_time) + ":00",
        'time_num': minute_time,
        'activ': activ,
        'user': request.user
    })
