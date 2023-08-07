def add_port(port_number: int, area: str, location: str, device_type:str, device: str):
    """
    Добавить порт
    :param port_number: номер порта
    :param area: площадка
    :param location: кабинет
    :param device: устроойство
    :param device_type: тип устойства
    :return: True если все получилось иначе False
    """
    pass


def add_user(user_name: str, computer_name: str, area: str, location: str, socket: str):
    """
    Добавить пользователя
    :param user_name: ФИО
    :param computer_name: Имя компьютера
    :param area: Площадка
    :param location: кабинет
    :param socket: розетка
    :return: True если все получилось иначе False
    """
    pass


def add_device(device: str, type_device: str, area: str, location: str, ):
    """
    Добавить устройство
    :param device: Номер или название устройства
    :param type_device: Тип устройство
    :param area: Площадка
    :param location: кабинет
    :return: True если все получилось иначе False
    """
    pass


def add_area(area: str):
    """
    Добавить площадка
    :param area: Площадка
    :return: True если все получилось иначе False
    """
    pass


def add_location(location: str, area: str):
    """
    Добавить кабинет
    :param location: название кабинета
    :param area: площадка
    :return: True если все получилось иначе False
    """
    pass


def add_connections(**kwargs):
    """
    Добавить соединение
    :param kwargs:
    area -
    location_1 -
    device_type_1 -
    device_1
    port_1 -
    location_2 -
    device_type_2 -
    device_2 -
    socket -
    :return: True если все получилось иначе False
    """
    pass


def add_socket(socket: str, area: str, location: str):
    """
    Добавить розетку
    :param socket:
    :param area:
    :param location:
    :return:
    """
    pass


def get_port(**kwargs):
    """
    Для возвращение информации о портах
    :param kwargs: параметры для поиска
    area - площадка
    location - кабинет
    device - устройство
    port - номер порта
    :return: порт [number_port, device, type_device, location, area]
    """
    pass


def get_user(**kwargs):
    """
        получить Пользователя
        :param kwargs: параметры для поиска
        area - площадка
        location - кабинет
        device - устройство
        port - номер порта
        :return: [user_name, computer_name, socket, number_port]
    """
    pass


def get_device(**kwargs):
    """
    Получить устройство
    :param kwargs:
    area - площадка
    location - кабинет
    device - устройство
    :return:
    """
    pass


def get_area(**kwargs):
    """
    Получить площадку
    :param kwargs:
    area - площадка
    :return: [area]
    """
    pass


def get_location(**kwargs):
    """
    Получить кабинет
    :param kwargs:
    area - площадка
    :return: [location, area]
    """
    pass


def get_connections(**kwargs):
    """
    Получить соединение
    :param kwargs:
    area - площадка
    location - кабинет
    port - порт
    device - устройство
    device_type - тип устройство
    socket - розетка
    :return: [device_1, device_type_1, port_1, location_1, device_2, device_type_2, port_2, location_2, socket, location, area]
    """
    pass


def get_socket(**kwargs):
    """
    Получить розетку
    :param kwargs:
    area - площадка
    location - кабинет
    device - устройство
    device_type - тип устройство
    socket - розетка
    user_name - Имя пользователя
    computer_name - Имя компьютера
    :return: [socket, user_name, computer_name, location_socket, area, device, device_type, port, location_port]
    """
    pass
