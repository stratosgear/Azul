'''
Created on Feb 10, 2010

@author: stratos
'''
from django.contrib import admin
from Azul.boardgames.models import Player

class PlayerAdmin(admin.ModelAdmin):
  list_display = ('name', 'initials', 'avatar')

admin.site.register(Player, PlayerAdmin)
