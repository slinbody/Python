#
# reference: http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname.encode('utf8')[:15])
    )[20:24])

get_ip_address('eth0')  # '192.168.0.110'
