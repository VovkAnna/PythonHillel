##########################################################################
value = 148
new_value = ((value)/ 2) if value<100 else (-(value))
print (new_value)
##########################################################################
value = 100
new_value = 1 if value<100 else 0
print (new_value)
##########################################################################
value = 66
new_value = True if value<100 else False
print(new_value)
##########################################################################
my_str = "aspect"
my_str=my_str.upper()
print(my_str)
##########################################################################
my_str = "ROVER"
my_str=my_str.lower()
print(my_str)
##########################################################################
my_str = "Anna"
my_str1 = (my_str + my_str) if len(my_str)<5 else (my_str)
print(my_str1)
##########################################################################
my_str = "Artem"
my_str1 = (my_str + my_str[::-1]) if len(my_str)<5 else (my_str)
print(my_str1)
##########################################################################
my_str = "Anna 148"
for symbol in my_str:
    if symbol .isalpha() or symbol.isdigit():
        print(symbol)
##########################################################################
my_str = "Anna //148"
for symbol in my_str:
    if not symbol .isalpha() and not symbol.isdigit():
        print(symbol)
##########################################################################
my_str = "An$na //148&&"
for symbol in my_str:
    if not symbol.isalpha() and not symbol.isdigit() and symbol !=" ":
                print(symbol)
##########################################################################
