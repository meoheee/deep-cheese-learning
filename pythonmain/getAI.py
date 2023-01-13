import flask

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.28'
port = 8000

s.connect((host, port))

# 서버로부터 수신
rbuff = s.recv(1024)  # 메시지 수신
received = str(rbuff, encoding='utf-8')
print('수신 : {0}'.format(received))






s.close()
