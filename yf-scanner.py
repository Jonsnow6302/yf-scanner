#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the Target 
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 yf-scanner.py <ip>")

#Add a pretty banner
print("-" * 100)
print("*" * 100)
print("-" * 100)
print("Scanning Target: "+target)
print("Time Started: "+ str(datetime.now()))
print("-" * 100)
print("*" * 100)
print("-" * 100)


try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Could not connect to the server")
