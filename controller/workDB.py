from MySql import MySqlDB

sql = MySqlDB


def create_area(**kwargs):
    return sql.create_area_full(**kwargs)


def create_location(**kwargs):
    return sql.create_location_full(**kwargs)


def get_area(**kwargs):
    return sql.get_area(name=kwargs['name'])

