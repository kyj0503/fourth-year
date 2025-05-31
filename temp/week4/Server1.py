import socket

HOST = 'localhost'  # 모든 네트워크 인터페이스에서 수락
PORT = 50007        # 사용할 포트 번호

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1: # 서버  순환
    conn, addr = s.accept() #클라이언트  연결
    print('Connected by', addr)
    while 1 : #클라이언트  순환
        data = conn.recv(1024) #클라이언트로부터  수신
        if data.lower() == "bye":  # "bye" 입력 시 종료
            print("클라이언트/서버 종료")
            conn.sendall("bye\n".encode())
            break
        try:
            result = eval(data)
            conn.sendall((str(result) + "\n").encode())

        except Exception as e:
            conn.sendall(("오류: " + str(e) + "\n").encode())
        if not data: break

    conn.close()
    break
s.close()

