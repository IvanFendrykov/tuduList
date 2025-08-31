
# print("Hello World!")
# print("Hello World!")
# name = "Vanya"
# API_KEY = "cwevwdc"
# WIDTH, HEIGHT = 100, 200
# apiKey = 44

# print(type(name)) # str
# print(type(apiKey)) # int
# print(type(45.45)) # float

# print(float(5))
# print(int(5.5))

# name = input("Input your Name")
# age = int(input("Input your Age"))
# print(name)
# print(type(age), age) 

# age = 45
# print(type(age), age) 

# name = "Ivan" + "Step"
# newName = name * 5
# print(newName)

# a = 14
# b = 7
# s = 2 * (a+b)
# print("Area", s, "sm.2")
# print("Area " + str(s) + " sm.2")
# print(f"Area {s} sm.2")

# a = int(input("Input number"))
# b = int(input("Input number"))


# plus = a + b
# minus = a - b
# dell = a / b
# multy = a * b
# print(f"{plus}, {minus}, {dell}, {multy}")

# text = "Python "
# resultText = text * 3 
# print(resultText)

# name = input("Input your Name")
# age = input("Input your Age")
# print(f"Name: {name}, Age: {age}")
# resultSum = (5 + 3) * 2 ** 2
# print(resultSum)
# print("Name: " + name +  " Age: "  + str(age))

# print( True and True)
# print( True or False)
# age = int(input("Input your age"))
# if(age >= 18):
#     print("You`re Welcome!")
# else:
#     print("You too yanger")
# if(age >= 18 or age <= 22):
#     print("You`re Welcome!")
# elif(age >= 23 or age <= 65):
#     print("You too yanger")
# else:
#     print("")

# userName = input("Please input your name: ")

# if(userName == "student"):
#     password = input("Please input your password: ")
#     if(password == "1457#%78"):
#         print("Welcome!")
#     else:
#         print("Your password is incorrect")
# else:
#         print("Your Name is not found")

# 1. Пользователь вводит число n.
# Если число делится на 3 и при этом не делится на 5, вывести "Fizz".
# Если делится на 5 и при этом не делится на 3, вывести "Buzz".
# Если делится и на 3, и на 5, вывести "FizzBuzz". При проверки используем остаток деление.
# А если ни то, ни другое — вывести само число.

# userNum = int(input("Please input your number "))
# if(userNum % 3 and == 0):
#     print(f"Fizz")

# 2. Проверка высокосного года: Пользователь вводит год. Год будет высокосный если он кратно делится на 4, но при этом не делится на 100, либо если он кратно делится на 400. 

# userYear = int(input("Please input your year "))
# if(userYear % 4 == 0 and userYear % 100 != 0):
#     print(f"This year {userYear} is spesiol")
# elif(userYear % 400 == 0 ):
#     print(f"This year {userYear} is spesiol")
# else:
#     print(f"This year {userYear} is classic")

# if (userYear % 400 == 0) or (userYear % 4 == 0 and userYear % 100 != 0):
#     print(f"This year {userYear} is special")
# else:
#     print(f"This year {userYear} is classic")

# 3.  Треугольник существует ли?
# Пусть заданы три стороны a, b, c.
# Если сумма любых двух сторон строго больше третьей → треугольник существует. В противном случаи  - не существует.
# Если условие выполняется и все стороны равны → вывести "Равносторонний".
# Если только две стороны равны → "Равнобедренный".
# Иначе → "Разносторонний".
# Если треугольник не существует → вывести "Это не треугольник".


# 4. Магазин скидок
# Покупатель вводит сумму покупки.
# Если сумма больше 10 000 крон и день недели "суббота" или "воскресенье" → скидка 20%.
# Если сумма больше 5 000 и день рабочий → скидка 10%.
# Если сумма меньше или равна 1 000 → скидки нет.
# Вывести итоговую цену с учётом скидки. День недели можна ввести в ручную пользователем.

# userMoney = int(input("Please input your total sum:  "))
# day = int(input("Input day 1-7: "))

# if(userMoney > 10000 and day in (6,7)):
#     totalSum = userMoney * 0.8
#     print(f"You have discount 20%, your price {totalSum}")

