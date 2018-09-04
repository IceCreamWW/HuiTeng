from django.shortcuts import render
from index.models import *


def index(request):
    context = {
        'certifications': Certifications.objects.filter(visible=True)
    }
    return render(request, 'index.html', context)
