# coding=utf-8
# /jiaqiang/Envs/Learn_env/python3

#request --> urlib -->socket 所有的web都是基于socket的
import socket
from urllib.parse import urlparse

def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path

    if path == '':
        path='/'

    #建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send('GET{} HTTP/1.1\r\nHost:{}\r\n\r\nConnection:close'.format(path,host).encode('utf8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    print(data)
    client.close()

get_url('http://www.baidu.com')