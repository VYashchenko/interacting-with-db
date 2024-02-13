import psycopg2
from Interact import Interact
import csv
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name,
        port=5432
    )

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         '''CREATE TABLE country2(
    #         id int PRIMARY KEY,
    #         name varchar(80) NOT NULL
    #         )
    #         '''
    #     )
    #     connection.commit()
    cursor = connection.cursor()
#     with open("data.csv", 'r') as file:
#         reader = csv.reader(file)
#         next(reader)
#
#         for row in reader:
#             id, name = row
#
#             cursor.execute("INSERT INTO country2 (id, name) VALUES (%s, %s)", (id, name))
#             connection.commit()
#
#
#
#
    db = Interact("test_db2", "postgres", "Incorrect1812", "127.0.0.1", 5432, connection, cursor)
    selected_c = db.select_country("Andorra")
    print("Selected country: ", selected_c)

except Exception as _ex:
    print("[INFO] Unnable connect to the database", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection ended successfully")
