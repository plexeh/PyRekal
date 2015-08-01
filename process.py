#/usr/bin/python

import os
from subprocess import *
import sys

def vidlist(path):
	dir = os.getcwd+'/'+path+'/'
	vids = [ f for f in listdir(dir) is isfile(join(dir,f)) ]
	return vids

def toprocess():
	originals = vidlist('unprocessed')
	completed = vidlist('video/slomo')
	processthis = set(orignals).difference(completed)
	return processthis

def processnew():
	videos = toprocess() #get list of videos
	dir = os.getcwd+'/unprocessed/'
	slowdir = os.getcwd+'/slowmo/'
	for video in videos:
		flags = 'mencoder '+dir+video+' -fps 12 -nosound -ovc copy $i -o '+slowdir+video
		os.system(flags)
		
