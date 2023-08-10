import socket
import config
import pickle


def connection():
    HOST = (config.host, config.port)
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    server.connect(HOST)
    return server


def send_message(server: socket.socket, message):
    request = pickle.dumps(message)
    request += config.end
    server.sendall(request)


def get_server(server: socket.socket):
    msg = b''
    while True:
        data = server.recv(config.buffer)
        msg += data
        if msg[:-4] in config.end:
            break
    return pickle.loads(msg[:-4])
