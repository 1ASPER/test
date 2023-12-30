from django.shortcuts import render
from .models import Task

def index(request):
    return render(request, template_name='index.html')

def get_data(request):

    data = {
        'task': Task.objects.all()
    }

    return render(request, 'get.html', data)



# Остальные функции в АДМИНКЕ :)

