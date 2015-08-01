#!/usr/bin/python

import config
import time
import subprocess
import os
#import process
import sys

def menu(cam):
	option = 0 
	print "---------------------"
	print "Rekall - text edition"
	print "---------------------"
	print "options:"
	print "1) power button"
	print "2) press shutter"
	print "3) launch browser"
	print "4) update status"
	print "5) launch live view"
	print "6) show available downloads"
	print "7) download & process videos"
	print "8) delete video on camera"
	print "9) quit"
	print "select an option between 1 and 5"
	option = input('[1-8]: ')
	print "---------------------"
	if option == 1:
		if cam.power == 1:
			cam.poweroff()
		else:
			cam.poweron()
	elif option == 2:
		cam.record()
	elif option == 3:
		#launch browser after fork()
		print "this would launch a browser if it could"
	elif option == 4:
		cam.getstatus()
		cam.printstatus()
	elif option == 5:
		#launch VLC http://10.5.5.9:8080/
		print "launch VLC"
	elif option == 6:
		print "New videos to download"
		cam.vidlist()
	elif option == 7:
		cam.downloadnew()
		#processnew()
	elif option == 8:
		print "deleting all"
		cam.deleteall()
	elif option == 9:
		sys.exit()
	else:
		print "try again..."
while True:
	menu(config.cam[0])
