from django.shortcuts import render, get_object_or_404

from .models.demos import Demoday


def index(request):
    demodays_list = Demoday.objects.all()
    context = {'demodays_list': demodays_list}
    return render(request, 'demodays/index.html', context)


def detail_demoday(request, demoday_id):
    demoday = get_object_or_404(Demoday, pk=demoday_id)
    return render(request,
                  'demodays/detail_demoday.html',
                  {'demoday': demoday})
