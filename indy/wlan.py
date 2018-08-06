import subprocess

def parse(data, _type = None):

	def parse_to_dict(data = data, sep = ':'):
		info_lines = (list(map(lambda x: x.strip().lower(), info.split(':'))) for info in data.split('\n') if sep in info)
		wlan_info_dict = {info[0] : info[1] for info in info_lines}
		return wlan_info_dict

	def line_generator(data = data):
		return (line.strip().lower() for line in data.split('\n'))

	return parse_to_dict if _type == 'dict' else line_generator


def runShell(*commands, timeout = None, encoding = 'utf-8', sep = ' & '):
	args = sep.join(map(lambda x: str(x), commands))
	return subprocess.Popen(args, shell = True, encoding = encoding, stdout = subprocess.PIPE).communicate(timeout = timeout)[0]
	

def checkWLAN(wlan = None, shell_encoding = 'chcp 437'):
	'''True if wlan status is active
	   arg "wlan" is name network to check
	   returns:
		 -1 - is not a valid name
		  0 - network not started
		  1 - network is started'''

	show_wlan_command = 'netsh wlan show hostednetwork'
	wlan_info_dict = parse(runShell(shell_encoding, show_wlan_command), _type = 'dict')()
	if wlan_info_dict['ssid name'] != '"{}"'.format(wlan):
		return -1
	elif wlan_info_dict['status'] == 'not started':
		return 0
	elif wlan_info_dict['status'] == 'started':
		return 1

def checkSuccess(data):
	for line in data:
		if 'administrator privilege' in line:
			return False
	return True

def initWLAN(wlan, key = '11111111', shell_encoding = 'chcp 437'):
	'''arg "wlan" is name network to init'''
	set_network = 'netsh wlan set hostednetwork mode=allow ssid="{}" key="{}" keyUsage=persistent'.format(wlan, key)
	return checkSuccess(parse(runShell(shell_encoding,  set_network))())

def startWLAN(wlan, key = "11111111", shell_encoding = 'chcp 437'):
	'''arg "wlan" is name network to start'''
	start_wlan_command = 'netsh wlan start hostednetwork'
	if checkWLAN(wlan) == -1:
		check = initWLAN(wlan,key)
		if not check:
			return check;
	return checkSuccess(parse(runShell(shell_encoding, start_wlan_command)()))
	
def stopWLAN(wlan):
	if checkWLAN(wlan) == 1:
		subprocess.Call("netsh wlan stop hostednetwork")

def getIP(mac, shell_encoding = 'chcp 437'):
	networks_info_command = "arp -a"
	info = (_line for _line in (line.split() for line in parse(runShell(shell_encoding, networks_info_command))()) if len(_line) == 3)
	for network_info in info:
		if mac == network_info[1]:
			return network_info[0]
