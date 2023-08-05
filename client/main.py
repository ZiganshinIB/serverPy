import socket
import config
import pickle


HOST = (config.host, config.port)
client = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)
client.connect(HOST)
print('Connected to', HOST)
request = 'test'
request = pickle.dumps(request)
request += config.end

client.sendall(request)
msg = b''
while True:
    data = client.recv(8)
    if not len(data):
        break
    msg += data

print(msg)
print(pickle.loads(msg))



