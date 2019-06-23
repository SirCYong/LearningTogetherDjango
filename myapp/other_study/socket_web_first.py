# -*- coding: utf-8 -*-
# auth: cy
# create
# update
import socket
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = "hello world! <h1>first socket</h1>"
response_params = [
    'HTTP/1.0 200 ok',
    'Date: Sun, 17 sur 2019 01:02:01 GMT',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body,
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    request = b''
    while EOL1 not in request and EOL2 not in request:
        request += conn.reve(1024)
    print(request)
    conn.send(response.encode())
    conn.close()

def main():
    # socket.AF_INET  # 用于服务器与服务器之间的通信
    # socket.SOCK_STREAM  # 用于基于TCP 的流式 socket 通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可服用 保证我们每次按 ctrl + c 可 快速重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)  # 设置 backlog-socket 连接最大排队数量
    print('http://127.0.0.1:8000')
    try:
        while True:
            conn, address = serversocket.accept()
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()