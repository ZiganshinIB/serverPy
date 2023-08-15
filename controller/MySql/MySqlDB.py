import pymysql
import pymysql.cursors
from . import config


def connection_db():
    try:
        connection = pymysql.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as ex:
        print('Connection refused...')
        print(ex)


def _create_data_(table_name: str, data: dict):
    create_data_sql = f''' 
INSERT INTO `{table_name}` ({', '.join(data)}) VALUES
({', '.join([f'{val}' if (type(val) == int or type(val) == float) else f'"{val}"' for val in data.values()])});
'''
    return create_data_sql


# TODO create_area_full(name: str) -> int area_id:
def create_area_full(name: str):
    sql_request = _create_data_(table_name='area', data={'name': name})
    connection = connection_db()
    try:
        with connection.cursor() as cursor:
            print(cursor.execute(sql_request))
            connection.commit()
    except Exception as ex:
        print("Error...")
        print(ex)
    finally:
        connection.close()
    return None


# TODO _create_area_(**kwargs) -> int area_id:
def create_area(**kwargs) -> int:
    sql_request = _create_data_(table_name='area', data={'name': kwargs['name']})
    return sql_request


# TODO _create_location_full_(cabinet: str, area_id: int)-> int location_id:
def create_location_full(cabinet: str, area_id):
    sql_request = _create_data_(table_name='location', data={'cabinet': cabinet, 'area_id': area_id})
    connection = connection_db()
    try:
        with connection.cursor() as cursor:
            print(cursor.execute(sql_request))
            print(connection.commit())
    except Exception as ex:
        print("Error...")
        print(ex)
    finally:
        connection.close()


# TODO _create_location_(**kwargs)-> int location_id:

# TODO _create_device_type_full_ (name: str) -> int device_type_id:

# TODO _create_device_full_ (name: str, device_type_id: int, location_id: int) -> int device_id:
# TODO _create_device_(**kwargs) -> int device_id:

# TODO _create_device_port_full_(port: int, device_id: int) -> int device_port_id:
# TODO _create_device_port_(**kwargs) -> int device_port_id:

# TODO _create_user_full_(name: str, arm_name: str, device_port_id: int) -> user_id:
# TODO _create_user_(**kwargs)-> int user_id:

# TODO _create_connection_full_(device_port_1_id: int, device_port_2_id: int) -> int connection_id:
# TODO _create_connection_(**kwargs) -> int connection_id:

def _get_data_and_(table_name: str, data: dict):
    get_data_sql = f''' 
SELECT * FROM `{table_name}` 
WHERE {' AND '.join([f'{name}={val}' if (type(val) == int or type(val) == float) else f'{name}="{val}"' for name, val in data.items()])};'''
    return get_data_sql


def _get_data_or_(table_name: str, data: dict):
    get_data_sql = f''' 
SELECT * FROM `{table_name}` 
WHERE {' OR '.join([f'{name}={val}' if (type(val) == int or type(val) == float) else f'{name}="{val}"' for name, val in data.items()])};'''
    return get_data_sql


def _get_data_or_list_(table_name: str, data: dict):
    get_data_sql = f''' 
SELECT * FROM `{table_name}` 
WHERE {' OR '.join([f'{name}={val}' if (type(val) == int or type(val) == float) else f'{name}="{val}"' for name, vals in data.items() for val in vals])};'''
    return get_data_sql


def _get_data_and_list_(table_name: str, data: dict):
    get_data_sql = f''' 
SELECT * FROM `{table_name}` 
WHERE '''
    get_data_sql = get_data_sql + " AND ".join(['('+' OR '.join([f'{name}={val}' if (type(val) == int or type(val) == float) else f'{name}="{val}"' for val in vals]) +')' for name, vals in data.items()])
    return get_data_sql


# TODO: _get_user_of_id__(user_id: int) -> list:
# TODO: _get_user_(**kwargs) -> list:
# TODO: _get_user_or_(**kwargs) -> list:
# TODO: _get_user_and_(**kwargs) -> list:
# TODO: _get_area_of_id__( area_id: int) -> list:
def get_area(name: str):
    """
    Возвращает совпадение по имени площадки
    :param name: name of the area
    :return: result of the SQL request
    """

    sql_request = _get_data_and_(table_name='area', data={'name': name})
    connection = connection_db()
    try:
        with connection.cursor() as cursor:
            print(cursor.execute(sql_request))
            rows = cursor.fetchall()
            print(rows)
            return rows
    except Exception as ex:
        print("Error...")
        print(ex)
    finally:
        connection.close()


