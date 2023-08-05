import pymysql
import pymysql.cursors
import config


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

    def create_table(self, name, column: dict):
        try:
            with self.connection.cursor() as cursor:
                #create_table_query = f"DROP TABLE IF EXISTS `{name}`;"
                create_table_query = f"CREATE TABLE `{name}`(\n\tid int AUTO_INCREMENT,\n"
                for c in column:
                    create_table_query += f"\t{c} {column[c]},\n"
                create_table_query += "\tPRIMARY KEY (id)\n);"
                print(create_table_query)
                cursor.execute(create_table_query)
                print('Table created!')

        except Exception as ex:
            print("Error...")
            print(ex)
        finally:
            self.connection.close()

    def insert_data_in_tabel(self, table_name, datas: list[dict]):
        try:
            with self.connection.cursor() as cursor:
                #create_table_query = f"DROP TABLE IF EXISTS `{name}`;"

                for d in datas:
                    insert_query = f"INSERT INTO `{table_name}` ("
                    insert_data = ''
                    for col in d:
                        insert_query += f"{col}, "
                        temp = d[col]
                        insert_data += f"{temp}, " if (type(temp) == int or type(temp) == float) else f"'{temp}', "
                    insert_query = insert_query[:-2] + ") VALUES(" + insert_data[:-2] + ");"
                print(insert_query)
                cursor.execute(insert_query)
                self.connection.connect()
        except Exception as ex:
            print("Error...")
            print(ex)
        finally:
            self.connection.close()


