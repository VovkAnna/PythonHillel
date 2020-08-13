my_list =['anna','gninrael','python','tsal','month']
new_list=[]
for index, value in enumerate(my_list):
    if index % 2:
       new_list.append(value [::-1])
    else:
        new_list.append(value)
print(new_list)
####################################################
my_list =['family','dnipro','artem','vadym']
my_s='a'
new_list=[]
for str in (my_list):
    if str[0] == my_s:
        new_list.append(str)
print(new_list)
####################################################
my_list =['family','dnipro','school','artem','vadym']
my_s='a'
new_list=[]
for str in (my_list):
    if my_s in str:
        new_list.append(str)
print(new_list)
#####################################################
my_list =['anna','dnipro',14,'vovk', 8 , 1982]
new_list=[]
for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)
#####################################################
my_str="abcabdfeem"
for symbol in my_str:
    if my_str.count(symbol) ==1:
        print(symbol)
# если хотим красиво в строчку
my_str="abcabdfeem"
my_list=[]
for symbol in my_str:
    if my_str.count(symbol) ==1:
        my_list.append(symbol)
print(" ".join(my_list))
######################################################
my_str_1="abcd"
my_str_2="zcdef"
my_list=[]
for symbol in my_str_1:
    if symbol in my_str_2 and symbol not in my_list:
        my_list.append(symbol)
for symbol in my_str_2:
    if symbol in my_str_1 and symbol not in my_list:
        my_list.append(symbol)
print(" ".join(my_list))
#######################################################
my_str_1="140882annatem"
my_str_2="090913artem"
my_list_1=[]
my_list_2=[]
for symbol in my_str_1:
    if my_str_1.count(symbol) ==1:
          my_list_1.append(symbol)
for symbol in my_str_2:
    if my_str_2.count(symbol) == 1:
          my_list_2.append(symbol)
print(" ".join(list(set(my_list_1).intersection(set(my_list_2)))))
# ####################################################
person = {"Фамилия":"Мороз",
           "Имя":"Дед",
           "Возраст":"100+",
           "Проживание":{
                "Cтрана":"Лапландия",
               "Город":"За полярным кругом",
               "Улица":"Подарочная"},
            "Работа":{
               "Наличие":"Официально трудоустроен",
               "Должность":"Волшебный персонаж"}
          }
#####################################################
cake_recept={"Составляющие":{
                        "Коржи":{
                            "Мука":"2 стакана",
                            "Молоко":"250 мл",
                            "Масло":"200 грамм",
                            "Яйцо":"4 шт"},
                        "Крем":{
                            "Сахар":"2 стакана",
                            "Масло":"100 грамм",
                            "Ваниль":"5 капель (экстракт)",
                            "Сметана":"200 грамм"},
                        "Глазурь":{
                            "Какао":"4 столовых ложки",
                            "Сахар":"4 столовых ложки",
                            "Масло":"100 грамм"}
                        }}