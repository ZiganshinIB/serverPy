import service

print('''
1) Создать площадку
''')
cmd = input()

request = b''
match cmd:
    case '1':
        name = input('Введите название площадки:')
        request = ['', {'name': name}]
    case _:
        print("Нет такого ")

server = service.connection()
service.send_message(server, request)
message = service.get_server(server)

print(message)



