# Вложенные функции

# def outer_fanc(who):
#     def inner_func():
#         print('Hello,', who)
#
#     inner_func()
#
#
# outer_fanc('world')


# def func():
#     a = 6                           #2
#     def func2(b):
#         a = 4                       #5
#         print('Сумма: ', a + b)     #6
#
#     print('a:', a)                  #3
#     func2(4)                        #4
#
#
# func()                              #1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     print('global:', x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal:', a)
#
#     inner()
#     print(a)
#     t = a
#
# fn()
# z = x + t
# print(z)
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x  # добавили nonlocal
#             x = 55
#
#         fn3()
#         print('fn2.x=', x)
#
#     fn2()
#     print('fn1.x=', x)
#
#
# fn1()
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b  # добавили nonlocal
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return (a, b)
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# def inerement(number):
#     def inner():
#         return number + 1
#
#     return inner()  #добавили return и всё заработало
#
#
# print(inerement(10))


# Замыкание
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# res = outer(5)
# print(res(10))
# q = res(15)
# print(q)


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)  #добавили 4-ку в список
#         a = a +1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
# res1 = func('Москва')
# res1()
# res1()

#
# students = {
#     "Alice": 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#     return classify_student
#
#
# A = make_classifier(80, 101)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))
#
# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add   # ф-ция создана для удобства, она только помогает
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())


# Вариант1
# def ploshad(a, b, c):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s = 2 * (a * b + a * c + b * c)
#
#     inner()
#     return s
#
#
# print(ploshad(2, 4, 6))
# print(ploshad(5, 8, 2))
# print(ploshad(1, 6, 8))


# Вариант2
# def ploshad(a, b, c):
#     def inner():
#         s = 2 * (a * b + a * c + b * c)
#         return s
#
#     return inner()
#
#
# print(ploshad(2, 4, 6))
# print(ploshad(5, 8, 2))
# print(ploshad(1, 6, 8))


# Вариант3
# = 1
#
#
# def ploshad(a, b, c):
#     global s
#     d = 1
#     s = 2 * d
#
#     def inner():
#         nonlocal d
#
#         d = (a * b + a * c + b * c)
#         return inner()
#
#     return s
#
#
# print(ploshad(2, 4, 6))
# print(ploshad(5, 8, 2))
# print(ploshad(1, 6, 8))
# s


# #Задача №1
# def proiz(y):
#     def inner(x):
#         return y * x
#     return inner
#
# res = proiz(2)
# print(res(15))
# print(res(20))


# #лямда-выраженеия
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))
# (lambda x, y: print('res= ', x + y))(1, 2)
# (lambda x, y: print(x + y))(1, 2)
# print('res=', (lambda x, y: x + y)('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
#
# sum = lambda a=1, b=2, c=3: a + b + c
# print(sum())
# print(sum(10))  # a = 10
# print(sum(10, 20))  # a = 10, b = 20
# print(sum(10, 20, 30))  # a=10, b=20, c=30


# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b'))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
#
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))

# inc2 = (lambda n: (lambda x: x + n))
# # f1 = inc2(42)
# # print(f1(3))
# print(inc2(42)(3))
# print((lambda n: (lambda x: x + n))(42)(3))


# sum3 = ((lambda n: (lambda z: (lambda y: y + z + n))))
# print(sum3(2)(4)(6))
# print((lambda n: (lambda z: (lambda y: y + z + n)))(2)(4)(6))

# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)

# lst.sort()
# print(lst)

# lst.sort(key=lambda i: i[1])  # Если [0], то будет a:,b: c:
# print(lst)

# lst.sort(key=lambda i: i[1], reverse=True)
# print(lst)
#
# dict1 = dict(lst)
# print(dict1)

# plaers = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#           {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#           {'name': 'Фёдор', 'last name': 'Сидоров', 'raiting': 4},
#           {'name': 'Михаил', 'last name': 'Семёнов', 'raiting': 6}]
# ps = sorted(plaers, key=lambda inem: inem['last name'])
# print(ps)
# print()
# ps1 = sorted(plaers, key=lambda i: i['raiting'])
# print(ps1)
# print()
# ps2 = sorted(plaers, key=lambda i: i['raiting'], reverse=True)
# print(ps2)


