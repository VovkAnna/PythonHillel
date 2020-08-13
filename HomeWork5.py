# val =3000
# val=str(val)
# my_symbol = "0"
# for my_symbol in val:
#     val.count(my_symbol)
# print(val.count(my_symbol))
# #############################################################
# val = 1201200
# val= str(val)[::-1]
# count = 0
# for symbol in val:
#     if symbol=="0":
#         count+=1
#     else:
#         break
# print(count)
#
# ##############################################################
# my_list_1 = [2,3,4,5,6]
# my_list_2 = [7,8,9,10,11]
# my_result=[]
# for val in my_list_1:
#     if val%2==0:
#         my_result.append(val)
# for val in (my_list_2):
#     if val%2==1:
#         my_result.append(val)
# print(my_result)
# ##############################################################
# my_list = [2,3,4,5,6]
# new_list = []
# for symbol in my_list[1::]:
#     new_list.append(symbol)
# new_list.append(my_list_1[0])
# print(new_list)
# ##############################################################
# my_list = [2,3,4,5,6]
# my_list.append(my_list.pop(0))
# print(my_list)
# ##############################################################
# my_str = "14 числа 08 месяца 1982 года"
# my_list=my_str.split()
# new_list = []
# for symbol in my_list:
#     if symbol.isnumeric():
#         new_list.append(int(symbol))
# result = sum(new_list)
# print(result)
##############################################################
Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
Примеры: 'abcd' -> ['ab', 'cd'], 'abc' -> ['ab', 'c_']
my_str="AnnaVovk1"





