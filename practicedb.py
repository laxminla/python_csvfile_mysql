# WE NEED TO GENERATE A DEPARTMENT CSV FILE HAVING COLUMNS DEPTID,DEPTNAME (IF ALREADY NOT GENERATED).
# READ EMPLOYEE TABLE FROM MYSQL AND LOOKUP DEPTNAME FROM A CSV TO GET DEPTNAME.
# WE NEED TO SHOW SECOND HIGHEST SALARY FOR EACH DEPARTMENT WHERE OUTPUT SHOULD HAVE EMPID,
# EMPNAME,SALARY,DEPTNAME. NOTE: USE PANDA TO READ CSV AND MYSQL TABLE . USE CLASS AND OBJECT AND METHOD​



import mysql.connector
##read and print the config.ini file
import configparser
parser = configparser.ConfigParser()
parser.read('config.ini')
for sect in parser.sections():
   print('Section:', sect)
   for k,v in parser.items(sect):
      print(' {} = {}'.format(k,v))
   print()

#connect MySQL with Python
con = mysql.connector.connect(
    host="localhost", user="root", password="diwazdiniz", database="hcldb")


def check_employee(employee_id):
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    c.execute(sql, data)

    # rowcount method to find
    # number of rows with given values
    r = c.rowcount

    if r == 1:
        return True
    else:
        return False





