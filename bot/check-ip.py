from subprocess import Popen, PIPE
from requests import get
from re import match
from sys import exit

def get_current_ip():
	# DNS
	print('Retrieving IP from DNS resolver...')
	p = Popen(['nslookup localhoneypot.ddns.net | tail -2'], stdout=PIPE, shell=True)
	out = p.communicate()[0].decode().split()
	if 'Address:' in out:
		#print(out[1])
		return out[1]

	# GIT
	print('Failed.\n\nRetrieving IP from GIT...')
	r = get(url = 'https://localhoneypot.github.io')
	if r.status_code == 200:
		#print(r.content.decode())
		return r.content.decode()

	# TELEGRAM
	print('Failed.\n\nRetrieving IP from Telegram...')
	p = Popen(['python3', 'bin/telegram.py'], stdout=PIPE)
	out = p.communicate()[0].decode().strip()
	if is_valid_ip(out):
		#print(out)
		return out

	# TOR
	print('Failed.\n\nRetrieving IP from TOR Hidden Service...')
	p = Popen(['curl', '--socks5-hostname', 'localhost:9050', '-s',
		'http://c7hlckkrkihirsp6weseznijtg25icoozosau5uj3acblwo75xo7o6qd.onion:1234/index.html'], stdout=PIPE); p.wait()
	out = p.communicate()[0].decode()
	if is_valid_ip(out):
		#print(out)
		return out

	# BLOCKCHAIN	
	print('Failed.\n\nRetrieving IP from Ethereum Blockchain...')
	p = Popen(['python3', 'bin/ethereum.py'], stdout=PIPE); p.wait()
	out = p.communicate()[0].decode()
	if is_valid_ip(out):
		#print(out)
		return out

	print('Failed.\n\nTerminating...')
	exit(0)

def update_cert(ip):
	cert = ''
	with open('resources/cert.ovpn', 'r') as file:
		for l in file.readlines():
			if 'remote ' in l:
				l = 'remote %s 1194\n' % ip
			cert = cert + l
	
	with open('resources/cert.ovpn', 'w') as file:
		file.write(cert)

def is_valid_ip(str):
	return match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', str) is not None


if __name__ == '__main__':

	ip = get_current_ip()
	update_cert(ip) 