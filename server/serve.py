import socket

def start_server(HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a:
        connlist = []
        a.bind((HOST, PORT))
        while True:
            a.listen(2)
            conn, addr = a.accept()
            with conn:
                print('Connected by ', addr)
                connlist.append(addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    conn.sendall(data)