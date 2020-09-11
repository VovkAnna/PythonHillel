
import json
import csv
import random
import string

def create_txt():
    len_my_str =random.randint(100,1000)
    string_symb = (string.ascii_letters+string.digits+string.punctuation+" ")
    list_rand =[]
    for i in range(len_my_str):
        list_rand.append(random.choice(string_symb))
    list_numb=[]
    for i in range (1,(len_my_str)-1):
        list_numb.append(i)
    random.shuffle(list_numb)
    list_ind=list_numb[0:9]
    for symb in (list_ind):
        list_rand[symb]="\n"
    data = ("".join(list_rand))
    return data

def create_json():
    list_x=[]
    list_y=[]
    numb_of_pairs =random.randint(5, 20)
    print(numb_of_pairs)
    for i in range (1, (numb_of_pairs)):
        list_x.append("".join(random.choices(string.ascii_lowercase, k=5)))
    print(list_x)
    for i in range (1, (numb_of_pairs)):
        rand_metod = random.randint(1, 3)
        if (rand_metod)==1:
            list_y.append(random.randint(-100,100))
        elif (rand_metod)==2:
            list_y.append(random.uniform(0,1))
        else:
            list_y.append(bool(random.randint(0,1)))
    print(list_y)
    my_dict = {key: value for key, value in zip(list_x,list_y)}
    return my_dict

def create_csv():
    m = random.randint(3, 10)
    n = random.randint(3, 10)
    print(m,n)
    list_str=[]
    for i in range(0,m):
        new_str=[]
        for j in range(n):
            new_str.append(random.randint(0, 1))
        list_str.append(new_str)
    data=(list_str)
    return data

def file_writer(filename_path):
    file_ext = filename_path.rsplit(".", 1)[-1]
    if file_ext == "txt":
        data=create_txt()
        with open(filename_path, "w") as txt_file:
            txt_file.write(data)

    elif file_ext == "json":
        my_dict = json.dumps(create_json())
        with open(filename_path, "w") as json_file:
            json_file.write(my_dict)

    elif file_ext == "csv":
        data=create_csv()
        with open(filename_path, "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)

my_path=r"C:\Users\User\PycharmProjects\ANNApythonlessons\456.csv"
file_writer(my_path)
