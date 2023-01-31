import pyfiglet
import socket
banner = pyfiglet.figlet_format("QrNX\nPORT SCANNER")
print(banner)
print("-------------------------------------------------------------------------")

def get_ip():
    ip_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip_s.connect(("10.255.255.255", 1))
        IP = ip_s.getsockname()[0]
    except:
        IP = "127.0.0.1" # If you are'nt connect the internet
    finally:
        ip_s.close()
    return IP

your_ip = get_ip()
for port in range(1,65535):
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sok.connect_ex((your_ip,port))
    if result == 0:
        print("Port {} is open".format(port))
    sok.close()
