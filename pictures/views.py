# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from Azul.pictures.models import Picture

def pictures_home(request):
    return render_to_response('pictures/index.html', None)


def pictures_truncate(request):
  Picture.objects.all().delete()
  return render_to_response('pictures/index.html', None)


def pictures_scan(request):
    return render_to_response('pictures/index.html', None)
