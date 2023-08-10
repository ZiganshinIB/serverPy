from .MySql import MySqlDB

sql = MySqlDB


def create_area(**kwargs):
    return sql.create_area_full(**kwargs)

