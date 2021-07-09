item 1
def sal():
   try:
       time = float(input('Введите выработку в часах '))
       salary = int(input('Какая ставка? '))
       premia = int(input('Сколко премия? '))
       raschet = time * salary + premia
       print(f'Заработная плата сотрудника  {raschet}')
   except ValueError:
       return print('Not a number')
sal()

item 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for el in my_list if my_list.index(el) > 1 if el > my_list[my_list.index(el)-1]]
print(f'Исходный список {my_list}')
print(f'Новый список {result}')

item 3
print(f'Числа кратные 20 или 21 в пределах от 20 до 240: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

item 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

item 5
from functools import reduce

def my_func(prev_el, el):
   return prev_el * el

print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

item 6
# from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)

def my_cycle_func(list, iteration):
    i = 0
    iter = cycle(list)
    while i < iteration:
        print(next(iter))
        i += 1

my_count_func(start_number = int(input("Введите целое число: ")), stop_number = int(input("Введите конечно число: ")))
my_cycle_func(list = ["как","тебя", "зовут"], iteration = int(input("Введите итератор: ")))

