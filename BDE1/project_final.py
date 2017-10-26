#-*- coding: utf-8 -*-
import pymysql.cursors
import config
import sys

connection = pymysql.connect(
host = config.host,
user = config.user,
password = config.password,
db = config.db,
charset = 'utf8',
cursorclass = pymysql.cursors.DictCursor,
autocommit = True)


print("================================================\n\
1.  print all buildings \n\
2.  print all performances \n\
3.  print all audiences \n\
4.  insert a new building \n\
5.  remove a building \n\
6.  insert a new performance \n\
7.  remove a performance \n\
8.  insert a new audience \n\
9.  remove a audience \n\
10. assign a performance to a building \n\
11. book a performances \n\
12. print all performances wich assigned at a building \n\
13. print all audiences who booked for a performance \n\
14. print ticket booking status of a performance \n\
15. exit \n\
================================================")


'''
def button(number):
    for i in range(1, 16):
        if number == i:
            this_module = sys.modules[__name__]
            getattr(this_module, "f"+str(i))()
'''

def button(connection):
    while True:
        number = eval(input("Select your action: "))
        cursor=connection.cursor()

        if number == 1:
            sql = "select * from buildings;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print('%-10s%-25s%-10s%-10s%-10s'%('bldg_id','name','locaction','capacity','assigned'))
            for row in result:
                 print('%-10s%-25s%-10s%-10s%-10s'%(row['bldg_id'],row['name'],row['location'],row['capacity'],row['assigned']))

        if number == 2:
            sql = "select * from performances;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print('%-10s%-25s%-10s%-10s%-10s%-10s'%('Perf_id','name','type','price','booked','bldg_id'))
            for row in result:
                 print('%-10s%-25s%-10s%-10s%-10s%-10s'%(row['perform_id'],row['name'],row['type'],row['price'],row['booked'],row['bldg_id']))


        if number == 3:
            sql = "select * from audiences;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("ID\tName\t\tGender\tAge")
            for row in result:
                print(row["aud_id"], "\t" + row["name"]+ "\t" + row["gender"]+ "\t", row["age"])

        if number == 4:
            bldg_name = input("Building name: ")
            bldg_loc = input("Building location: ")
            bldg_capacity = eval(input("Building capacity: "))
            sql = "insert into buildings(name, location, capacity) \
            values('%s', '%s', %d)"%(bldg_name,bldg_loc,bldg_capacity)
            cursor.execute(sql)
            connection.commit()

        if number == 5:
            bldg_name = input("Building name: ")
            sql = "delete from buildings where name = '%s'"%(bldg_name)
            cursor.execute(sql)
            connection.commit()


        if number == 6:
            perf_name = input("Performance name: ")
            perf_type= input("Performance type: ")
            perf_price = int(input("Performance price: "))
            sql = "insert into performances(name, type, price) \
            values('%s', '%s', %d)"%(perf_name, perf_type, perf_price)
            cursor.execute(sql)
            connection.commit()

        if number == 7:
            perf_name = input("Performance name: ")
            sql = "delete from performances where name = '%s'"%(perf_name)
            cursor.execute(sql)
            connection.commit()

        if number == 8:
            aud_name = input("Audience name: ")
            aud_gender = input("Audience gender: ")
            aud_age = int(input("Audience age: "))
            sql = "insert into audiences(name, gender, age) \
            values('%s', '%s', %d)"%(aud_name, aud_gender, aud_age)
            cursor.execute(sql)
            connection.commit()

        if number == 9:
            aud_name = input("Audience name: ")
            sql = "delete from audiences where name = '%s'"%(aud_name)
            cursor.execute(sql)
            connection.commit()

        if number == 10:
            bldg_id = int(input("Building id: "))
            perf_id = int(input("Performance id: "))
            sql = "select perform_id from performances where perform_id = %d \
            and bldg_id is null;"%(perf_id)
            cursor.execute(sql)
            result = cursor.fetchall()
            if result == ():
                print("This performance is already placed;")
                return None

            else:
                with connection.cursor() as cursor:
                    sql = "update performances set bldg_id = %d \
                    where perform_id = %d;"%(bldg_id, perf_id)
                    cursor.execute(sql)
                    sql = "select count(*) from performances where bldg_id = \
                    %d"



                    sql = "update buildings set assigned = assigned + 1 \
                    where bldg_id = %d"%(bldg_id)
                    cursor.execute(sql)
                    connection.commit()


        if number == 11:
            sql = "select * from performances;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("You have these kinds of choices!!!")
            print('%-10s%-25s%-10s%-10s%-10s%-10s'%('Perf_id','name','type','price','booked','bldg_id'))
            for row in result:
                 print('%-10s%-25s%-10s%-10s%-10s%-10s'%(row['perform_id'],row['name'],row['type'],row['price'],row['booked'],row['bldg_id']))

            aud_id = int(input("Audience id: "))
            perf_id = int(input("Performance id: "))

            sql = "select bldg_id from performances where perform_id = %d"%(perf_id)
            cursor.execute(sql)
            bldg = cursor.fetchone()
            if bldg['bldg_id'] == None:
                return print("The performance is not assigned to any building.")


            sql = "select capacity from buildings join performances \
            using(bldg_id) where perform_id = %d"%(perf_id)
            cursor.execute(sql)
            seat_limit = cursor.fetchall()[0]['capacity']
            seat_num = list(map(int,input('Seat number(s): ').split(',')))



            for seat in seat_num:
                if not (1<= seat <= seat_limit):
                    return print("The seat is out of range")

                sql = "select * from reservation where \
                aud_id = %d and perform_id = %d and seat_num = %d"%(aud_id, perf_id, seat)
                cursor.execute(sql)
                result = cursor.fetchall()
                if result != ():
                    return print("The seat is alredy reserved")

                else:
                    sql = "insert into reservation values(%d, %d, %d);"%(aud_id,perf_id,seat)
                    cursor.execute(sql)
                    sql = "update performances set booked = booked+1 where perform_id = %d"%(perf_id)
                    cursor.execute(sql)
                    sql = 'update audiences set perform_id = %d where \
                    aud_id = %d and perform_id is null'%(perf_id, aud_id)
                    cursor.execute(sql)

            sql = 'select count(seat_num) from reservation where aud_id\
            = %d'%(aud_id)
            cursor.execute(sql)
            seat_nums = cursor.fetchall()[0]["count(seat_num)"]
            sql = 'select price from performances where perform_id\
            = %d'%(perf_id)
            cursor.execute(sql)
            seat_price = cursor.fetchall()[0]["price"]
            print(seat_nums * seat_price)


        if number == 12:
            bldg_id = int(input("Building Id: "))
            sql = 'select * from buildings where bldg_id = %d'%(bldg_id)
            cursor.execute(sql)
            result = cursor.fetchone()
            if not result:
                return print("The building does not exist.")

            sql = "select perform_id, performances.name, type, price, booked\
            from buildings join performances using(bldg_id) where bldg_id =%d;"%(bldg_id)
            cursor.execute(sql)
            result = cursor.fetchall()
            print('%-20s%-30s%-10s%-10s%-10s'%('perform_id','name','type','price','booked'))
            for row in result:
                 print('%-20s%-30s%-10s%-10s%-10s'%(row['perform_id'],row['name'],row['type'],row['price'],row['booked']))

        if number == 13:
            perf_id = int(input("Performance Id: "))
            sql = "select * from performances where perform_id = %d"%(perf_id)

            cursor.execute(sql)
            result = cursor.fetchall()
            if not result:
                return print("The performances does not exist.")

            sql = "select distinct audiences.aud_id, name, gender, age, seat_num\
            from reservation join audiences using(perform_id) where perform_id =%d"%(perf_id)
            cursor.execute(sql)
            result = cursor.fetchall()
            print('%-10s%-25s%-10s%-10s'%('ID','name','gender','age'))
            for row in result:
                 print('%-10s%-25s%-10s%-10s'%(row['aud_id'],row['name'],row['gender'],row['age']))

        if number == 14:
            perf_id=int(input('Performance ID: '))
            sql = "select capacity from buildings join performances using(bldg_id)\
            where perform_id = %d"%(perf_id)
            cursor.execute(sql)
            p_capacity=cursor.fetchall()[0]['capacity']
            print('%-10s%-10s'%('seat_num','aud_id'))
            sql = "select seat_num,aud_id from reservation where perform_id = %d"%(perf_id)
            cursor.execute(sql)
            seat_aud=cursor.fetchall()
            reserved_seat=[i['seat_num'] for i in seat_aud]
            for seat_num in range(1,p_capacity+1):
                for row in seat_aud:
                    cursor=connection.cursor()
                    if seat_num in reserved_seat:
                        print('%-10s%-10s'%(seat_num, row['aud_id']))
                        break
                    else:
                        print(seat_num, "")
                        break


        if number == 15:
            print("Good bye!;")
            connection.close()
            break


button(connection)
