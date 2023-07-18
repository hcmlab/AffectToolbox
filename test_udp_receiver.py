import socket
_UDP_IP = '127.0.0.1'
_UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((_UDP_IP,_UDP_PORT))

while True:
    data, addr = sock.recvfrom(50000)
    print(data.decode('utf-8'))