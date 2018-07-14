import os

def checkWLAN(wlan):
	'''True if wlan status is active
	   arg "wlan" is name network to check
	   returns:
		 -1 - is not a valid name
		  0 - network not started
		  1 - network is started'''

	file_name = "info.txt"
	os.system("CHCP 437 > nul")
	os.system("netsh wlan show hostednetwork" + " > %s" % (file_name))
	file=open(file_name,'r').readlines()
	file_name = '\\'.join(__file__.split("\\")[:-1])+"\\"+file_name
	os.remove(file_name)
	tmp = file[4].split(':')
	tmp = [i.strip() for i in tmp]
	if(tmp[1]!='"'+wlan+'"'):
		return -1

	tmp = file[-2].split(':')
	tmp = [i.strip() for i in tmp]
	if(tmp[1]=="Not started"):
		return 0

	return 1

def initWLAN(wlan, key):
	'''arg "wlan" is name network to init'''
	os.system('netsh wlan set hostednetwork mode=allow ssid="%s" key="%s" keyUsage=persistent' % (wlan, key) + "> nul")

def startWLAN(wlan, key="11111111"):
	'''arg "wlan" is name network to start'''

	if checkWLAN(wlan)==-1:
		initWLAN(wlan,key)
		os.system("netsh wlan start hostednetwork > nul")
	else:
		os.system("netsh wlan start hostednetwork > nul")

def stopWLAN(wlan):
	if checkWLAN(wlan)==0:
		os.system("netsh wlan stop hostednetwork > nul")

def getIP(mac):
	file_name = "info.txt"
	os.system("arp -a "+" > %s" % (file_name))
	file=open(file_name,'r')
	file_name = '\\'.join(__file__.split("\\")[:-1])+"\\"+file_name
	res = ""
	for i in file:
		tmp = i.split()
		if(tmp and tmp[1]==mac):
			res = tmp[0]
	file.close()
	#os.remove(file_name)
	return res