# a = [(lambda x, y: x + y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[0](12, 5)
# print(b)
# c = a[1](12, 5)
# print(c)


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье'))
# }
#
# d[5]()

# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 13))

# mini = (lambda a, b, c: a if a < b else b if b < c else c)
# print((mini(54, 41, 11)))
# mini2 = (lambda a, b, c: a if (a < b and a < c) else (b if b < a and b < c else c))
# print(mini2(51, 45, 2))


# def multiple(t):
#     return t * 2
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, range(10))))

# t = 2.88, -1.75, 100.55
#
# print(tuple(map(lambda x: int(x), t)))
# print(list(map(lambda x: int(x), t)))
#
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))
# print(list(map(int, map(float, a))))

# areas = [3.3458723, 5.476637, 7.8503456, 56.9845678, 9.231432, 32.6785439]
# print(list(map(round, areas)))
# print(list(map(round, areas, range(1, 7))))
# print(list(map(round, areas, range(1, 3))))
# print(list(map(round, areas, [1, 2, 4, 6, ])))
# print(list(map(round, areas, [1, 1, 1, 1, 1, ])))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, ]
#
# lst = list(map(lambda x, y: (x, y), st, num))
# print(lst)
# print()
# lst1 = dict(map(lambda x, y: (x, y), num, st))
# print(lst1)
# print()
# lst2 = list(map(lambda x, y: [x, y], num, st))
# print(lst2)
# print()
# lst3 = dict(map(lambda x, y: {x, y}, num, st))
# print(lst3)

# tp = dict(lst)
# print(tp)

# t1 = [1, 2, 3]
# t2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, t1, t2)))

# filter (func, iterable)
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)
# res1 = list(filter(lambda s: 75 < s < 88, b))
# print(res1)

# from random import randint
# b = [randint(0, 100) for i in range(10)]
# print(b)
# b2 = list(filter(lambda s: 10 <= s <= 20, b))
# print(b2)


# lst = [45, 55, 60, 37, 100, 105, 220]
# lst1 = list(filter(lambda s: s % 15 == 0, lst))
# print(lst1)

# ДЕКОРАТОРЫ

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
# print()
# test = hello
# print(test())

# Принцип работы декоратора:
# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return wrap
#
#
# def func_test():
#     print("Hello, I am 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# То же самое, но запись с декоратотом @
# def my_decorator(func):  # Декорирующая ф-ция
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return wrap
#
#
# @my_decorator  # Декоратор
# def func_test():  # Декорируемая ф-ция
#     print("Hello, I am 'func_test'")
#
#
# func_test()
#
# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов ф-ции: ', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('hello')
#
#
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):  # Сюда обяз-но два аргумента, т.к. в print_name два аргумента
#         print('*' * 30)
#         fn(arg1, arg2)  # Сюда то же
#         print('^' * 30)
#
#     return wrap
#
#
# @args_decorator
# def print_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_name('Ольга', 'Семёнова')


# def args_decorator(fn):
#     def wrap(*arg, **kwarg):
#         fn(*arg, **kwarg)
#         print('*' * 30)
#         print('args: ', arg)
#         print('kwargs: ', kwarg)
#         print('^' * 30)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Pithon'):
#     print(a, b, c, 'изучают', study, end='\n\n')
#
#
# print_full_name('Ольга,', 'Борис,', 'Светлана', study='JawaScript')
# print_full_name('Владимир,', 'Екатерина,', 'Виктор')

# def decor(args1, args2):  # (*args)
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')  # (args[0], x, args[1], y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)


# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
#
# def multioly(n):
#     def wrap(fn):
#         def wrap2(x):
#             # print('Результат:', x * n)
#             return 'Результат: ' + str(fn(x) * n)  # так правильно
#
#         return wrap2
#
#     return wrap
#
#
# @multioly(3)
# def return_num(num):
#     return num + 2  # добавили 2-ку, а рез-тат не изменился, поэтому код не корректен
#
#
# return_num(5)
# print(return_num(5))
#
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z='Hello! '):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Doge'))
# print(typed_fn2('Hello, ', 'World', '!'))
# print(typed_fn3('Hello', 'World, ', z=5))


