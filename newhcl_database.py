
import pandas as pd   #to read csv into dataframe
from database_class import Database
import configparser
import logging

logging.basicConfig(filename='database.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

try:
    #loading employees csv file into panadas dataframe
    empdata = pd.read_csv('employees.csv')
    df1 = pd.DataFrame(empdata)
    print(df1.columns)
    print()

    #Join two columns and create new column in dataframe
    df1['full_name'] = df1['first_name'].str.cat(df1['last_name'],sep=' ')
    print(empdata.to_string())
    print(df1.columns)

    # loading deaprtment csv file into pandas dataframe
    deptdata = pd.read_csv('departments.csv', header=None,names=['dept_id','dept_name'])
    df2 = pd.DataFrame(deptdata)
    print('h1')
    print(df2.columns)
    print('h2')
    print(df2)


#config parser function to read config file
    def parse_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config
    #create config object
    config = parse_config()

    ipaddress = config["DatabaseConnection"]["ipaddress"]
    username = config["DatabaseConnection"]["username"]
    password = config["DatabaseConnection"]["password"]
    dbname = config["DatabaseConnection"]["dbname"]
    tableName1 = config["DatabaseConnection"]["tableName1"]
    tableName2 = config["DatabaseConnection"]["tableName2"]

    #create db object of Database class
    db = Database()
    conn = db.create_server_connection(ipaddress,username,password,"NONE")
    print(conn)

    create_database_query = "CREATE DATABASE IF NOT EXISTS {dbname}".format(dbname=dbname)
    #employee_table1 = db.create_database(conn, create_database_query)
    status = db.create_database(conn, create_database_query)
    conn = db.create_server_connection(ipaddress, username, password, dbname)


    create_joindeptemp_table_query = """
        CREATE TABLE IF NOT EXISTS {placeholder} (
        employee_id INT PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        emp_manager_name VARCHAR(40) NOT NULL,
        salary INT NOT NULL,
        age INT NOT NULL,
        date_of_joining VARCHAR(40) NOT NULL,
        date_of_birth VARCHAR(40) NOT NULL,
        dept_id INT NOT  NULL,
        full_name VARCHAR(40) NOT NULL
        );
        """.format(placeholder=tableName1)

    create_department1_table_query = """
    CREATE TABLE IF NOT EXISTS {placeholder} (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(40) NOT NULL
    );
    """.format(placeholder=tableName2)

    depInfoQuery = db.execute_query(conn, create_department1_table_query)
    empInfoQuery = db.execute_query(conn, create_joindeptemp_table_query)

    populate_table = """
    INSERT INTO {tableName1} VALUES ({employee_id},'{first_name}','{last_name}','{emp_manager_name}',{salary},{age},{date_of_joining},{date_of_birth},{dept_id},'{full_name}')
    """

    populate_table2 = """
    INSERT INTO {tableName2} VALUES ({dept_id},'{dept_name}')
    """
    #print(len(df1.index))
    #print(len(df2.index))
#iterate over the rows of dataframe df2 using iterrows method
    for index, row in df2.iterrows():

        populate_table_query2 = populate_table2.format(tableName2=tableName2, dept_id=row['dept_id'], dept_name=row['dept_name'])
        print(populate_table_query2)
        depInfoQuery = db.execute_query(conn, populate_table_query2)
    print("dept")


    for index, row in df1.iterrows():
        print(row)
        print('in df1 iterrows')
        populate_table_query = populate_table.format(tableName1=tableName1, employee_id=row['employee_id'],first_name=row['first_name'],last_name=row['last_name'],salary=row['salary'],age=row['age'],date_of_joining=str(row['date_of_joining']),emp_manager_name=row['emp_manager_name'],date_of_birth=str(row['date_of_birth']),dept_id=row['dept_id'],full_name=str(row['full_name']))
        print(populate_table_query)
        empInfoQuery = db.execute_query(conn, populate_table_query)


except Exception as e:
    print(e)








