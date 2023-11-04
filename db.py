from pymysql import Connect
import pymongo 
import pandas as pd
import pymysql.cursors


print("conergnected")
# Connect to the database
connection = pymysql.connect(host='db4free.net',
                             user='osamadatabase',
                             port=3306,
                             password='-J5Mvgmk_uzE*ZU',
                             database='databaseosama',
                             cursorclass=pymysql.cursors.DictCursor)

def insert_record():
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `test` (`name`, `number`) VALUES (%s, %s)"
            cursor.execute(sql, ('osama', '789'))
    connection.commit()
    # connection is not autocommit by default. So you must commit to save
    # your changes.
            

with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT * from test"
    cursor.execute(sql)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    df.to_csv("dataframe.csv")
    with open("dataframe.txt", "w") as file1:
        for i in result:
            print(i)    
            file1.write(str(i)+'\n')
        file1.close()

        #open and read the file after the appending:
    f = open("dataframe.txt", "r")
    print(f.read())

    print(df)
    print(result)