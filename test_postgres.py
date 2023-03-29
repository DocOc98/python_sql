import psycopg2
import sys

# get the connections parameters from input
print("Enter the server name: ")
server = input()
print("Enter the port: ")
port = input()
print("Enter the database name: ")
database = input()
print("Enter the username: ")
username = input()
print("Enter the password: ")
password = input()

# create the connection string
connection_string = "host=" + server + " port=" + port + " dbname=" + database + " user=" + username + " password=" + password

# try to connect to the database
try:
    connection = psycopg2.connect(connection_string)
    print("Connection successful!")
except:
    print("Connection failed!")
    sys.exit()