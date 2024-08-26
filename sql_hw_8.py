import sqlite3


# db = sqlite3.connect('hw8.db')

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_country(db_file, country):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''INSERT INTO countries (title) 
                        VALUES (?)
            '''
            cursor = connection.cursor()
            cursor.execute(sql, country)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

db_name = 'hw8.db'

sql_to_create_table_country = '''
CREATE TABLE countries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL
)
'''
insert_country(db_name, 'hongKong')

my_connection = create_connection(db_name)
if my_connection is not None:
    print('Successfully connected to database')
create_table(my_connection, sql_to_create_table_country)
my_connection.close()
# create_table(db_name, sql_to_create_table_country)

