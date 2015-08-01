#!/usr/bin/python

import camera
#configure camera
#define number of cameras
cam_count = 1

cam = []

for x in range(0,cam_count):
	cam.append(camera.camera())
	#grab details from DB
#temporary
cam[0].ip = '10.5.5.9'
#cam[0].setup('wlan0')
