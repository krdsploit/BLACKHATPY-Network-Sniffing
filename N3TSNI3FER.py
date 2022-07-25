from csv import Sniffer
import socket
import os 

t3rgt = input("Put ya Trg => ")

def func():
    if os.name == 'nT':
        socket_protocol = socket.IPPROTO_IP
    else:
            socket_protocol = socket.IPPORT_ICMP


    s3nf = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    s3nf.bind(t3rgt, 0)
    s3nf.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nT':
        s3nf.ioctl(socket.SID_RCVALL, socket.RCVALL_OFF)

    print(s3nf.recvfrom(65565))

    if os.name == 'nT':
        s3nf.ioctl(socket.SID_RCVALL, socket.RCVALL_OFF)



if __name__ == '__main__':
    func()

