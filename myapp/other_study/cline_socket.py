# -*- coding: utf-8 -*-
# auth: cy
# create
# update
if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8000))
    import time
    time.sleep(2)
    sock.send(b'2')
    print(sock.recv(1024))
    sock.close()