# def cnt(fn):
#     def wrap(*args):
#         print('Среднеарифметическое: ', sum(args) / len(args))
#         print('Сумма чисел: ', args, ' = ', fn(*args))
#         print('Сумма чисел: ', *args, ' = ', fn(*args))
#
#
#     return wrap
#
#
# @cnt
# def summer(*ar):
#     return sum(ar)
#
#
# summer(3, 4, 5, 6, 8)


#
# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end='')
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# hello_world2('Hi!')
# hello_world('world')

# print(int('100', 2))  # перевод из 2-чной в 10-чную, ниже аналогично
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))

# print(bin(18))  # 0b10010  0b-ноль, би   2-ичная с-ма счисления
# print(oct(18))  # 0b10010  0b-ноль, o   8-ричная с-ма счисления
# print(hex(18))  # 0b10010  0b-ноль, икс   16-ричная с-ма счисления
#
# print(0b100)
# print(0o20)
# print(0x11)

# q = 'Pyt'
# w = 'hon'
# c = q + w
# print(c)
# print(c * 3)
# print('e' in c)
# print(c[::-1])
# print(c[::])
# c = c[:3] + 't' + c[:4]
# print(c)

# str2 = 'Я изучаю Python. Мне нравится Python. Python очень интересный язык программирования '

#
# def changeChar(s, c_old, c_new):
#     s2 = ''
#     for i in s:
#         if i != c_old:
#             s2 += i
#         else:
#             s2 += c_new
#
#     return s2
#
#
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования '
# st2 = changeChar(st, 'N', 'P')
# print('sr1 =', st)
# print('st2 =', st2)

# print(u'Привет')
# print('C:\file.txt')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file.txt\\'[:-1])  # останется один слеш
# print(r'C:\file.txt' + '\\')
# print('C:\\file.txt\\')

# name = 'Дмитрий'
# age = 25
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' Лет')
# print('Меня зовут ', name, '. Мне ', str(age), ' Лет', sep='')
# print(f'Меня зовут {name}. Мне {age} Лет')
#
# print(f'{round(2.356789, 2)}')
# print(f'{2.356789:.2f}')
#
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}"
#       f" - выражение")

# d = 74
# print(f'{d}')
# print(f'{{d}}')
# print(f'{{{d}}}')  # и так далее

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')


# s1 = """ <div>
#     <a href="#">content</a>
# <div>
# """
# print(s1)
# s1 = ''' <div>
#     <a href="#">content</a>
# <div>
# '''
# print(s1)
# 'Привет'


# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса цилиндра
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# print(ord('a'))
# print(ord('р'))

# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in (input('->'))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:  # можно просто [::], работает так же
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)
# print(arr[::-1])  просто развернёт список


# print(chr(97))
# print(chr(35))
# print(chr(8364))


# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end='')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end='')

# print('apple' == 'Apple')  # False
# print('apple' > 'Apple')  # True
# print(ord('a'))  # 97
# print(ord('A'))  # 65
# print('cQ' == 'Sa')
# print('cQ' > 'Sa')
# print('cQ' < 'Sa')


# from random import randint
#
# SHORTEST = 7
# LONGTEST = 10
# MIN_ASCII =33
# MAX_ASCII =126
#
# def random_password():
#     random_length = randint(SHORTEST, LONGTEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
# print('Ваш случайный пароль:', random_password())
# print(dir(str))


# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())

# print(s.count('l', 3))  # подсчитывает кол-во
# print(s. find('Python1'))
# print(s. find('L', 3))

# a = 'один два'
# b = a[:a.find(' ')]
# c = a[a.find(' ') + 1:]
# print(b)
# print(c)
# print(c + ' ' + b)

# s = 'ab12c59p7dq'
# s1 = []

# for i in s:
#     if i in '1234567890':
#         s1.append(int(i))

# for i in s:
#     if '1234567890'.rfind(i) != -1:
#         s1.append(int(i))
# print(s1)


# s = "hello, WORLD! I am learning Python"
# print(s)
# print(s.index('Python'))
# print(s.index('Python1'))  # выбросит исключение: подстрока не существует

