from django.shortcuts import render


def index(request):
    context = {
        'name': 'Hello world',
    }
    return render(request,'cars/index.html', context)