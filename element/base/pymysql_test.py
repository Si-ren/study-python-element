import  pymysql

ms_con = pymysql.connect(host="192.168.33.128", port=3306, user="root", password="root", charset="utf8")
cursor = ms_con.cursor()

# if __name__ == "__main__":
#
#     cursor =ms_con.cursor()
#     sql="show databases"
#     cursor.execute(sql)
#     # row = cursor.fetchall()
#     # print(row)
#     for i in cursor.fetchall():
#         print(i)
#
#     cursor.close()
#     ms_con.close()

if __name__ == '__main__':
    try:
        sql = "show databases"
        cursor.execute(sql)
        # row = cursor.fetchall()
        # print(row)
        for i in cursor.fetchall():
            print(i)
        row = cursor.execute("use test;")
        print(row)
        cursor.close()
        ms_con.close()
    except Exception as e:
        ms_con.rollback()
        print(e)