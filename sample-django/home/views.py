from django.shortcuts import render
from django.template import loader


def index(request):
    context = {
        'value_from_server':'one', 
        'another_value_from_server':'two'
    }
    return render(request, 'index.html', context)

# from django.shortcuts import render
# from django.shortcuts import render_to_response
# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return render_to_response('index.html', context={'value_from_server':'one', 'another_value_from_server':'two'})
#     #return HttpResponse("Hello, world. You're at the home index.")
