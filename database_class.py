
import mysql.connector   #to connect mysql
from mysql.connector import Error
class Database:
#Function to create server connection
    def create_server_connection(self, host_name, user_name, user_password, db_name):
        conn = None
        print("The database name is ", db_name)

        try:
            if db_name == "NONE":
                conn = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    password=user_password
                )
                print("Connection set to NONE")

            else:
                conn = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    password=user_password,
                    database=db_name
                )
                print("MySQL Database is connected")

        except Error as err:
            print(f"Error: '{err}'")
        return conn


    def create_database(self, conn, query):
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            print("Database created ....")
        except Error as err:
            print(f"Error: '{err}'")

# Function to execute query
    def execute_query(self, conn, query):
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            #the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
            print("Queries saved....")
        except Error as err:
            print(f"Error: '{err}'")

#Function to read query
    def read_query(self, conn, query):
        cursor = conn.cursor(buffered=True)

        try:
            cursor.execute(query)
            records = cursor.fetchall()
            conn.commit()
            print("You're connected to database:newhcldb ")
            return records

        except Error as err:
            print(f"Error: '{err}'")








