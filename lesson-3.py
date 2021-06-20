# item 1 division
def my_func(ar1, ar2):
   if ar2 == 0:
       print("деление на ноль")
       delenie = 0
   else:
       delenie = ar1 / ar2
       return delenie

print (my_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))

# item 2 named arguments to print them pretty
def my_func(first_name, last_name, year, city, email, phone):
    print (first_name, last_name, "was born in", year,"*", "He currently lives in",city,"*","His email is", email, "and phone is", phone)

my_func(first_name="Oleg", last_name="Akilov", year="1975", city="Pittsburgh", email="oakilov1@gmail.com", phone="123456789")

# item 3 the sum of two biggest arguments
def my_func (ar1, ar2, ar3):
    arguments = [ar1, ar2, ar3]
    minimal = min(arguments)
    arguments.remove(minimal)
    print(sum(arguments))

my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите второе число: ")))

#item 4a: exponentiation by **
def my_func(arg1, arg2):
    equasion = 1 / arg1 ** abs(arg2)
    print(equasion)

my_func(int(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))

#item 4b: exponentiation by multiplication and division
def my_func(arg1, arg2):
    n = 1
    equasion_1 = arg1
    while n != abs(arg2):
        equasion_1 = equasion_1 * arg1
        n += 1
    equasion_2 = 1 / equasion_1
    print(equasion_2)

my_func(int(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))

# item 5 a line of numbers with a space
i = str()
z = 0
while 1:
    while i != "S":
        i = input("Введите строку чисел или S to stop: ")
        i = i.split(" ")
        a = 0
        while a<len(i):
            try:
                i[a] = int(i[a])
            except ValueError:
                print(f"Финальная сумма: {z}")
                exit(0)
            a = a + 1
        for c in i:
            z = z + c
        print(z)

# item 6: use a special function that use capital letter
def int_func(old_word):
    new_word = old_word.title()
    print(new_word)

int_func(input("Введите слово: "))


# item 7: could be done instead of #6
def my_func(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input("Введите строку: ").split()
res = []
for word in source:
    res.append(my_func(word))
print(' '.join(res))