def get_area_or(names):
    """
        Возвращает площадки совпавшие по именам
        :param names: Names of areas
        :return: result of the SQL request
        """
    sql_request = _get_data_or_list_(table_name='area', data={'name': names})
    connection = connection_db()
    try:
        with connection.cursor() as cursor:
            print(cursor.execute(sql_request))
            rows = cursor.fetchall()
            print(rows)
            return rows
    except Exception as ex:
        print("Error...")
        print(ex)
    finally:
        connection.close()


def _join_tables_(tables_args: dict, join_to: dict):
    """
    Возвращает запрос с INNER JOIN
    :param tables_args: {table_name : [col]}
    :param join_to: {(table, col) : (table, col)}
    :return: INNER JOIN
    """
    sql_request = '''
SELECT \n\t'''
    sql_request = sql_request + ', \n\t'.join([f'{table_name}.{col} AS "{table_name}.{col}"' for table_name in tables_args for col in tables_args[table_name]])
    sql_request = sql_request + f"\nFROM {list(tables_args.keys())[0]}\n"
    for in_join, to_join in join_to.items():
        sql_request = sql_request + f"JOIN {to_join[0]} ON {to_join[0]}.{to_join[1]} = {in_join[0]}.{in_join[1]}\n"
    return sql_request


# TODO: _get_location_of_area_(**kwargs) -> list:
def get_location_of_area(**kwargs):
    """
    Возвращает кабинеты совпавшие по именам
    :param kwargs: area_name or area_id
    :return: result of the SQL request (list of location)
    """
    sql_request = _join_tables_({'location': ['id', 'cabinet'], 'area': ['name']},
                                {('location', 'area_id'): ('area', 'id')})
    if 'area_id' in kwargs:
        sql_request = sql_request + f'''WHERE area.id = {kwargs['area_id']};'''
    elif 'area_name' in kwargs:
        sql_request = sql_request + f'''WHERE area.name = \"{kwargs['area_name']}\";'''
    else:
        sql_request = sql_request + ';'
    return sql_request


def get_location(**kwargs):
    sql_request = _join_tables_({'location': ['id', 'cabinet'], 'area': ['name']},
                                {('location', 'area_id'): ('area', 'id')})
    if 'id' in kwargs:
        sql_request = sql_request + f'''WHERE location.id = {kwargs['id']};'''
    elif 'cabinet' in kwargs:
        sql_request = sql_request + f'''WHERE location.cabinet = \"{kwargs['area_name']}\"'''
        if 'area_id' in kwargs:
            sql_request = sql_request + f''' AND area.id = {kwargs['area_id']};'''
        elif 'area_name' in kwargs:
            sql_request = sql_request + f''' AND area.name = \"{kwargs['area_name']};\"'''
    else:
        if 'area_id' in kwargs:
            sql_request = sql_request + f'''WHERE area.id = {kwargs['area_id']};'''
        elif 'area_name' in kwargs:
            sql_request = sql_request + f'''WHERE area.name = \"{kwargs['area_name']}\";'''
        else:
            sql_request = sql_request + ';'
    connection = connection_db()
    try:
        with connection.cursor() as cursor:
            print(cursor.execute(sql_request))
            rows = cursor.fetchall()
            print(rows)
            return rows
    except Exception as ex:
        print("Error...")
        print(ex)
    finally:
        connection.close()

# TODO: _get_location_(**kwargs) -> list:
# TODO: _get_location_or_(**kwargs) -> list:
# TODO: _get_ location_and_(**kwargs) -> list:

# TODO: _get_device_type_of_id_(device_type_id: int)-> list
# TODO: _get_device_type_(**kwargs)-> list

# TODO: _get_device_of_id_(device_id: int)-> list
# TODO: _get_device_(**kwargs) -> list
# TODO: _get_device_or_(**kwargs) -> list
# TODO: _get_device_and_(**kwargs) -> list

# TODO: _get_device_port_of_id_(device_port_id:int) -> list
# TODO: _get_device_port_(**kwargs) -> list
# TODO: _get_device_port_or_(**kwargs) -> list
# TODO: _get_device_port_and_(**kwargs) -> list

# TODO: _get_connection_of_id_(connection_id:int) -> list
# TODO: _get_connection_(**kwargs) -> list
# TODO: _get_connection_or_(**kwargs) -> list
# TODO: _get_connection_and_(**kwargs) -> list


# TODO: _set_ area_(area_id:int, **kwargs) -> bool
# TODO: _set_ location_(location_id: int, **kwargs) -> bool
# TODO: _set_ device_type_( device_type_id: int, **kwargs) -> bool
# TODO: _set_ device_(device_id: int, **kwargs) -> bool
# TODO: _set_ device_port_( device_port_id: int, **kwargs) ->bool
# TODO: _set_ user_(user_id: int, **kwargs) -> bool
# TODO: _set_ connection_( connection_id: int, **kwargs) -> bool
