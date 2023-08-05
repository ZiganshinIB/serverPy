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

# data = [
#     {
#         'name': "ilmir",
#         'password': '3dsafd4134',
#         'email': 'iiafdadafd'
#     },
#
# ]
# db.insert_data_in_tabel(table_name,data)

col = ['name', 'password', 'email']
datas = [
    ['Artur', '234eefewqer', 'fda543' ],
    ['Artur', 'ewqer', 'fda543' ],
    ['Ilmir', '234adfr', 'fdada543' ]
]
db.insert_datas_in_tabel(table_name, col, datas)


