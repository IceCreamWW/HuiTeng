from django.shortcuts import render
# Create your views here.


def index(request):
    context = {}
    context['certifications'] = 0
    return render(request, 'index.html')