# s = 'I am learning Python. hello, WORLD!'
# f = s.find('h')
# sc = s.rfind('h') + 1
# print(s[:f] + s[sc:])
# print(s[:s.find('h')] + s[s.rfind('h') + 1:])

# print('abc123'.isalnum())
# print('123"'.isalnum())
# print('ABCabc'.isalpha())
# print('ABCabc1'.isalpha())

# print('ABCabc'.isalpha())

# print('py'.center(10))
# print('py'.center(10, '-'))

# print('     py'.lstrip())
# print('py     '.rstrip())
# print('     py  '.strip())
#
# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$;'.rstrip(';$.'))
#
# print("http://www.python.org".lstrip('/:pthsw').rstrip('org.'))
# print("http://www.python.org".strip('htps:/worg.'))
#
# print("http://www.python.org".strip('/:pthsworg').strip('.'))

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print('..'.join(seq))
#
# print(':'.join('Hello'))

# print('Строка разделённая пробелами'.split())
# print('Строка_разделённая_пробелами'.split('_'))
# print('Строка_разделённая_пробелами'.split('а'))

# a = input('->').split()
# a = list(map(int, input('->').split()))
# print(a)


# metod REPLACE
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# print(st)
# print(st.replace('Nython', 'Python'))
# print(st.replace('Nython', 'Python', 2))

# metod JOIN
# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
# print('..'.join(['1', '2', '3']))
# print('..'.join([1, 2, 3]))  # работать не будет
# print('..'.join('Hello'))

# method SPLIT
# print('Строка, разделённая пробелами'.split())
# # print('Строка, разделённая пробелами'.split('!'))
# # print('Строка!, разделённая пробелами'.split('!'))
# # print('Строка_разделённая_пробелами'.split())
# # print('Строка_разделённая_пробелами'.split('_'))
# # print('Строка, разделённая пробелами'.split('а'))  # в скобках буква "а" в русском регистре
# #
# # print('www.python.org'.split('.'))
# # print('www.python.org'.split('.', 1))
# # print('www.python.org'.split('.', 4))

# a = input('->').split()
# print(a)
# b = list(map(int, input('->').split()))  # Получим цельночисловые обьекты


# a = input('Введите ФИО: ').split()
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')
# print(f'{a[0]} {a[1][0]}.{a[2][0]}.')

# print('www.python.org.ru.'.split('.', 2))
# print('www.python.org.ru.'.rsplit('.', 2))
# print('www...python...org...'.rsplit('.'))

# st = 'В строке заменить пробелы символом *'
# print(st.replace(' ', '*'))
# st1 = st.split()
# x = '*'
# print('*'.join(st1))
# print(x.join(st1))
# print('*'.join(st.split()))
import re

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта'
# reg = 'я'
# reg1 = 'совпадения'
# print(s.find(reg))
# print(re.findall(reg, s))
# print(re.findall('12', s))
# print(re.search(reg, s))
# print(re.search(reg1, s))
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = 'я'
# reg1 = '.'
# # reg2 = '\.'
# reg2 = r'\.'  # так будет правильно
# reg3 = r'\.'
# reg4 = r'2023'

# print(re.split(reg, s))
# print(re.split(reg1, s))
# print(re.split(reg2, s))
# print(re.split(reg2, s, 1))
# print(re.sub(reg3, '!', s))
# print(re.sub(reg3, '!', s, 1))
# print(re.findall(reg4, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 1945'

# reg5 = r'[5-9]'
# reg6 = r'[12][09][0-9][0-9]'
# reg7 = r'[а-я]'
# reg8 = r'[А-яё][А-яё]'
# reg9 = r'[^839]'
# reg10 = r'\w'


# print(re.findall(reg10, s))
# print(re.findall(reg9, s))
# print(re.findall(reg5, s))
# print(re.findall(reg6, s))
# print(re.findall(reg7, s))
# print(re.findall(reg7, s))
# print(re.findall(reg8, s))

# st = 'Ели[-ели].'
# pattern = r'[А-яёю.\[\]-]'
# print(re.findall(pattern, st))


