#a simple port scanner 
#returns a array of open ports

import socket
import sys

def usage():
	print("usage: python " + sys.argv[0] +  " <host> <start_port> <end_port>")

def isOpen(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	res = s.connect_ex((host, port))
	if res == 0:
		s.close()
		return True
	else:
		s.close()
		return False



def scanPorts(host, start, end):
	openPorts = []
	i = start
	while i<=end:
		if isOpen(host, i):
			openPorts.append(i)
		i = i + 1
	return openPorts


def Main():
	if len(sys.argv) != 4:
		usage()
		return;
	host_ip = socket.gethostbyname(sys.argv[1])
	out = scanPorts(host_ip, int(sys.argv[2]), int(sys.argv[3]))
	print(out)

if __name__ == '__main__':
	Main()

