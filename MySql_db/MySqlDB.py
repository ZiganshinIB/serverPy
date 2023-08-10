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
                # create_table_query = f"DROP TABLE IF EXISTS `{name}`;"
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
                # create_table_query = f"DROP TABLE IF EXISTS `{name}`;"

                insert_query = ''
                for d in datas:
                    insert_query += f"INSERT INTO `{table_name}` ("
                    insert_data = ''
                    for col in d:
                        insert_query += f"{col}, "
                        temp = d[col]
                        insert_data += f"{temp}, " if (type(temp) == int or type(temp) == float) else f"'{temp}', "
                    insert_query = insert_query[:-2] + ") VALUES(" + insert_data[:-2] + ");\n"
                print(insert_query)
                cursor.execute(insert_query)
                self.connection.commit()
        except Exception as ex:
            print("Error...")
            print(ex)
        finally:
            self.connection.close()

    def insert_datas_in_tabel(self, table_name, col: list, datas: list):
        try:
            with self.connection.cursor() as cursor:
                # create_table_query = f"DROP TABLE IF EXISTS `{name}`;"

                insert_query = ''
                insert_query += f"INSERT INTO `{table_name}` ({', '.join(col)}) VALUES\n"
                insert_datas = ''
                for col_d in datas:
                    insert_datas += '('
                    for data in col_d:
                        insert_datas += f"{data}, " if (type(data) == int or type(data) == float) else f"'{data}', "
                    insert_datas =insert_datas[:-2] +'),\n'
                insert_query = insert_query + insert_datas[:-2] + ";"
                print(insert_query)
                cursor.execute(insert_query)
                self.connection.commit()
        except Exception as ex:
            print("Error...")
            print(ex)
        finally:
            self.connection.close()

    # TODO: Дописать эту часть
    def update(self, table_name, ref: dict, filter_):
        try:
            with self.connection.cursor() as cursor:
                update_query = f"UPDATE `{table_name}` SET "
                for d in ref:
                    temp = ref[d]
                    update_query += f"{d} ="
                    update_query += f"{temp}, " if (type(temp) == int or type(temp) == float) else f"'{temp}', "
                update_query = update_query[:-2] + "WHERE " + filter_ + ";"
                print(update_query)
        except Exception as ex:
            print("Error...")
            print(ex)
        finally:
            self.connection.close()

    def get(self, table_name, columns, filter_):
        try:
            with self.connection.cursor() as cursor:
                select_query = f"SELECT ({', '.join(columns)})\n"
                select_query += f"FROM {table_name}"
                select_query += f"WHERE {filter_};"
                cursor.execute(select_query)
        except Exception as ex:
            print("Error...")
            print(ex)
        finally:
            self.connection.close()


    # TODO: _get_user_of_id_full(user_id: int)


    # TODO: _get_user_of_username_full_(user_name: str)


    # TODO: _get_user_full(data: dict{<parametr>:<value>})

    # TODO: _get_users_and_(**conditions)

    # TODO: _get_users_or_(**conditions)

    # TODO: _get_area_
