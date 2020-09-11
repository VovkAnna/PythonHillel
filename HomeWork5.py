val =3000
val=str(val)
my_symbol = "0"
for my_symbol in val:
    val.count(my_symbol)
print(val.count(my_symbol))
#############################################################
val = 1201200
val= str(val)[::-1]
count = 0
for symbol in val:
    if symbol=="0":
        count+=1
    else:
        break
print(count)

##############################################################
my_list_1 = [2,3,4,5,6]
my_list_2 = [7,8,9,10,11]
my_result=[]
for val in my_list_1:
    if val%2==0:
        my_result.append(val)
for val in (my_list_2):
    if val%2==1:
        my_result.append(val)
print(my_result)
##############################################################
my_list = [2,3,4,5,6]
new_list = []
for symbol in my_list[1::]:
    new_list.append(symbol)
new_list.append(my_list_1[0])
print(new_list)
##############################################################
my_list = [2,3,4,5,6]
my_list.append(my_list.pop(0))
print(my_list)
##############################################################
my_str = "14 числа 08 месяца 1982 года"
my_list=my_str.split()
new_list = []
for symbol in my_list:
    if symbol.isnumeric():
        new_list.append(int(symbol))
result = sum(new_list)
print(result)
#############################################################
my_str="AnnaVovk1"
a=len(my_str)
n=2
if a%2 ==0:
    my_list = [my_str[i:i+n] for i in range(0,a,n)]
else:
    my_list =[my_str[i:i + n] for i in range (0, (a-1), n)]+[my_str[-1] + " "]
print(my_list)
#############################################################
my_str = "Qwer ty uiopa sdf gh"
l_limit = 'r'
r_limit ='d'
i_1 = my_str.index(l_limit[0:])
i_2= my_str.find(r_limit[0:])
sub_str=my_str[((i_1)+1):(i_2)]
print(sub_str)
#############################################################
my_str = "Juliette has a gun"
l_limit = 'u'
r_limit ='a'
i_1 = my_str.find(l_limit[0:])
i_2 = my_str.rfind(r_limit[0:])
sub_str=my_str[((i_1)+1):(i_2)]
print(sub_str)
##############################################################
my_list =[4,20,6,77,19,14,8,19,82,3,9,20,13]
count = 0
for i in range(1, (len(my_list) - 1)):
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        count += 1
print(count)