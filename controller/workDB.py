from .MySql import MySqlDB

sql = MySqlDB


def create_area(**kwargs):
    return sql.create_area_full(**kwargs)


def create_location(**kwargs):
    return sql.create_location_full(**kwargs)


def get_area(**kwargs):
        return sql.get_area(name=kwargs['name'])


def create_location_area_id(**kwargs):
    return sql.create_location_full(cabinet=kwargs['cabinet'],
                                    area_id=kwargs['area_id'])


def create_location_area_name(**kwargs):
    return "Ведутся работы"


def get_location(**kwargs):
    return sql.get_location(**kwargs)

