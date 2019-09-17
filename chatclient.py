import socket,sys,select,string
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv) < 3):
	print("ENTER: python chat-client.py hostname:port username")
	sys.exit()
in_list = sys.argv[1].split(':')
HOSTNAME = in_list[0]
PORTNUMBER = int(in_list[1])
username = sys.argv[2]
s.settimeout(8)
s.connect((HOSTNAME,PORTNUMBER))
print("connection established")
nick = 'NICK '+ username
s.send(nick)
x =''
