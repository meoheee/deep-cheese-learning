import socket
import cv2
import numpy as np
class client:
    def __init__(self):
        # 연결할 서버(수신단)의 ip주소와 port번호
        TCP_IP = '192.168.0.28'
        TCP_PORT = 2023

        # 송신을 위한 socket 준비
        self.sock = socket.socket()
        self.sock.connect((TCP_IP, TCP_PORT))

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def recieveimg(self):
        # String형의 이미지를 수신받아서 이미지로 변환 하고 화면에 출력
        length = self.recvall(self.sock, 16)  # 길이 16의 데이터를 먼저 수신하는 것은 여기에 이미지의 길이를 먼저 받아서 이미지를 받을 때 편리하려고 하는 것이다.
        stringData = self.recvall(self.sock, int(length))
        data = np.frombuffer(stringData, dtype='uint8')
        decimg = cv2.imdecode(data, 1)
        return decimg

    def recievedata(self):
        data = self.recvall(self.sock, 16)
        return str(data)

    def close(self):
        self.sock.close()

if __name__ == "__main__":
    clientclass = client()
    img = clientclass.recieveimg()
    imgname = clientclass.recievedata()
    print(imgname)
    data = clientclass.recievedata()
    print(data)
    cv2.imwrite(img,imgname)