class Interact:

    def __init__(self, dbname, user, password, host, port, connection, cursor):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = connection
        self.cursor = cursor



    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to PostgreSQL database successfully")
        except (Exception) as error:
            print("Error while connecting to PostgreSQL", error)


    def insert_country(self, id, name):
        try:
            insert_query = f"INSERT INTO country (id, name) VALUES ('{id}',{name}) "
            self.cursor.execute(insert_query)
            print("Inserted country succesfully")

        except (Exception) as _ex:
            print("Error occured while inserting country:", _ex)



    def select_country(self, name):
        try:
            select_query = f"SELECT * FROM country WHERE name = '{name}'"
            self.cursor.execute(select_query)
            print(self.cursor)
            row = self.cursor.fetchone()
            return row
        except(Exception) as _ex:
            print("Error while selecting country:", _ex)
            return None




    def update_country(self, name, new_id):
        try:
            select_query = f"UPDATE country SET id = {new_id} WHERE name = '{name}'"
            self.cursor.execute(update_query)
            self.connection.commit()
            print("Table country upadted successfully")

        except(Exception) as _ex:
            print("Something went wring with update", _ex)


    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from PostgreSQL database")