import pymysql
import pymysql.cursors
import config


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
            print(connection.commit())
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

def _get_data_(table_name: str, data: dict):
    create_data_sql = f''' 
SELECT * FROM `{table_name}` 
WHERE {' AND '.join([f'{name}={val}' if (type(val) == int or type(val) == float) else f'{name}="{val}"' for name, val in data.items()])}'''
    return create_data_sql

# TODO: _get_user_of_id__(user_id: int) -> list:
# TODO: _get_user_(**kwargs) -> list:
# TODO: _get_user_or_(**kwargs) -> list:
# TODO: _get_user_and_(**kwargs) -> list:




# TODO: _get_area_of_id__( area_id: int) -> list:

# TODO: _get_area_(**kwargs) -> list:
def get_area(**kwargs):
    name = kwargs['name']
    print(name)
    t = '''
SELECT * FROM `area`
WHERE name = 'name'
'''
# TODO: _get_area_or_(**kwargs) -> list:
# TODO: _get_area_and_(**kwargs) -> list:

# TODO: _get_location_of_id_(location_id: int) -> list:
# TODO: _get_location_of_area_(area_id: int) -> list:
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
