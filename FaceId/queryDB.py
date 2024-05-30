import mysql.connector
import datetime
from tkinter import messagebox
import time

# hàm Connection tới database
def connectdatabase():
    connection=mysql.connector.connect(
        host="localhost",
        database="test",
        user="root",
        password="123456"
    )
    return connection

# hàm insert nếu id nhập vào chưa có trong database và update nếu trong database đã có id
def insertOrUpdate(id,name):
    con=connectdatabase()
    query = "select * from people where id ="+str(id)
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    isRecorrdExit = 0
    for row in records:
        isRecorrdExit = 1
    if(isRecorrdExit == 0):
        query = "insert into people (id,name) values (%s,%s)"
        cursor.execute(query,(id,name))
    else:
        query = "update people set name = %s where id = %s" 
        cursor.execute(query,(name,id))
    con.commit()
    con.close()
    cursor.close()



# hàm sử lý checkout and checkIn
def checkInAndCheckOut(idPeople):
    check:bool
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
    con=connectdatabase()
    # truy vấn để lấy ra data     
    query = "select * from attendance where idPeople ="+str(idPeople)+ " and date(timeCheckIn) = '"+cur_date+"'";
    cursor=con.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    isRecorrdExit = 0
    # nếu câu query trên có dữ liệu thì gán isRecorrExit bằng 1 
    for row in records:
        isRecorrdExit = 1
    # check nếu isRecorrdExit == 0 thì tức là id Người dùng  trong ngày hiện tại chưa có trong database thì mình insert nó vào db
    if(isRecorrdExit == 0):
        query = "insert into attendance (idPeople,timeCheckIn,timeCheckOut) values (%s,%s,%s)"
        cursor.execute(query,(idPeople,cur_time,None))
        check = True
    # nếu isRecorrdExit = 1  thì mình sẽ tính là thời gian checkout
    else:
        query = "update attendance set timeCheckOut = %s where idPeople = %s" 
        cursor.execute(query,(cur_time,idPeople))
        check=False
    con.commit()
    con.close()
    cursor.close()
    return check


# hàm tìm kiếm People theo id
def getProfile(id):
    conn=connectdatabase()
    cmd="select * from people where id = "+str(id)
    cursor=conn.cursor()
    cursor.execute(cmd)
    records=cursor.fetchall()
    profile=None
    for row in records:
        profile=row
    conn.close()
    return profile