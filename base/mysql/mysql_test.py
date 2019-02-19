import mysql.connector

mydb=mysql.connector.connect(
    host='60.205.94.252',
    user='root',
    passwd='123456',
    database='python_test'
)

mycursor=mydb.cursor()

#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


'''
#单行插入
sql="INSERT INTO sites (name, url) VALUES (%s, %s)"
val=("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql,val)
'''

'''
#多行插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val=[("baidu","www.baidu.com"),
     ("gooogle","www.google.com")]
mycursor.executemany(sql,val)
'''

'''
#查询

sql="select * from sites"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x,x[0])
'''
'''
#带条件查询
'''
sql="select * from sites where name = %s"
val=("baidu",)
mycursor.execute(sql,val)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
#mydb.commit()

#print(mycursor.rowcount,"条记录插入成功")


