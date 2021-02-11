import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='csit321',
                                         user='root',
                                         password='password')

    sql_select_Query = "select * from CUSTOMER"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in CUSTOMER is: ", cursor.rowcount)

    print("\nPrinting each CUSTOMER record")
    for row in records:
        print("CustomerID = ", row[0], )
        print("FirstName = ", row[1])
        print("LastName  = ", row[2])
        print("Email  = ", row[3])
        print("DOB = ", row[4], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