# vr = '''Час в 23-часовом формате от 00 до 23. 2021-06-15Т 21:45
#     Минуты в диапазоне от 00 до 59. 2021-86-15-15Т 01:09'''
# pat = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(pat, vr))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5'
# reg = r'\Aищу'
# reg = r'\A\w\s\w+'
# reg = r'\w\s\w\Z'
# reg = r'\b\w\s\w'
# reg = r'\w\s\w\b'
# reg = r'ния\b'
# reg = r'\w+'
# reg = r'\d+'


# print(re.findall(reg, s))

# sf = 'Цифры: 7, +17, -42, 0013, 0.3'
# pat = r'\d+'
# print(re.findall(pat, sf))
# pat1 = r'\S*\d+'
# print(re.findall(pat1, sf))
# pat2 = r'[+-]?\d+[.\d]*'
# print(re.findall(pat2, sf))

# sa = '05-03-1987 # Дата рождения'
#
# print(re.sub(r'#.*', '', sa))
# s8 = re.sub(r'#.*', '', sa)
# print('Дата рождения: ', re.sub('-', '.', s8))


# sp = 'author=Пушкин А.С.; title = Евгений Онегин; price =2000; year= 1831'
# # pat = r'\w+\s*=\s*[^;]+'
# pat = r'\w+\s*=[^;]+'
#
# print(re.findall(pat, sp))


# ax = '12 сентября 2021 года'
# # reg1 = r'\d{4}'
# # reg1 = r'\d{2,4}'
# reg1 = r'\w{2,4}'
# # reg1 = r'[а-я]{2,4}'
# print(re.findall(reg1, ax))


# ad = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# # reg = r'\+?7\d{10}'
# # reg = r'[+]?7\d{10}'
# reg = r'[+]?\d{11}'
# print(re.findall(reg, ad))


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5'
# reg = r'\w+\s\w+'
# reg1 = r'^\w+\s\w+'
# reg2 = r'\w+\s\w+$'
#
# print(re.findall(reg, s))
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))


# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}', a)
#
#
# print(login('admin_admin'))
# print(login('*admin_admin'))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# print(re.findall(r'[я]', 'Яя', flags=re.IGNORECASE))
# print(re.findall(r'[я]', 'Яя'))
# print(re.findall(r'[а-я]', 'Яя', flags=re.IGNORECASE))


# text = '''
# one
# two
# '''
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r'^one', text, re.MULTILINE))
# print(re.findall(r'^one$', text, re.MULTILINE))


# text = '''
# one
# two
# '''
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))


# s = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, login-1@i.ru'
#
# reg = r'[\w.-]+@[\w.]+\w{2,3}'
# print(re.findall(reg, s))


# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.+?>', text))


# *?, +?, ??
# {m,n}?, {,n}?, {n,}?

# t = '2324 786 22 4569'
# reg = r'\d{1,3}?'
# print(re.findall(reg, t))

# s = "<p>Изображение <ing alt='картинка' scr='bg.jpg' title=подсказка> - фон страницы</p>"
# reg = r'<ing\s+[^>]*scr\s*[^>]+>'
# print(re.findall(reg, s))


# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r'\[\d+\]'
# print(re.findall(reg, s))

# s = 'Пётр и Ольга отлично учатся!'
# reg = 'Пётр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(?:int|double)\s*=\s*\d+[.\w+]*"
# print(re.findall(reg, s))

# 192.168.255.255
# s = "127.0.0.1"
# reg = r"\d{1,3}.\d{1,3}.\d{1.3}.\d{1,3}"

# s = "Word2016, PS6, AI5"
# reg = r"[A-z]+\d*"
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5'
# reg = r"([0-9]+)\s(\D+)"
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


# s1 = '+7 499-456-45-78'
# s2 = '+74994564578'
# s3 = '7 (499) 456 45 78'
# s4 = '+7 (499) 456-45-78'
# reg = r'^([+]*\d{1}[\s|(]*\d{3}[)|\s|-]*\d{3}[\s|-]*\d{2}[\s|-]*\d{2})$'
# print(re.findall(reg, s1))
# print(re.findall(reg, s2))
# print(re.findall(reg, s3))
# print(re.findall(reg, s4))


