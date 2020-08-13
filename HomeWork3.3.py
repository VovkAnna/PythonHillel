################################################################
my_str = "totolink"
my_symbol = "to"
count = my_str.count(my_symbol)
if my_symbol in my_str:
    while count > 0:
        print(my_symbol)
        count -= 1

#################################################################
my_str = "totolink"
my_symbol = "to"
a = my_str.count(my_symbol)
if my_symbol in my_str:
    print(a)
#################################################################
my_str = 'Totoli nk'
my_str = my_str.lower()
my_str1=set(my_str)
print (len(my_str1))
