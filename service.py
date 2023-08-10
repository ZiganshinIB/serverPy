import pickle
import socket
import config


def start():
    HOST = (config.host, config.port)
    server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(HOST)
    server.listen()
    print('I am listening your connection ')
    return server


def get_request(client: socket.socket):
    req = b''
    while True:
        data = client.recv(config.buffer)
        req += data
        if req[-4:] == config.end:
            break
    return pickle.loads(req[:-4])


def sen_response(client, data_mes):
    res = pickle.dumps(data_mes)
    client.sendall(res)
    print("Send message")
    client.close()


def make_request(request, data):
    from controller import workDB
    match request:
        case 'create_area':
            if 'name' in data:
                message = workDB.create_area(name=data['name'])
                return message
            else:
                return False
    return None



