import mysql.connector
import json
import os


def mysql_query(query):
    # Establish a connection to the database

    try: 
        connection = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database=os.environ.get("MYSQL_DB")
        )
        # print('mysql_query() : Connected to MySQL database')

        if connection.is_connected():
            print("Connected to MySQL database")

            # Excecute query
            cursor = connection.cursor()

            # Execute a query
            cursor.execute(query)
        
            output = cursor.fetchall() # Fetch results with cursor.fetchall()
            # cursor.fetchall() returns output as a list enclosing a tuple
            # print("mysql_query() : Query results => ", output)

            return output
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

        return "error"
    
    finally:
        # Close connection
        if connection.is_connected():
            cursor.close()                     # close the cursor and connection properly when you're done to avoid resource leaks.
            connection.close()
            print("MySQL connection closed")
    

class DBQuery():
    """
    - Job of class is just to interract with the MySQL DB Server.
    - Expects incoming string to be in the format "<api action>:<Country name> e.g get:Kenya, post:Zambia, put:Australia, delete:USA
    - Based on the string, 
    """
    def __init__(self,string_pattern):
        self.string_pattern = string_pattern
    
    def getData(self):
        query = "select * from Countries where CountryName = '{}'".format(self.string_pattern.split(":")[1])
        # print("DBQuery().getData() => query : ", query)

        # If needing the output to be in a string format for manipulation
        output = mysql_query(query)
        str_output = json.dumps(output)

        return str_output
    
    def putData(self):
        pass

