import pymysql

def showTasks():
    conn = pymysql.connect(user='root', password='root',
                           host='localhost', database='')
    cursor=conn.cursor()
    sql="select todo from es4.tasks"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def newTask(new):
    conn = pymysql.connect(user='root', password='root',
                           host='localhost', database='')
    sql = "insert into es4.tasks(todo) values (%s)"
    cursor = conn.cursor()
    cursor.execute(sql, (new,))
    conn.commit()
    cursor.close()
    conn.close()

def removeTask(old):
    conn = pymysql.connect(user='root', password='root',
                           host='localhost', database='')
    sql = "select todo from es4.tasks where todo=%s"
    cursor = conn.cursor()
    cursor.execute(sql,(old,))
    result = cursor.fetchall()
    cursor.close()
    if len(result)>0:
        sql = "delete from es4.tasks where todo=%s"
        cursor = conn.cursor()
        cursor.execute(sql, (old,))
        conn.commit()
        cursor.close()
    conn.close()