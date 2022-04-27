from models import room,order


# room test
r1 = room.Room(1,6)
r1.set_room_status(True)
r1.set_clean_status(False)
r2=room.Room(2,4)


rooms_list=[r1,r2]
# print(f"{'-'*10}\nRooms list\n{'-'*10}")
# print(r1,r2)
# print()
# print()
# ########################


# order test

o1=order.Order(23,"Mosh Ban Hari",6,"","",True)
o2=order.Order(24,"Naor Farjun",2,"","")
o3=order.Order(25,"Mosh Ban Hari",2,"2/2/2020","7/2/2020",True)



orders_list=[o1,o2,o3]
# print(f"{'-'*10}\nOrders list\n{'-'*10}")
# print(o1,o2)

# #################
order_typy={
	"id":0,
	"name":1,
	"num_of_guests":2,
	"arrivel":3,
	"leaving":4,
	"food":5
}

def look_for_order_by_value(type,value):
	orders_filtered=[]
	for o in orders_list:
		if value == o.look_in_the_order()[type]:
			orders_filtered.append(o)
			
	return orders_filtered

data_to_search="Mosh Ban Hari"
type_to_search="name"

orders_filtered=look_for_order_by_value(order_typy[type_to_search],data_to_search)
if len(orders_filtered) == 0:
	print("\nNot found order with the data you search\ntype: %s\ndata: %s"%(type_to_search,data_to_search))
else:
	print("\nWe found a %s orders with the data you search\ntype: %s\ndata: %s"%(len(orders_filtered),type_to_search,data_to_search))
	for o in orders_filtered:
		print(o)