'''
Created on Feb 10, 2010

@author: stratos
'''
from django.contrib import admin
from Azul.process.models import Process

class ProcessAdmin(admin.ModelAdmin):
  list_display = ('pid', 'name', 'parameters')

admin.site.register(Process, ProcessAdmin)
