import service

server = service.start()

while True:
    user, addr = server.accept()
    print(f"{user}:  {addr}")
    req = service.get_request(user)
    message = service.make_request(req[0], req[1])
    service.sen_response(user, True)



