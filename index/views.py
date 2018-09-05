from django.shortcuts import render
from index.models import *
from django.http import HttpResponse


def index(request):
    context = {
        'certificates': Certificates.objects.filter(visible=True)
    }
    return render(request, 'index.html', context)


def certificate(request, certificate_id):
    context = {
        'certificate': Certificates.objects.get(visible=True, id=certificate_id)
    }
    return render(request, 'certificate.html', context)


def test(request):
    return render(request, 'test.html')
