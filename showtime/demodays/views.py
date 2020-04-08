from django.shortcuts import render, get_object_or_404

from .models import DemoDay


def index(request):
    demodays_list = DemoDay.objects.all()
    context = {'demodays_list': demodays_list}
    return render(request, 'demodays/index.html', context)


def detail_demoday(request, demoday_id):
    demoday = get_object_or_404(DemoDay, pk=demoday_id)
    return render(request,
                  'demodays/detail_demoday.html',
                  {'demoday': demoday})