# elif(5000 <= userMoney < 10000 and day in (1,2,3,4,5)):
#     totalSum = userMoney * 0.9
#     print(f"You have discount 10%, your price {totalSum}")

# else:
#     print(f"You don`t have any discount, your price {userMoney}")

# a = 8
# b = 5
# print( not a == b)


# a = 50000000
# b = 50000000
# print(a is b)

# erroe_massege = 400
# match erroe_massege:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unaothorized")
#     case 402:
#         print("Not Found")

# value  = "Alex"
# match value:
#     case str():
#         print("This is string")
#     case int():
#         print("This is number")

# point = (3, 4)
# match point:
#     case (0, 0):
#         print("You in start position")
#     case (x, 0):
#         print("You are going on horizont")
#     case (0, y):
#         print("You are going on vertikal")
#     case (x, y):
#         print(f"Your vay x: {x}, y: {y}")

# num = 22

# match num:
#     case n if n % 2 == 0:
#         print(" Not even")
#     case n if n % 2 != 0:
#         print(" Not even")
    
# str1 = 15
# print(id(str1))
# str1 = 15.1 
# print(id(str1))


fruits = ["orange", "apple", "banan", "pineapple"]


# print(len(fruits))


# fruits.append("potatoes")
# print(fruits)

# del fruits[2]
# print(fruits)

# # fruits.clear()
# # print(fruits)

# fruits2 = fruits.copy()
# print(fruits2)

list_num = [45,14,45,52,1,45]
# print(list_num.count(45))


# fruits.extend(list_num)
# print(fruits)

# print(fruits.index(45))

# fruits.insert(1, "Good")
# print(fruits)
# fruits.pop(1)
# print(fruits)

# fruits.remove("banan")
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.sort()
# print(fruits)

string = "Hello world!"
# print(len(string))
# print(string[1])
# print(string.upper())
# print(string.lower())
# print(string.strip())
# print(string.split(" "))
# print(string.replace("world","people"))
# print(string.find("o"))
# print(string.index("o"))
# print(string.count("l"))
# print(string.startswith("Hel"))
# print(string.startswith("el"))
# print(string.endswith("ld!"))
# print(string.endswith("el"))
# newstring = ", ".join(fruits)
# print(newstring)
# name = "Alex"
# age = 35
# print("Hello, {}! your are {} years old".format(name, age))
# print(f"Hello, {name}! your are {age} years old")

# print(fruits[-1])
# print(string[2:-3])
# print(string[::3])
# print(string[:])

# for el in fruits:
    # print(el)
# newlist = []
# for num in list_num:
#     if( num == 45):
#         i = list_num.index(num)
#         newlist.append(i)
#         # print(f"Number {num}")
# index = 0

# for el in list1:
#     if el == 45:
#         print(f"Число 45 в списке занимает позицию {index}")
#     index += 1

list1 = [0,45, 14, 47, 78, 45, 45]
# newlist = []
# start = 0

# for num in list1:
#     if num == 45:
#         i = list1.index(num, start) 
#         newlist.append(i)
#         start = i + 1

# print(newlist)

# print(newlist)

# a = 500
# b = 500
# print(a is b)

# for el in range(len(list1)):
#     if list1[el] == 45 :
#         print(f"{el}")
# list2 = list(range(0,10,2)) # start stop step
# list2 = list(range(0,10)) # start stop
# list2 = list(range(10)) # stop
# print(list2)

# a = range(45, 85)
# print(a[5])

# for el, num in enumerate(list1):
#     if num == 45 :
#         print(f"{el}")

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# count = 1
# while count > 0:
#     if count == 10:
#         break
#     print(count)
#     count += 1
# import getpass
# password = ""
# while password != "password":
#     # password = input("Input password, or input exit")
#     password = getpass.getpass("Input password, or input exit")
#     if password == "password":
#         print("ok")

#     if password == "exit":
#         print("Stop")
#         break

# text = "Hello Academy Step!"
# for char in text:
#     if char == "d":
#         break
#     print(char)

# for char in text:
#     if char == "a":
#         continue
#     print(char)