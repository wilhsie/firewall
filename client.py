import sys, socket, struct
import makeip, maketcp

def main():
	'''
	Main.
	'''

	if len(sys.argv) < 3:
		print 'usage: {} <host> <port>'.format(sys.argv[0])
		return 1 

	s = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket.IPPROTO_RAW)

	host = sys.argv[1]
	port = int(sys.argv[2])
	data = "{\ncommand: \"AUTH\",\nuser: \"directspeed\"\n}"

	ipobj = makeip.ip(src_host, dest_host)
	iph = ipobj.pack()

	tcpobj = maketcp.tcp(1234, 80)
	tcpobj.data_length = len(data)
	tcph = tcpobj.pack(ipobj.source, ipobj.destination)

	packet = iph + tcph + data
	
	s.send(packet, (host, port))

	s.close()

	return 0

if __name__ == '__main__':
	sys.exit(main())
