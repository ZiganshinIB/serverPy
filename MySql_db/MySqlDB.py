import pymysql
import pymysql.cursors
import config

def _create_data_(table_name: str, data: dict):
    create_data_sql = f''' 
        INSERT INTO {table_name} ({', '.join(data)}) VALUES
        ({', '.join([f'{val}' if (type(val) == int or type(val) == float) else f'"{val}"' for val in data.values()])});
    '''
    return create_data_sql

class MySqlDB:
    def init(self):
        try:
            self.connection = pymysql.connect(
                host=config.host,
                port=config.port,
                user=config.user,
                password=config.password,
                database=config.db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('OK')
        except Exception as ex:
            print('Connection refused...')
            print(ex)

    def _create_data_(self, table_name: str, data: dict):
        create_data_sql = f''' 
            INSERT INTO {table_name} ({', '.join(data)}) VALUES
            ({', '.join([f'{val}' if (type(val) == int or type(val) == float) else f'"{val}"' for val in data.values()])});
        '''
        return create_data_sql

    # TODO _create_area_full_(name: str) -> int area_id:
    def _create_area_full_(self, name: str) -> int:
        sql_request = _create_data_(table_name='area', data={'name': name})
        print(sql_request)
        pass
    # TODO _create_area_(**kwargs) -> int area_id:

    # TODO _create_location_full_(cabinet: str, area_id: int)-> int location_id:
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


    # TODO: _get_user_of_id__(user_id: int) -> list:
    # TODO: _get_user_(**kwargs) -> list:
    # TODO: _get_user_or_(**kwargs) -> list:
    # TODO: _get_user_and_(**kwargs) -> list:

    # TODO: _get_area_of_id__( area_id: int) -> list:
    # TODO: _get_area_(**kwargs) -> list:
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

