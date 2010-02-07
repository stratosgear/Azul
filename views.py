'''
Created on Feb 6, 2010

@author: stratos
'''

from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
#    return HttpResponse('Hello')
    return render_to_response('index.html', None)
