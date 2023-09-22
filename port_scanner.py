#Libraries
import sys
import socket
import pyfiglet

#Banner
banner = pyfiglet.figlet_format("QrNX's Port Scanner\n")
print(banner)

ip = sys.argv[1]
open_ports = []

def create_socket(ip,port,result=1):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        
        req = sock.connect_ex((ip,port))
        
        if req == 0:
            result = req
        sock.close()
    except Exception as e:
        pass
    return result

def control_all_ports():
    for port in range(1,65535):
        sys.stdout.flush()
        connection = create_socket(ip,port)
        
        if connection == 0:
            open_ports.append(port)
            
def print_open_ports():
    if open_ports:
        print("Open Ports: {}".format(sorted(open_ports)))
    else:
        print("There is no open ports.\n")        
            
            
control_all_ports()
print_open_ports()

