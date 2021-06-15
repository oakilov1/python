# Item 1: playing with variables
# calculation of the age of the retirement
print("how many years untill retirement?")
g1 = int(input("please enter your age: "))
g2 = input("are you a man? ")
int(g1)
if g2 == "yes" or "Yes" or "Y" or "y":
   if g1 >= 65:
       print("you have already retired")
   else: retirement_age = 65 - g1
else:
   if g1 >= 60:
       print("you have already retired")
   else: retirement_age = 60 - g1
print(retirement_age)

#Item 2: time into hours from sec
g1 = int(input("Введите время в секундах: "))
hour = int(g1 // 3600)
minute = int((g1 / 3600 - hour) * 60)
secund = int((((g1 / 3600 - hour) * 60) - int((g1 / 3600 - hour) * 60)) * 60)
print(hour, ":", minute, ":", secund)

# item 3: Number n
g1 = int(input("Введите число: "))
g2 = g1 * 11
g3 = g1 * 111
g4 = g1 + g2 + g3
print("Сумма n + nn + nnn", g4)

# item 4: the bigest number
g1 = input("Введите число: ")
lenght = len(g1)
g1 = int(g1)
r = -1
while g1 > 10:
   d = g1 % 10
   g1 //= 10
   if d > r:
       r = d
print(r)

# item 5: income and expenses
earning = int(input("Введите выручку: "))
expenses = int(input("Введите убытки: "))
if earning > expenses:
   income = earning - expenses
   print ("прибыль", income)
   profitability = income / earning
   print("рентабилтность", profitability)
   employees = int(input("Сколько сотрудников? "))
   proF_per_person = profitability / employees
   print("прибыль на одного сотрудника: ", proF_per_person)
else:
   loss = expenses - earning
   print ("убыток: ", loss)

# item 6: sportsman
a = int(input("сколько км в первый день? "))
b = int(input("Цель в км? "))
n = 0
while a < b:
    a = a + (a*10/100)
    n = n + 1
print ("потребуется ", n, "дней")
