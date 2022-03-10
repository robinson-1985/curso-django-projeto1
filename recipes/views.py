from multiprocessing import context
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/page/home.html', context={
        'name': 'Robinson Dias',
    })
