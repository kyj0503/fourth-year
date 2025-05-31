import socket

HOST = 'localhost'  # 서버 주소
PORT = 50007        # 서버와 동일한 포트 사용

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = input("> ")  # 사용자 입력
    if not data:continue

    s.sendall((data + "\n").encode())  # 서버에 데이터 전송

    if data.lower() == "bye": break# "bye" 입력 시 종료
    data = s.recv(1024)  # 서버 응답 수신
    print('Received', repr(data))
s.close()
