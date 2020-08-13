my_indexes = [0, 1, 2, 3, 4]
my_list = [3,7,11,13,17]
for index in my_indexes:
	print(my_list[index])
###########################################
my_indexes = [0, 1, 2, 3, 4, 5]
my_list = [3, 9, 14, 8, 20, 6]
my_list1 = [9, 8, 7, 6, 5, 4]
for index in my_indexes:
		print (f"{my_list[index],my_list1[index]}")
###########################################
my_string_1 =('0123456789')
my_string_2 = my_string_1
my_string =[]
for symb_1 in my_string_1:
	for symb_2 in my_string_2:
		my_string.append(int(symb_1 + symb_2))
print(my_string)

