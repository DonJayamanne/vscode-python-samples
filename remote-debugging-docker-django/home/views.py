from django.shortcuts import render
from django.template import loader


def index(request):
    context = {
        'value_from_server':'one', 
        'another_value_from_server':'two'
    }
    return render(request, 'index.html', context)
