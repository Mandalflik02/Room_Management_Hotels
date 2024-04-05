import sqlite3
from models import * 
con = sqlite3.connect("room.db")
cur = con.cursor()
# cur.execute("CREATE TABLE rooms(room_number,room_capacity,room_is_catch,room_is_clean)")
# cur.execute("CREATE TABLE rooms_faults(room_number,fault)")
# cur.execute("CREATE TABLE rooms_dates(room_number,start_date,end_date)")
# res = cur.execute("DROP TABLE rooms_faults")
# res = cur.execute("DROP TABLE rooms")
# print(res.fetchall())




def create_room_fults_in_db(room):
    for f in room.get_room_faults():
        fault=[room.get_room_number(),f]
        cur.execute("INSERT INTO rooms_faults VALUES(?,?)",fault)


def get_room_faults_from_db(room_number):
    res = cur.execute("SELECT * FROM rooms_faults WHERE room_number = %s "% room_number)
    return res.fetchall()

def create_room_dates_in_db(room):
    # print(room.get_dates_catch())
    for d in room.get_dates_catch():
        date_range=[room.get_room_number(),d.get_arrival_date(),d.get_leaving_date()]
        cur.execute("INSERT INTO rooms_dates VALUES(?,?,?)",date_range)
    res = cur.execute("SELECT * FROM rooms_dates WHERE room_number = %s"%room.get_room_number())
    print("dates",res.fetchall())





rooms_list=[Room (5,8)]
# d1= Dates_Range("01/01/2025","01/02/2025",1)
# d2= Dates_Range("01/03/2025","01/04/2025",1)

for r in rooms_list:
    r.add_fault("open window1")
    r.add_fault("open window2")
    r.add_date_catch("01/01/2025","01/02/2025",1)
    r.add_date_catch("01/03/2025","01/04/2025",1)
    create_room_fults_in_db(r)
    create_room_dates_in_db(r)
    room = [(r.get_room_number(),
             r.get_room_capacity(),
             r.get_room_status(),
             r.get_clean_status(),
            )]
    
    # print(f"room{room[0][0]}",get_room_faults_from_db(room[0][0]))
    # cur.executemany("INSERT INTO rooms VALUES(?, ?, ?, ?)", room)

# res = cur.execute("SELECT * FROM rooms")
# print("rooms",res.fetchall())
# print("faults",cur.execute("SELECT * FROM rooms_faults WHERE room_number = 1").fetchall())
# print("faults",cur.execute("SELECT * FROM rooms_faults WHERE room_number = 5").fetchall())


# get room
num =1
# print("Room number: ",num)
# res = cur.execute("SELECT * FROM rooms WHERE room_number = %s"%num)
# print("rooms",res.fetchall())
# res = cur.execute("SELECT * FROM rooms_faults WHERE room_number = %s"%num)
# print("rooms",res.fetchall())
# res = cur.execute("SELECT * FROM rooms_dates WHERE room_number = %s"%num)
# print("dates",res.fetchall())