import socket

#创建牙膏socket
'''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建连接
s.connect(('www.sina.com.cn', 80))


s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:

    # 建立连接:
    s.connect(('127.0.0.1', 8888))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
except ConnectionRefusedError as e:
    print(e)