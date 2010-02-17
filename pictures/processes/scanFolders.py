'''
Created on Feb 14, 2010

@author: stratos
'''

import sys, os, glob, re

thisFolder = os.path.dirname(__file__)
#projPath = os.path.pardir(os.path.pardir(thisFolder))
sys.path.append('/home/stratos/dev/workspaces/Azul')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.db import models
from Azul.pictures.models import Picture

imgPattern = re.compile(".(jpg|jpeg|png)", re.IGNORECASE)

def processFile(f):
  if os.path.isfile(f):
    path = os.path.abspath(f)
    if imgPattern.search(path):
      p = Picture()
      p.filename = path
      p.fingerprint = p.calculateFingerprint()
      p.save()
      print "file: " + path

def scandirs(path):
    for currentFile in glob.glob(os.path.join(path, '*')):
        if os.path.isdir(currentFile):
            #print 'got a directory: ' + currentFile
            scandirs(currentFile)
        #print "processing file: " + currentFile
        processFile(currentFile)

scandirs('/home/stratos/Pics')
