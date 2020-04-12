import os
import datetime
import pymysql

#Get username from Cloud9 workspace
#(modify this variable if running on another editor)

username = os.getenv('C9_USER')

#Connect to the database
connection=pymysql.connect(host="localhost",
                          user=username,
                          password="",
                          db="Chinook")
try:
    #run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'fred']
        #prepare a string with the same number of placeholders as in list of names
        format_strings=",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings),list_of_names)
        connection.commit()
finally:
    #close the connection, regardsless whether the above was successful
    connection.close()
