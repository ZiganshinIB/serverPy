from MySql import MySqlDB

sql = MySqlDB


def create_area(**kwargs):
    return sql.create_area_full(**kwargs)


def create_location(**kwargs):
    return sql.create_location_full(**kwargs)