# s = '31'
# reg = r'(?:0?[1-9]|[12][0-9]|[3][01])'

# s = '12'
# reg = r'(?:0?[1-9]|[1][12])'

# s = '2022'
# reg = '([1][9][0-9][0-9]|[2][0][0-2][0-9])'

# data = "30-12-2023"
# reg = r'^(?:0?[1-9]|[12][0-9]|[3][01])[-](?:0?[1-9]|[1][12])[-]([1][9][0-9][0-9]|[2][0][0-2][0-9]$)'
# print(re.findall(reg, data))
# reg1 = r'[^\d]'
# data1 = ' '.join(re.split(reg1, data))
# print(data1)
# reg2 = r'(\d{2}[ ])(\d{2}[ ])(\d{4})'
# print(re.findall(reg2, data1))


# def data(s):
#     reg = r'^(?:0?[1-9]|[12][0-9]|[3][01])[-](?:0?[1-9]|[1][12])[-]([1][9][0-9][0-9]|[2][0][0-2][0-9]$)'
#     reg1 = r'[^\d]'
#     reg2 = r'(\d{2}[ ])(\d{2}[ ])(\d{4})'
#
#     if re.findall(reg, s) == []:
#         print('Неправильно осуществлён ввод данных')
#     else:
#         print('Результат: ', re.findall(reg2, ' '.join(re.split(reg1, s))))
#
#
# d_m_year = input('Введите дату, месяц, год в формате dd-mm-yyyy: ')
# data(d_m_year)

#
# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))


# s = "<p>Изображение <ing scr='bg.jpg'> - фон страницы</p>"
# # reg = r'<ing\s+[^>]*scr=([\'"])(.+)\1>'
# reg = r'<ing\s+[^>]*scr=(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))

# s = "Самолёт прилетает 10/23/2023. Будем рады вас видеть 10/24/2023"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "google.com and google.ru and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# ДЗ № 22-1
# test = "1X, Text, ACC 123 A1B2C3"
# reg4 = r'(\D|\d{3})'
#
# # print(re.findall(reg4, test))
# # print(re.sub(reg4, r'', test))
# st = re.sub(reg4, r'', test)
# s = list(st)
# print(s)
# print(list(re.sub(reg4, r'', test)))


# ДЗ №22-2
# txt1 = "#START# tile #END#"
# reg = r'[a-z]{4}'
# print(re.findall(reg, txt1))
#
# reg2 = r'#[A-Z]+#'
# print(re.sub(reg2, r'', txt1))

# ДЗ № 22-3
# dig = "12_34__56"
# reg = r'\A\d{2}'
# print(re.findall(reg, dig))

# РЕКУРСИЯ

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input("На каком Вы этаже"))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(4, 2))

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


# print(type(names[0]) == str)
# print(type(names[0]) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#
#         else:
#             cnt += 1
#     return cnt
#
#
# print(count(names))

# def union(s):
#     if not s:  # s == []:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print("Выпрямленный список:", union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
# print(remove(" Hello\tWorld  "))



# ДЗ № 22-1
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(len(names))
# s = []
# for i in range(len(names)):
#     if type(names[i]) == str:
#         s.append(names[i])
#     else:
#         for j in range(len(names[i])):
#             if type(names[i][j]) == str:
#                 s.append(names[i][j])
#             else:
#                 for k in range(len(names[i][j])):
#                     if type(names[i][j][k]) == str:
#                         s.append(names[i][j][k])
#
# print(s)




# ДЗ № 22-2
s = []


def minus(sp):
    if not sp:
        return print(len(s))
    if sp[0] < 0:
        s.append(sp[0])
        print(s)
    return s, minus(sp[1:])
    # s.append(sp[0])
    # print(s)
    # return minus(sp[1:])


minus([-2, 3, 8, -11, -4, 6])

# sp = [-2, 3, 8, -11, -4, 6]
# c = []
# for i in range(len(sp)):
#     if sp[i] < 0:
#         c.append(sp[i])
# print(c)


# for i in sp:
#     if i < 0:
#         c.append(i)
# print(c)
