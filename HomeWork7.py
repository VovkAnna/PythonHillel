import random
my_list=[]
while len(my_list) <= 20:
    a=random.randint(0,100)
    my_list.append(a)
print(my_list)
###########################################################
import random
triangle ={"A":(),
           "B": (),
           "C": ()}
triangle["A"] = (random.randint(-100,100),random.randint(-100,100))
triangle["B"] = (random.randint(-100,100),random.randint(-100,100))
triangle["C"] = (random.randint(-100,100),random.randint(-100,100))
print(triangle)
###########################################################
def my_print(strA):
    print("***"+strA+"***")
my_str="Juliette has a gun"
my_print(my_str)
##########################################################
def my_print(strA):
    a = len(strA)*"*"
    print(f"{a}\n{strA}\n{a}")
my_str ="Juliette has a gun"
my_print(my_str)
#########################################################
def my_print(strA):
    a = len(strA)*"*"
    print(f"{a}\n{strA}\n{a}")
my_str ="Juliette has a gun"
my_str1 = "***"+my_str+"***"
my_print(my_str1)
########################################################
