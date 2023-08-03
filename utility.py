
from config import *
config = parse_config()

ipaddress = config["DatabaseConnection"]["ipaddress"]
username = config["DatabaseConnection"]["username"]
password = config["DatabaseConnection"]["password"]
dbname = config["DatabaseConnection"]["dbname"]
tableName1 = config["DatabaseConnection"]["tableName1"]
tableName2 = config["DatabaseConnection"]["tableName2"]

employeescsv = config["filename"]["employees"]
departmentscsv = config["filename"]["departments"]