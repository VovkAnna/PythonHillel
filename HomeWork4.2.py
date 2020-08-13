my_list = [13, 18, 166, 45, 163, 77, 182]
for value in my_list:
    if value > 100:
        print(value)
#################################################
my_list = [13, 18, 166, 45, 163, 77, 182]
my_results = []
for value in my_list:
    if value >100:
        my_results.append(value)
print(my_results)
################################################
my_list = [8,16]
if len(my_list)<2:
    my_list.append(0)
else:
    my_list.append(my_list[-1]+my_list[-2])
print(my_list)
#################################################
try:
    val = float(input("Введите число"))
    result = val ** -1
    print(result)
except(ZeroDivisionError):
    print("Введите число отличное от нуля")
except(ValueError):
    print("Что-то не так. Возможно вы ввели текст либо в значении использовали запятую вместо точки")


