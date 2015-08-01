#!/usr/bin/python
# class and functions for camera object
import urllib2
import requests
from bs4 import BeautifulSoup
import time
import os

class camera:
	status = 0
	ip = 0
	link = 1
	power = 0
	interface = 'wlan0'
	password = 'ribcage1'
	mode = 0
	smode = 0
	spot = 0
	interval = 0
	autopoweroff = 0
	angle = 0
	pmode = 0
	vmode = 0
	recmin = 0
	recsec = 0
	volume = 0
	leds = 0
	mess = 0
	battery = 0
	vtime = 0
	rec = 0

	def getstatus(this):
		try:
			this.status = [ord(i) for i in urllib2.urlopen('http://10.5.5.9/camera/se?t='+this.password).read()]
		except urllib2.HTTPError, err:
			this.power = 0
			return
		
		this.mode = this.status[1]
		this.smode = this.status[3]
		this.spot = this.status[4]
		this.interval = this.status[5]
		this.autopoweroff = this.status[6]*60
		this.angle = this.status[7]
		this.pmode = this.status[8]
		this.vmode = this.status[9]
		this.recmin = this.status[13]
		this.recsec = this.status[14]
		this.volume = this.status[16]
		this.leds = this.status[17]
		this.mess = this.status[18]
		this.battery = this.status[19]
		#this.vtime = (int(chr(this.status[25]))*10)+(int(chr(this.status[26])))
		this.rec = this.status[29]
		this.power = 1
		return

	def poweroff(this):
		urllib2.urlopen('http://10.5.5.9/bacpac/PW?t='+this.password+'&p=%00')

	def poweron(this):
		urllib2.urlopen('http://10.5.5.9/bacpac/PW?t='+this.password+'&p=%01')
		print "waiting for power on..."
		time.sleep(5)
	
	def printstatus(this):
		if this.power == 0:
			print 'Power: '+str(this.power)
			print 'Turn power on for full status'
			return

		print 'IP Address: '+this.ip
		print 'Interface: '+this.interface
		print 'Mode: '+str(this.mode)
		print 'Start Mode: '+str(this.smode)
		print 'Spot meter: '+str(this.spot)
		print 'Auto-Off: '+str(this.autopoweroff)
		print 'Power: '+str(this.power)
		if this.rec == 1:
			print 'Recording for: '+str(this.recmin)+':'+str(this.recsec)
		print 'Battery: '+str(this.battery)+'%'
		return

	def record(this):
		url = 'http://10.5.5.9/bacpac/SH?t='+this.password+'&p=%0'

		if this.rec == 0:
		# turn on recording
			url = url+'1'
	
		else:
		#turn off recording
			url = url+'0'
		urllib2.urlopen(url)
		return

	def vidlist(this):
		# List videos on camera
		url = 'http://10.5.5.9:8080/videos/DCIM/'
		links = []
		r = requests.get(url)
		soup = BeautifulSoup(r.text)
		for folder in soup.find_all('a'):
			directory =  folder.get('href')
			if directory[-6:] == 'GOPRO/':
				print directory
				location = url + directory
				r2 = requests.get(location)
				soup2 = BeautifulSoup(r2.text)
				for link in soup2.find_all('a'):
					link = link.get('href')
					if link[-4:] == '.MP4':
						print link
						links.append(directory+link)
		return links

	def dlvidlist(this):
		dldir = os.getcwd()+'/unprocessed/' #download dir
		files = []
		for (dirpath, dirnames, filenames) in os.walk(dldir):
			files.extend(filenames)
			break
		return files

	def downloadnew(this):
		url = 'http://10.5.5.9:8080/videos/DCIM/'
		#find new files on camera
		#camfiles = this.vidlist()
		#pcfiles = this.dlvidlist()
		hitlist = this.vidlist() #set(camfiles[0]).difference(pcfiles)
		#hitlist = set(camfiles).intersection(diff)
		togo = len(hitlist)
		done = 0
		for file in hitlist:
			print url+file
			u = urllib2.urlopen(url+file)
			f = open(os.getcwd()+'/unprocessed/'+file.split('/',1)[1], 'wb')
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			print "Downloading: %s Bytes: %s" % (file, file_size)
			file_size_dl = 0
			block_sz = 8192
			while True:
				buffer = u.read(block_sz)
				if not buffer:
					break
				file_size_dl += len(buffer)
				f.write(buffer)
				status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
				status = status + chr(8)*(len(status)+1)
				print status,
			f.close()
			done += 1
			print "%s of %s completed." % (done, togo)
	def processnew(this):
		#process new videos for slow mo
		return

	def setmode(this):
		#set resolution and recording mode
		return

	def deleteall(this):
		#delete all recordings on camera
		return

	def watchlive(this):
		return
#	def getpass(this):
#		this.password = urllib2.urlopen('http://10.5.5.9/camera/sd').read()
	
#	def setup(this,iface):
#		this.getpass()
#		this.interface = iface
		                        
