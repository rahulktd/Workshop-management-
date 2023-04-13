from django.shortcuts import render

from service.models import WorkSchedule


def view_work_times(request):
    scheduled_works = WorkSchedule.objects.filter(worker=request.user)
    return render(request, 'WORKER_TEMPLATE/Scheduled_works.html', {'scheduled_works': scheduled_works} )