import MySqlDB

db = MySqlDB.MySqlDB()
db.init()

table_name = "users_test"
# columns = {
#     'name': 'varchar(32)',
#     'password': 'varchar(32)',
#     'email': 'varchar(32)'
# }
# db.create_table(table_name, columns)

data = [
    {
        'name': "ilmir",
        'password': '34134',
        'email': 'iiafd'
    }
]
db.insert_data_in_tabel(table_name,data)