
import pickle
import socket
import config

HOST = (config.host, config.port)
server = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(HOST)
server.listen()
print('I am listening your connection ')
d = [{'name': 'Amanda','age': 18}]


def get_request():
    print('Waiting for request')
    req = b''
    while True:
        data = user.recv(config.buffer)
        req += data
        if req[-4:] == config.end:
            break
    return pickle.loads(req)


while True:
    user, addr = server.accept()
    print('Connected -', addr)

    # -- Получение сообщения от клиента
    req = get_request()
    print(req)

    # -- Отправка сообщения от сервера
    res = pickle.dumps(d)
    user.sendall(res)

    user.close()
    print('Disconnected -', addr)

