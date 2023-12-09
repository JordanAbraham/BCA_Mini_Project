import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Jordan",
  password="Jordan@25",
  port = "3306",
  database = "WMP"
)

my_cursor = mydb.cursor()
my_cursor.execute("create table employee(first_name varchar(255),last_name varchar(255), phone_no varchar(255), email varchar(255), Product_id int auto_increment primary key, password varchar(255))")
# my_cursor.execute("create table Products(Product_name varchar(255),Cop_name varchar(255), Country varchar(255), Import_date varchar(255),Export_date varchar(255),Manufacturing_date varchar(255),Expiry_date varchar(255), Total_price int(255), Other varchar(255),  Product_id int auto_increment primary key, location varchar(255))")