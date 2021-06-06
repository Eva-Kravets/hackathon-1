from django.shortcuts import render

from .forms import *


def site(request):
    if request.method == 'POST':
        application = AddApplication(request.POST)
        if application.is_valid():
            try:
                application.save()
                return redidect('site')
            except:
                application.add_error(None, 'Ошибка добавления поста')
    else:
        application = AddApplication()

    context = {
        'application': application,
    }
    return render(request, 'app/index.html', context=context)
