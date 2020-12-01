#!/usr/bin/env python

import subprocess

ports = []
ports.append(21) #ftp
ports.append(22) #ssh
ports.append(23) #telnet
ports.append(80) #http
ports.append(443) #https
ports.append(445) #smb
ports.append(1900) #upnp
ports.append(1433) #sqlserver
ports.append(3306) #mysql
ports.append(3389) #rdp
ports.append(5900) #vnc
ports.append(27017) #mongodb

for port in ports:
	print("Pentbox is listening on port %d" % port)
	proc = subprocess.Popen(["./pentbox.py", "-p", str(port)])
	#print("ProcessID: %d" % proc.pid)
