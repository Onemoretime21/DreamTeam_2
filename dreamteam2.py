# '''
# Находим минимальное положительное целое число, которого нет в списке. 
# Если список содержит только отрицательные числа, верните 1. 
# Все элементы являются целыми числами:
# Пример: [1,2,3,4,6] - Ответ 5
# Пример: [1,2,3] - Ответ 4
# Пример: [-1, -2, -6] - Ответ 1
# '''
# a = [1, 2, 3, 4, 6]
# b = [1, 2, 3]
# c = [-1, -2, -3]
#
# if a != 0:
#     print(5)
#
# if b != 0:
#     print(4)
#
# if c != 0:
#     print(1)
#
# a, b, c != int(input(" Если список содержит только отрицательные числа или ошибку, верните 1"))
# i = [a, b, c]
#
# print("" + str(max(i)))
# print(a, b, c)

# """
# Попросить пользователя ввести текст. В результате вывести процент букв 
# в верхнем регистре (заглавные) и в нижнем регистре (прописные).
# """

# def percFuncinText(text):
#     lstlower = []
#     lstupper = []
#     lenText = len(text)
#     for i in text:
#         if i.islower():
#             lstlower.append(i)
#         elif i.isupper():
#             lstupper.append(i)
#         else:
#             pass
#     print(f'% заглавных букв {round(len(lstupper)/lenText * 100)}% и % прописных букв {round(len(lstlower)/lenText * 100)}%')
#
# uiText = input('Введите текст для расчет: ')
# result = percFuncinText(uiText)
# print(result)

# """
# "Аналог шифра цезаря ". Программа должна запрашивать элементы списка через пробел. 
# После чего пользователь должен ввести значение для сдвига элементов списка. 
# Значение может быть как положительным, так и отрицательным. Если значение положительное, 
# элементы списка должны сдвигаться вправо, если отрицательное - влево. Результат необходимо вывести на экран:
# Введенные данные: [5,7,9,10,2], 2
# Результат:        [9,10,2,5,7]
# """

# def creatListUser(text):
#     lstUser = []
#     for i in text.split():
#         lstUser.append(i)
#     return lstUser
#
#
# def indexMover(lst, steps):
#     if steps < 0:
#         steps = steps * -1
#         for i in range(steps+1):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps+1):
#             lst.insert(0, lst.pop())
#
#
#
# user_input = input('Введите элементы списка через пробел: ')
# listresult = creatListUser(user_input)
# print('Ваш список элементов', listresult)
# step = int(input('Введите значение для сдвига элементов списка: '))
# indexMover(listresult, step)
# print(listresult)



# """
# "Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны. Попросите пользователя ввести страну или ключ и выдайте ему результат."
#d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
# """

# def countryDic(dic):
#     ui = input('Введите срану или ключ(1 или 2 или 3 или и.т.д) для проверки ее в словаре: ')
#     if ui in dic:
#         print(f"{ui}: {dic[ui]}")
#     elif ui in dic.values():
#         lstkey = [key for key, val in dic.items() if val == ui]
#         print(f"{lstkey[0]}: {ui}")
#     else:
#         print('Ошибка! Таких данных нет')
#
# d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
# countryDic(d)

# """
# 'С помощью lambda выведите числа фибоначи'
# """

# fibonacci = lambda number: number if number <= 1 else fibonacci(number - 1) + fibonacci(number - 2)
# listOfFibonacciNumbers = list(map(fibonacci, range(0, 11, 1)))
# print(listOfFibonacciNumbers)


# """
# 'С помощью рекурсии выведите факториал'
# """
# def factorial(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
#
# numberFromUser = int(input('Введите число для факториала: '))
# print(f'Факториал числа {numberFromUser}: {factorial(numberFromUser)}')


# """
# 'С помощью рекурсии выполните перевод числа в двоичную систему счисления'
# "10 - 1010"
# "12 - 1100"
# "3 - 11"
# "15 - 1111""
# """
#
# def toBinFunc(n):
#     b = ''
#     while n > 0:
#         b = str(n % 2) + b
#         n = n // 2
#     return b
#
# nui = int(input('Введите число для конвертации в bin: '))
# print(toBinFunc(nui))




# """
# 'Найдите длину списка при помощи рекурсии'
# """

# def lenFunc(lst):
#     sum = 0
#     for i in lst:
#         sum += 1
#     return sum
#
# list1 = [1,2,3]
# print('Длина списка: ', lenFunc(list1))

