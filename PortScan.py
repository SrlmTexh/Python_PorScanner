import socket

TRGT = input('IP: ')
PORTS_RANGE = input('Port range [ex. 5-200] ')

first_port = int(PORTS_RANGE.split('-')[0])
last_port = int(PORTS_RANGE.split('-')[1])

print('IP: ', TRGT, '\n Scanning ports ...')

for port in range(first_port, last_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((TRGT, port))
    if (status == 0):
        print('Open Ports: \n  Port -> ', port)
    s.close()

