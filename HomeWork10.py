
import json
import re
import string


def read_jsonfile(filename):
    with open(filename,encoding='utf-8') as json_file:
        text = json.load(json_file)
    return(text)
my_dict=r"C:\Users\User\PycharmProjects\ANNApythonlessons\data.json"
data =(read_jsonfile(my_dict))

def name_sort(some_dict):
    name=some_dict.get("name")
    names = re.findall(r'\w+$', name)
    return(names)
name_sorted =sorted(data,key =name_sort)
[print(line) for line in name_sorted]

def date_sort(some_dict):
    date=some_dict.get("years")
    dates=re.findall(r'\d+',date)
    death_numb=[int(number) for number in dates]
    death=-1*min(death_numb) if date.count('BC')==2 else max(death_numb)
    return(death)
data_sorted = sorted(data,key =date_sort)
[print(line) for line in data_sorted]

def sort_len_key(some_dict):
    strings = some_dict.get("text")
    all_words= re.sub(r'’', '', strings)
    len_string_by_words=len(re.findall(r'\w+',all_words))
    print(len_string_by_words)
    return(len_string_by_words)
len_sorted = sorted(data,key=sort_len_key)
[print(line) for line in len_sorted]

    


