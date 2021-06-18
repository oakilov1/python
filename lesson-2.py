# item 1: the type of elements of a list
lst = [2, 'text', 456, 45.3, None, 0.3]
i = 0
b = len(lst)
while i < b:
    print(type(lst[i]))
    i += 1

# item 2: the exchange of the elements' places
lst = []
ele = str
print ("Введите строку элементов. Напишите STOP когда закончите")
while ele != "STOP":
    ele = input()
    if ele == "STOP":
        break
    lst.append(ele)
print(lst)

if len(lst) % 2 != 0:  # мне кажется этот цикл можно написать как-то покороче, но как?
    last = lst[len(lst)-1]
    lst.pop(len(lst)-1)
    j = 0
    for i in range(int(len(lst) / 2)):
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        j += 2
    lst.append(last)
else:
    j = 0
    for i in range(int(len(lst) / 2)):
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        j += 2
print(lst)

# item 3a: months via list
seasons = ["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
month = int(input("Месяц ? "))
print(seasons[month-1])

# item 3b: months via dict
seasons = {"Зима": (1, 2, 12),"Весна": (3, 4, 5),"Лето": (6, 7, 8),"Осень": (9, 10, 11)}
month = int(input("Месяц ? "))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# item 4: numbered lines
i = 1
for line in input().split(' '):
    if len(line) > 10:
            line = line[:10]
    print(i, line)
    i += 1

# item 5: rating
my_list = [7, 5, 3, 3, 2]
new_number = int(input("Введите число: "))
my_list.append(new_number)
my_list.sort()
my_list.reverse()
print(my_list)
