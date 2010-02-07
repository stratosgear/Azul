# Create your views here.

from django.http import HttpResponse

def pictures_home(request):
    return HttpResponse("Pics Home")