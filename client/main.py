import service

while True:
    print('''
1) Создать площадку
2) Получить площадку 
3) Создать кабинет
4) получить кабинет
''')
    cmd = input()
    request = b''
    match cmd:
        case  '1':
            name = input('Введите название площадки: ')
            request = ['create_area', {'name': name}]
        case '2':
            name = input('Введите название площадки: ')
            request = ['get_area', {'name': name}]

        case '3':
            cabinet = input('Введите название кабинета: ')
            area_id = int(input("Введите id площадки"))
            request = ['create_location', {'cabinet': cabinet,
                                           'area_id': area_id}]
        case 0:
            break
        case _:
            print("Нет такого ")
    server = service.connection()
    service.send_message(server, request)
    message = service.get_server(server)
    print(message)
