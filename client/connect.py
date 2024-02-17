import socket

HOST = '172.29.0.1'  # Server hostname or ip
PORT = 25565  # PORT use by server


def user_input():
    i = input('Type something.')
    return i


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a:
    a.connect((HOST, PORT))
    while True:
        uid = user_input()
        a.sendall(bytes(uid, 'utf-8'))
        data = a.recv(1024)
        print('Received', str(data, 'utf-8'))
        if data == b'exit':
            break