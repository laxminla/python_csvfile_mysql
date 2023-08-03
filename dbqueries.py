import pandas as pd
from database_class import Database
import logging
from utility import *

logging.basicConfig(filename='database.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


try:
    data = pd.read_csv(departmentscsv)
    df2 = pd.DataFrame(data)

    #initializing an object named db from the Database class
    db = Database()
    #creates a server connection using the create server connection method of the db object
    conn = db.create_server_connection(ipaddress,username,password,dbname)

    get_info = """SELECT * FROM {};""".format(tableName2)
    #Query performs a left join between the employees table and the departments table based on dept_id
    get_info = """SELECT * FROM employees LEFT JOIN departments ON employees.dept_id = departments.dept_id;"""
    #filter the result second highest salary from each department by using innermost subquery and outer subquery
    get_info = """SELECT employee_id, full_name, salary, dept_id from employees WHERE salary = (select max(salary) from employees WHERE salary < (select max(salary) from employees));"""

    query = """
    SELECT employees.employee_id, employees.full_name, employees.salary, departments.dept_id, departments.dept_name FROM employees JOIN departments on employees.dept_id = departments.dept_id WHERE salary = (select max(salary) from employees WHERE salary < (select max(salary) from employees));
    """

    empSalQuery3 = """
    SELECT salary, dept_id, employee_id, full_name FROM employees
    WHERE salary = (select max(salary) from employees WHERE salary < (select max(salary) from employees)) group by employee_id;
    
    """

    empSalQuery3 = """
    SELECT * FROM employees
    WHERE salary = (select max(salary) from employees WHERE salary < (select max(salary) from employees));
    """
# # common table expression CTE defined as res. CTE calculates the ranking (x_rank) of employees within each department based on thier salary.
# #rank() function assigns a rank to each employee within thier department
# # where clause filters the second highest salary in each dept based on x_rank = 2
#     empSalQuery3 = """
#     with res as (select salary, dept_id, employee_id, full_name, rank() over (partition by dept_id order by salary desc) x_rank from employees) select res.employee_id, res.full_name, res.dept_id, res.salary from res where x_rank = 2;
#     """

    #need panda to read sql query and save into variables emps

    emps = pd.read_sql_query(con=connection, sql=empSalQuery3)
    print("printing empList")
    print(emps.to_string())

    df2 = df2.merge(emps, on="dept_id")
    print(df2)



except Exception as e:
    logging.error("Exception occurred", exc_info=True)
