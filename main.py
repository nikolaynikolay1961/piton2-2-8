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

# РЕКУРСИЯ ****************************************************************************

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
#                     ****************************************
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
#                          ***********************************************
# def to_str(n, base):
#     convert = "0123456789"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(4, 2))

#                    **********************************************

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


# ДЗ № 23-1
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


# ДЗ № 23-2
# s = []
#
#
# def minus(sp):
#     if not sp:
#         return print(len(s))
#     if sp[0] < 0:
#         s.append(sp[0])
#         print(s)
#     return s, minus(sp[1:])
#     # s.append(sp[0])
#     # print(s)
#     # return minus(sp[1:])
#
#
# minus([-2, 3, 8, -11, -4, 6])

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

#           ***  файлы ********************************************************

# f = open('text.txt', 'r')
# # f = open('text.txt', mode='r')  # аналогичная запись
# print(f)
# print(*f)  # распаковка файла
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))  # считает первых три символа
# print(f.read())  # считает остальное
# f.close()

# f = open('text.txt', 'r')
# try:
#     print(f.read())
# finally:       # даже если файл повреждён 'файнели' всё равно закроет файл
#     f.close()


# f = open('text1.txt', 'r')
# # print(f.readline())  # считывает построчно до первого переноса на другую строчку
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('text1.txt', 'r')
# print(f.readlines())  # возвращает список строк
# f.close()


# f = open('text1.txt',  'r')
# for line in f:
#     print(line, end='\r')  # end='\r' убирает лишний перенос строки
# f.close()

# f = open('text1.txt',  'r')
# count = 0
# for line in f:
#     count += 1
# f.close()
# print(count)

# f = open('text1.txt',  'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Привет\nWorld!')
# f.close()

# f = open('xyz.txt', 'a')  # добавляем новый текст
# f.write('\nНовый текст')
# print(f.write('\nНовый текст'))  # возвратит кол-во дописанных символов
# f.close()

# f = open('xyz.txt', 'a', )
# # print(f.write('\nНовый текст'))
# lines = ['\nЛиния 1', '\nЛиния 2']
# f.writelines(lines)  # берёт эл-ты из списка и добавляет их
# f.close()

# f = open('xyz.txt', 'w')
# # lst = [str(i) + str(i - 1) + '\t' for i in range(1, 20)]
# lst = [str(i) + str(i - 1) for i in range(1, 20)]
# print(lst)
# # f.writelines(lst)
#
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
# #
# f = open("text2.txt", "r")
# read_file = f.readlines()  # считает все данные в виде списка
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменить строку в списке;\n':
#         read_file[i] = 'Hello world\n'
# print(read_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_file)  # заменили текст в файле
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# ind = int(input('Введите номер строки'))
# f = open("text2.txt", "r")
# read_file = f.readlines()
# f.close()
# if 0 > ind - 1 <= len(read_file):
#     print("Неправильно введён номер")
#
# else:
#     read_file.pop(ind - 1)
# print(read_file)
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()


# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("--new string--"))  # I a--new string--hon
# print(f.tell())
# f.close()


# f = open('text.txt', 'a')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("--new string--"))  # I a--new string--hon
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# # print(f.seek(3))
# print(f.write("--new string--"))  # I a--new string--hon
# print(f.tell())
# f.close()


# f = open("textdz.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# pos1 = int(input('Введите номер строки, которую хотите переместить: '))
# pos2 = int(input("С какой строкой хотите поменять местами: "))
# f = open("textdz.txt", "r")
# read_file = f.readlines()
# f.close()
# if 0 > pos1 - 1 and pos2 <= len(read_file):
#     print("Неправильно введён номер")
#
# else:
#     read_file[pos1 - 1], read_file[pos2 - 1] = read_file[pos2 - 1], read_file[pos1 - 1]
# print(read_file)
# print(read_file[1])
# f = open("textdz.txt", "w")
# f.writelines(read_file)
# f.close()

# with open('text5.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text2.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]

# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# print(get_line(lst))


# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# lst = list(map(float, nums.split(' ')))
# print(lst)
# print(len(lst))

# Задача: Написать ф-цию, к-рая выводит слово из файла, имеющее макс-ую длину
#        (или список слов, если таковых несколько)

# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))  # max(w, key=len) = самое длинное слово
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = 'res.txt'
# print(longest_words(file_name))

#       ________________________________________________________________________

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\n"
#
# with open("one.txt", 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)

# Модуль OS и OS.PATH  *******************************************************************

# print("Текущая директория: ", os.getcwd())
#
# print(os.listdir())
# print(os.listdir(".."))
# os.mkdir("folder")
# os.makedirs("nested1/nested2/nested3")
# os.remove("xyz.txt")

# os.rename('nested1', 'test')  # переименовывает файл или директорию
# os.rename("test.txt", 'test/test1.txt')
# os.rmdir("folder")

# print(os.walk("test"))
# for root, dirs, files in os.walk("test", topdown=True):
#     print("Root:", root)
#     print("Subdirs", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")


# remove_empty_dirs("test")


# print(os.path.split())
# print(os.path.dirname())
# print(os.path.basename())
# print(os.path.join())

# dirs = ["Work/F1", "Work/F2/F21"]
# for d in dirs:
#     os.makedirs(d)

# files = {'Work': ['w.txt'],
#          'Work/F1': ['fl1.txt', 'fl2.txt', 'fl3.txt'],
#          'Work/F2/F21': ['f211.txt', 'f212.txt']
#          }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()

# file_text = ['Work/w.txt', 'Work/F1/fl2.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст для файла по пути {file}.")

# DZ **********************************************

# read_file1 = 'one.txt'
# read_file2 = 'two.txt'
# write_file = 'union.txt'
#
# with open(read_file1, 'r') as f1, open(read_file2, 'r') as f2, open(write_file, 'w') as fw:
#     for line1, line2 in zip(f1, f2):
#         line = (str(line1).strip() + ' ' + str(line2).strip() + '\n')
#
#         fw.write(line)
#         print(line)

# print("     Обход сверху вниз")
# for root, dirs, files in os.walk('Work', topdown=True):
#     print(root, '\n', '\t', dirs, '\n', '\t', files)

#     print("     Обход снизу вверх:")
# for root, dirs, files in os.walk('Work', topdown=False):
#     print(root, '\n', '\t', dirs, '\n', '\t', files)
# **********************************************************************************************

# грамотное решение

# def print_tree(root, topdown):
#     print(f"Обход {root} {'Сверху вниз' if topdown else 'Снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root, '\n', '\t', dirs, '\n', '\t', files)
#     print('-' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# print(os.path.exists(r'путь к папке'))   # существует ли этот файл
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# path = 'text.txt'
# # print(os.path.getatime(path))  # возвращает время последнего доступа к файлу в секундах
# # print(os.path.getctime(path))  # возвращает время создания файла
# # print(os.path.getmtime(path))  # время последнего изменения файла
# # print(os.path.getsize(path))  # размер файла в байтах
# size = os.path.getsize(path) / 1024  # перевод в килобайты
# print(size)
# t = os.path.getctime(path)
# print(time.strftime('%d.%m.%Y, %H:%M.%S', time.localtime(t)))
#
#
# print(os.path.isfile(r"Work\w.txt"))  # является ли документ файлом
# print(os.path.isdir(r"Work\w.txt"))  #  является ли документ папкой (директорией)
# если документа не существует, то тоже False


# print(os.path.exists(r'C:\Users\Дмитрий\PycharmProjects\pythonProject'))
# print(os.path.exists('Work'))
# если путь или папка существует, то True, если нет - то False

# *****************************************************************************

# class Point:
#     '''Класс для представления координат точек на плоскости'''
#     x = 1
#     y = 1


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# x = 5
# p1 = Point()
# p2 = Point()
# print("p1 =", p1.x)
# print("Point =", Point.x)
#
# p1.x = 100
# p2.x = 200
# print(p1.x)
# print(p2.x)
# print(Point.x)


# class Point:
#     x = 1
#     y = 1
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print("Метод set_coord")
#         print(self.__dict__)
#
#
# p1 = Point()
# print(p1.x)
# p1.x = 5
# p1.y = 10
# p1.set_coord()  # равнозначные записи
# Point.set_coord(p1)  # ----//----

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x  # то есть : p1.x = x, вместо self приходит экземпляр
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# p2 = Point()
# p2.set_coord(3, 9)
# print(p2.__dict__)
# print(p2.x)

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#
#     def print_info(self):
#         print('Персональные данные'.center(40, '*'))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("_" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name('Алевтина')
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday("30.02.1989")
# print(h1.get_birthday())

#
# class Book:
#     title = 'title'
#     release = 'release'
#     publisher = 'publisher'
#     genre = 'genre'
#     author = 'author'
#     price = 'price'
#     circulation = 'circulation'
#
#     def print_info(self):
#         print('Данные о книге'.center(50, '-'), '\n')
#         print(f"Название: {self.title}\nГод выпуска: {self.release}\nИздатель: {self.publisher}\n"
#               f"Жанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}\nТираж: {self.circulation}")
#         print("--+--" * 10)
#
#     def input_info(self, title, release, publisher, genre, author, price, circulation):
#         self.title = title
#         self.release = release
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#         self.circulation = circulation
#
#     def set_title(self, title):
#         self.title = title
#
#     def get_title(self):
#         return self.title
#
#     def set_release(self, release):
#         self.release = release
#
#     def get_release(self):
#         return self.release
#
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def get_genre(self):
#         return self.genre
#
#     def set_author(self, author):
#         self.author = author
#
#     def get_author(self):
#         return self.author
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#     def set_circulation(self, circulation):
#         self.circulation = circulation
#
#     def get_circulation(self):
#         return self.circulation
#
#
# h1 = Book()
# h1.print_info()
# h1.input_info("Орфографический словарь", "1984", 'изд.Просвещение', "учебная литература", "Ушаков", "40 коп.", "2млн")
# h1.print_info()
# h1.set_circulation('3 000 000 экз.')
# h1.print_info()


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def prin_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника: ", self.skill, '\n')
#
#
# p1 = Person("Viktor", "Reznik")
# p1.prin_info()
# p1.add_skill(2)
#
# p2 = Person("Anna", "Dolgina")
# p2.prin_info()
# p2.add_skill(3)

#
# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра", self.__class__.__name__)
#
#     def print_coord(self):
#         print(f"x: {self.x}, y: {self.y}")


# p1 = Point(5, 10)
# # print(p1.__dict__)
# p1.print_coord()
# print(id(p1))
#
# p2 = Point(2, 7)
# # del p2
# p2.print_coord()
# print(id(p2))

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1  # а если self.count += 1, то p1.count = 1 у всех р.2, р.3, и т.д.
#         self.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(7, 2)
# print(p2.count)
# p3 = Point(3, 4)
# print(p3.count)
# print(Point.count)
# print(p3.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#
#     def say_hi(self):
#         print("Приветствую. Меня зовут", self.name)


# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid2 = Robot('C-3P0')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)

# droid3 = Robot('RP-xP0')
# droid3.say_hi()
# print('Численность роботов:', Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы завершили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
# print('Численность роботов в конце программы:', Robot.k)

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 15
# print(p1.z)
# print(p1.__x, p1.__y)
# print(p1.get_coord())
# p1.set_coord(1, 2)
# print(p1.get_coord())
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.x, p1.y)
# print(p1.__dict__)


# print(('*' * 7 + '\n') * 3)
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_coord_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord_x(self):
#         return print("Высота прямоугольника:", self.__x)
#
#     def set_coord_y(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord_y(self):
#         return print("Ширина прямоугольника:", self.__y)
#
#     def square(self):
#         print("Площадь прямоугольника:", self.__x * self.__y)
#
#     def perimetr(self):
#         print("Периметр прямоугольника:", (self.__x + self.__y) * 2)
#
#     def hypotenuse(self):
#         print("Гипотенуза прямоугольника:", round((self.__x ** 2 + self.__y ** 2) ** (1 / 2), 2))
#
#     def picture(self):
#         print(('*' * self.__y + '\n') * self.__x)


# p1 = Rectangle(3, 9)
# p1.get_coord_x()
# p1.get_coord_y()
# p1.square()
# p1.perimetr()
# p1.hypotenuse()
# p1.picture()


#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):  # получаем __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):  # Устанавливаем __set_x
#         print("Вызов __set_x")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x

# x = property(__get_x, __set_x, __del_x)


# p1 = Point(5, 10)
# p1.x = 100
# print(p1.__dict__)
# print(p1.x)
# del p1.x
# print()

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.2046
#
#
# weight = KgToPounds(12)  # экземпляр класса
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 2.3
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")


# class Person:
#     def __init__(self, name, skill):
#         self.__name = name
#         self.__skill = skill
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self, name):
#         del self.__name
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, skill):
#         self.__skill = skill
#
#     @skill.deleter
#     def skill(self, skill):
#         del self.__skill
#
#
# p1 = Person("Viktor", 12)
# print(p1.name, p1.skill)
# p1.name = "Ann"
# p1.skill = 16
# print(p1.name, p1.skill)
# # del p1.name
# print(p1.name)

# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 7)
# print(p1.get_count())
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Args:
#     @staticmethod
#     def max(*args):
#         return max(args)
#
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def art(*args):
#         return sum(args) // len(args)
#
#     @staticmethod
#     def fac(x):
#         z = 1
#         for i in range(1, x + 1):
#             z *= i
#         return z
#
#
# print(Args.max(3, 5, 7, 9))
# print(Args.min(3, 5, 7, 9))
# print(Args.art(3, 5, 7, 9))
# print(Args.fac(6))

# class Number:
#     @staticmethod
#     def max(*args):
#         max1 = 0
#         for i in args:
#             max1 = max1 if i < max1 else i
#         return max1
#
#
# print(Number.max(3, 5, 7, 9))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"


# d = Date()
# string_date = '23.10.2022'
# string_date = d.from_string('23.10.2022')
# day, month, year = map(int, string_date.split('.'))
# print(day, month, year)
# data = Date(day, month, year)
# print(data.string_to_db())
# print(string_date.string_to_db())
# string_date1 = Date.from_string('21.12.2021')
# print(string_date1.string_to_db())

# class Counting:
#     __count = 0
#
#     @staticmethod
#     def triangle(a, b, c):
#         p = (a + b + c) * 0.5
#         s = p * (p - a) * (p - b) * (p - c)
#         Counting.__count += 1
#         return print("Площадь треугольника по формуле Герона", (a, b, c), ':', round((s ** (1 / 2)), 3))
#
#     @staticmethod
#     def triangle2(d, h):
#         s1 = d * h * 0.5
#         Counting.__count += 1
#         return print('Площадь треугольника по высоте и основанию', (d, h), ":", s1)
#
#     @staticmethod
#     def rectangle(dl, h):
#         s2 = dl * h
#         Counting.__count += 1
#         return print(" Площадь прямоугольника со сторонами", (dl, h), ':', s2)
#
#     @staticmethod
#     def square(r):
#         Counting.__count += 1
#         return print("Площадь квадрата со стороной ", r, ':', r ** 2)
#
#     @staticmethod
#     def quantity():
#         return print("Количество подсчетов площади:", Counting.__count)
#
#
# Counting.triangle(3, 4, 5)
# Counting.triangle2(7, 6)
# Counting.rectangle(2, 6)
# Counting.square(6)
# Counting.quantity()

# class Account:
#     rate_usd = 0.13
#     rate_euro = 0.11
#     suffix = 'RUB'
#     suffix_usd = 'usd'
#     suffix_euro = 'euro'

# def __init__(self, num, surname, percent, value=0):
#     self.num = num
#     self.surname = surname
#     self.percent = percent
#     self.value = value
#     print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт.")
#     print("-*-" * 16)
#
# def __del__(self):
#     print('*' * 30)
#     print(f'Счёт # {self.num} принадлежащий {self.surname} был закрыт')
#
# @classmethod
# def set_usd_rate(cls, rate):
#     cls.rate_usd = rate
#
# @classmethod
# def set_euro_rate(cls, rate):
#     cls.rate_euro = rate
#
# @staticmethod
# def convert(value, rate):
#     return value * rate
#
# def edit_owner(self, surname):
#     self.surname = surname
#
# def add_persons(self):
#     self.value += self.value * self.percent
#     print('Проценты начислены')
#     self.print_balance()
#
# def withdraw_money(self, val):
#     if val > self.value:
#         print(f"Нет такой суммы {val} {Account.suffix}")
#     else:
#         self.value -= val
#         print(f"{val} {Account.suffix} Снято")
#     self.print_balance()
#
# def add_money(self, val):
#     self.value += val
#     print(f"{val} {Account.suffix} добавлено")
#     self.print_balance()

# def convert_to_usd(self):  # добавить
#     usd_val = Account.convert(self.value, Account.rate_usd)
#     print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")
#
# def convert_to_euro(self):
#     euro_val = Account.convert(self.value, Account.rate_euro)
#     print(f'Состояние счёта: {euro_val} {Account.suffix_euro}')
#
# def print_balance(self):
#     print(f"Текущий баланс {self.value} {Account.suffix}")
#
# def print_info(self):
#     print('Информация о счёте')
#     print('-' * 29)
#     print(f"#{self.num}")
#     print(f'Владелец: {self.surname}')
#     self.print_balance()
#     print(f"Проценты: {self.percent:.0%}")
#     print('-' * 20)


# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_euro()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_euro_rate(3)
# acc.convert_to_euro()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_persons()
# acc.convert_to_euro()
# print()
# acc.withdraw_money(100)
# acc.add_money(5000)
# acc.withdraw_money(3000)

#
# import re
# #
# #
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verity_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()  # ("Волков", "Игорь", "Николаевич")
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError(" В ФИО можно только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес должен быть числом от 20кг и выше')
#
#     @staticmethod
#     def verity_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер числа должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter  # добавить 2 метода
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verity_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Сидоров Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)

# class Client:
#     course_usd = 0.11
#     course_euro = 0.13
#     currency = 'RUB'
#     currency_usd = 'USD'
#     currency_euro = 'EUR'
#
#     def __init__(self, score=0, surname=0, percent=0, value=0):
#         self.__score = score
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счёт #{self.__score} принадлежащий {self.__surname} был открыт.")
#         print("-*-" * 16)
#
#     def __del__(self):
#         print('*' * 30)
#         print(f"Счёт# {self.__score} принадлежащий {self.__surname} был закрыт")
#
#     def set_score(self, score):
#         self.__score = score
#
#     def get_score(self):
#         return self.__score
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname

#        def set_percent(self, percent):
#            self.__percent = percent


#       def get_percent(self):
#            return self.__percent


#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return self.__value
#
#     def print_info(self):
#         print('Информация о счёте:')
#         print('=' * 19)
#         print(
#             f'#{acc.get_score()}\nВладелец:{acc.get_surname()}\nТекущий баланс:{acc.get_value()}'
#             f'\nПроценты:{acc.get_percent(): .0%}')
#         print('-' * 19)
#
#     def convert_usd(self):
#         usd_val = self.__value * Client.course_usd
#         print(f'Состояние счёта:{usd_val}{Client.currency_usd}')
#
#     def convert_euro(self):
#         euro_val = self.__value * Client.course_euro
#         print(f'Состояние счёта:{euro_val}{Client.currency_euro}')
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.__value} {Client.currency}")
#
#     def add_percent(self):
#         self.__value += self.__value * self.__percent
#         print("\n", 'Проценты успешно начислены')
#         self.print_balance()
#
#     def take_of(self, money):
#         if money > self.__value:
#             print(f"\nНа счету нет такой суммы: {money} {Client.currency}")
#             self.print_balance()
#         else:
#             self.__value -= money
#             print(f"\n{money} {Client.currency} успешно сняты")
#             self.print_balance()
#
#     def put_on(self, money):
#         self.__value += money
#         print(f"\n{money} {Client.currency} зачислены")
#         self.print_balance()
#
#
# acc = Client('12345', 'Долгих', 0.03, 1000)
#
# acc.set_score('12345')
# acc.set_surname('Долгих')
# acc.set_percent(0.03)
# acc.set_value(1000)
#
# acc.print_info()
# print()
# acc.convert_usd()
# acc.convert_euro()
# print()
# acc.set_surname('Дюма')
# acc.print_info()
# acc.add_percent()
# acc.take_of(100)
# acc.take_of(3000)
# acc.put_on(5000)
# acc.take_of(3000)


# class Client:
#     course_usd = 0.11
#     course_euro = 0.13
#     currency = 'RUB'
#     currency_usd = 'USD'
#     currency_euro = 'EUR'
#
#     def __init__(self, score=0, surname=0, percent=0, value=0):
#         self.__score = score
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         # print(f"Счёт #{self.__score} принадлежащий {self.__surname} был открыт.")
#         # print("-*-" * 16)
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#         self.__score = score
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     def print_info(self):
#         print('Информация о счёте:')
#         print('=' * 19)
#         print(
#             f'#{acc.__score}\nВладелец:{acc.__surname}\nТекущий баланс:{acc.__value}'
#             f'\nПроценты:{acc.__percent: .0%}')
#         print('-' * 19)
#
#     def client_info(self):
#         print(f"Счёт #{acc.__score} принадлежащий {acc.__surname} был открыт.")
#         print("-*-" * 16)
#
#     def convert_usd(self):
#         usd_val = self.__value * Client.course_usd
#         print(f'Состояние счёта:{usd_val}{Client.currency_usd}')
#
#     def convert_euro(self):
#         euro_val = self.__value * Client.course_euro
#         print(f'Состояние счёта:{euro_val}{Client.currency_euro}')
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.__value} {Client.currency}")
#
#     def add_percent(self):
#         self.__value += self.__value * self.__percent
#         print("\n", 'Проценты успешно начислены')
#         self.print_balance()
#
#     def take_of(self, money):
#         if money > self.__value:
#             print(f"\nНа счету нет такой суммы: {money} {Client.currency}")
#             self.print_balance()
#         else:
#             self.__value -= money
#             print(f"\n{money} {Client.currency} успешно сняты")
#             self.print_balance()
#
#     def put_on(self, money):
#         self.__value += money
#         print(f"\n{money} {Client.currency} зачислены")
#         self.print_balance()
#
#
# acc = Client()
# acc.client_info()
# acc.score = '12345'
# acc.surname = 'Долгих'
# acc.percent = 0.03
# acc.value = 1000
# acc.print_info()
#
# print()
# acc.convert_usd()
# acc.convert_euro()
# print()
# acc.surname = 'Дюма'
# acc.print_info()
# acc.add_percent()
# acc.take_of(100)
# acc.take_of(3000)
# acc.put_on(5000)
# acc.take_of(3000)

#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):  # создали метод, т.к. переменна width закрыта
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределённый инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"рисование линии: {self._ep}, {self._sp}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def __init__(self, sp, ep, color, width, bg='yellow'):
#         super().__init__(sp, ep, color, width)
#         self._background = bg
#
#     def draw_rect(self) -> str:
#         print(f"рисование Прямоугольника: {self._ep}, {self._sp}, {self._color},"
#               f" {self.get_width()} {self._background}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# Line.draw_line(line)
# # print(line._color)
# # print(isinstance(Point, object))
# rect = Rect(Point(30, 40), Point(70, 80), 'red', 10)
# rect.draw_rect()

# DRY (Don't Repeat Yourself) - не повторяйся

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f"{self.__color}"
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"{self.__width}, {self.__height}, {self.color}"  # self.color - это метод из род.класса
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @width.setter
#     def width(self, h):
#       if h > 0:
#           self.__height = h
#       else:
#
#           raise ValueError("Высота должна быть положительным числом")
#
#     def area(self):
#         return self.__width * self.__height
##        return self.width * self.height   # одно и то же
#
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect)
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = "red"
# rect.width = 5
# print(rect)
# print(rect.area())

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"=Прямоугольник=:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()  # добавляем метод из родительского класса
#         print("Фон", self.fon)

# class RectFonBorder(RectFon):
#     def __init__(self):(self, width, height, background, border):
#         super().__init__(width, height, background)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print('Рамка: ', self.border)


# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)


# shape = Rect(100, 200)
# shape.show_rect()
# shape1 = RectFon(400, 300, 'yellow')
# shape1.show_rect()
# shape2 = RectBorder(600, 500, '1px solid red')
# shape2.show_rect()
# shape3 = RectFonBorder(600, 500, 'yellow', '1px solid red')
# shape3.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))  # ['1' '2' '3'] -> 1 2 3
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегрузка методов
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#    # def set_coord(self, sp, ep):
#    #     if sp.is_int() and ep.is_int():
#    #         self._sp = sp
#    #         self._ep = ep
#
#
# class Line(Prop):

#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp= sp
#         else:
#             if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# Line.set_coord(Point(20, 40), Point(50, 60)
# line.draw_line()

# Абстрактные методы
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width

#

#
#     def draw_line(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод draw() ")
#
#
# class Line(Prop):
#      def draw_line(self):
#          print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(50, 60))
# line.draw_line()

# import re
#
#
# class AutoMobile:
#     def __init__(self, model=0, year=0, manufacturer=0, power=0, color=0, price=0):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.power = power
#         self.color = color
#         self.price = price
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         self.__model = model
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         self.verify_year(year)
#         self.__year = year
#
#     @property
#     def manufacturer(self):
#         return self.__manufacturer
#
#     @manufacturer.setter
#     def manufacturer(self, manufacturer):
#         self.verify_manufacturer(manufacturer)
#         self.__manufacturer = manufacturer
#
#     @property
#     def power(self):
#         return self.__power
#
#     @power.setter
#     def power(self, power):
#         self.verify_power(power)
#         self.__power = power
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         self.verify_color(color)
#         self.__color = color
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, price):
#         self.verify_price(price)
#         self.__price = price
#
#     @staticmethod
#     def verify_manufacturer(manuf):
#         if not isinstance(manuf, str):
#             raise TypeError("Название марки автомобиля должно быть строкой")
#
#     @staticmethod
#     def verify_power(pow):
#         if not isinstance(pow, int) or pow < 300 or pow > 600:
#             raise TypeError("Мощность должна быть в числах от 300 до 600 л.с.")
#
#     @staticmethod
#     def verify_year(year):
#         if not isinstance(year, int) or year < 2019:
#             raise TypeError("Год выпуска должен быть в числах и не раньше 2019 года")
#
#     @staticmethod
#     def verify_color(color):
#         if not isinstance(color, str):
#             raise TypeError("Цвет должен быть строкой")
#
#     @staticmethod
#     def verify_price(price):
#         if not isinstance(price, int) or price > 15000000:
#             raise TypeError("Цена в числах и не более 15 млн. руб.")
#
#
#
#
#     def auto_info(self):
#         print('Данные автомобиля'.center(40, '-'))
#         print(f'Название модели: {auto.model}\nГод выпуска: {auto.year}'
#               f'\nПроизводитель: {auto.manufacturer}'
#               f'\nМощность: {auto.power} л.с.\nЦвет: {auto.color}'
#               f'\nЦена: {self.auto_list()}  ')
#
#     def auto_list(self):
#         s = str(auto.price)
#         a = s[-3:]
#         b = s[:-6]a
#         c = s[-6:-3]
#
#         return str(b + ' млн ' + c + ' тыс ' + a + " руб")
#
#
# auto = AutoMobile()
# auto.model = 'X7'
# auto.year = 2021
# auto.manufacturer = 'BMW'
# auto.power = 530
# auto.color = 'white'
# auto.price = 10790000
# auto.auto_info()

# class Table:
#     def __init__(self, width=0, height=0, radius=0):
#         self.width = width
#         self.height = height
#         self.radius = radius
#
#     def square_table(self):
#         raise NotImplementedError("В дочернем классе должен быть метод определения площади")
#
#
# class RoundTable(Table):
#     def square_table(self, width=None, height=None, radius=None):
#         if width is None and height is None:
#             self.radius = radius
#             srt = 3.14 * self.radius ** 2
#             print(f"Площадь круглого стола: {srt}")
#
#
# class RectTable(Table):
#     def square_table(self, width=None, height=None, radius=None):
#         if radius is None and width != height:
#             self.width = width
#             self.height = height
#             print(f"Площадь прямоугольного стола: {self.width * self.height}")
#         if width == height:
#             self.width = width
#
#             print(f"Площадь квадратного стола: {self.width ** 2 }")
#
#
# table = RoundTable()
# table.square_table(radius=20)
# table1 = RectTable()
# table1.square_table(10, 20)
# table2 = RectTable()
# table2.square_table(15, 15)
# table1.__dir__()  # не работает?


# Правильное решение ДЗ
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, height=None, radius=None):
#         if radius is None:
#             if height is None:
#                 self._width = self._height = width
#             else:
#                 self._width = width
#                 self._height = height
#         else:
#             self._radius = radius
#
#     def square_table(self):
#         raise NotImplementedError('В дочернем классе должен быть метод определения площади')
#
#
# class RectTable(Table):
#     def square_table(self):
#         return self._width * self._height
#
#
# class RoundTable(Table):
#     def square_table(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = RectTable(20, 10)
# print(t.__dict__)
# print(t.square_table())
#
# t2 = RectTable(20)
# print(t2.__dict__)
# print(t2.square_table())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.square_table())


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print('Переместил шахматную фигуру 1')
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Переместил шахматную фигуру')
#         pass
#
#
# q = Queen()
# q.draw()
# q.move()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")  # это будет значение self.value, к примеру 10
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub  # умножаем значение на курс: 741.60
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")  # будет из 2-х строк одна: 10 USD
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EURO"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]  # список экземпляров класса
# print('=' * 20)
# for elem in d:
#     elem.print_value()  # 10 USD
#     print(f"= {elem.convert_to_rub():.2f} RUB")  # = 741.60 RUB
#
# d1 = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('=' * 20)
# for elem in d1:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")

# доделать +
# интерфейсы
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display(self):
#         print("Дочерний класс")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Внучатый класс")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display()


# Вложенные класы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print("Я - метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Я связующий метод")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):  # из внутреннего во внешний
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я метод вложенного класса", MyOuter.age, self.obj.name)
#             # MyOuter.outer_class_method()
#             # self.obj.outer_obj_method()
#             # self.inner_name.outer_obj_method()  # так не работает
#
#
# out = MyOuter('Внешний')
# # inner = out.MyInner("Внутренний", out)
# inner = out.MyInner('a', out)
# # print(inner.inner_name)
# inner.inner_method()
#
# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()  # из внешнего во внутренний
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light green'
#             self.code = '024avc'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Code:', self.code)
#
#
# outer = Color()
# outer.show()
#
# g = outer.lg
# g.display()
# print(g.name)
# g.name = 'Red'  # = outer.lg.name
# print(g.name)
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.nb = self.Notebook()
#
#     def show(self):
#         print(self.name, '=>', self.nb.printer())
#
#     class Notebook:
#         def __init__(self):
#             self.firm = 'HP'
#             self.model = 'I7'
#             self.option = '16'
#
#         def printer(self):
#             return f"{self.firm}. {self.model}. {self.option}"
#
#
# p = Student("Roman")
# p1 = Student("Vladimir")
# p.show()
# p1.show()


# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# d2 = outer.head
# d2.display()

# 29.12.2022

# class Computer:
#     def __init__(self, name, oc1, brand):
#         self.name = name
#         # self.os = self.OS(title='Windows')
#         # self.os = self.OS(title=name)
#         self.os = self.OS(oc1)
#         self.cpu = self.CPU(brand)
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def __init__(self, brand):
#             self.brand = brand
#
#         def make(self):
#             return self.brand
#
#         def model(self, model1):
#             return model1
#
#
# comp = Computer('PC 001', 'Windows-7', 'Intel')
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model('Core-i7'))
# print(my_cpu.model('Core-i5'))


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#         # print('ABC')
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
# print('----')
# b = a.db
# # b = Subclass.Inner()
# b.display1()
# print('===')
# b.display2()

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping' + ' =' + ' спит')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing' + " =" + " играет")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking' + " =" + " лает")
#
#
# beast = Dog('Buddy')
# beast.bark()
# beast.play()
# beast.sleep()


# class A:
#     def __init__(self):
#         print('A')
#
#
# class AA:
#     pass


# class B(A):
#     # def __init__(self):
#     #     print('B')
#
#     def hi(self):
#         print('B_hi')
#
#
# class C(AA):
#     # def __init__(self):
#     #     print('C')
#
#     def hi(self):
#         print('C_hi')
#
#
# class D(C, B):
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)  # если не супер, то имя нужного класса и селф
#     #     # super().__init__()
#     #     print('D')
#     def hi(self):
#         C.hi(self)
#         print('D_hi')
#
#
# d = D()
# d.hi()
# print(D.mro())  # метод "эм-эр-о" показывает иерархию классов
# print(D.__mro__)  # то же самое


# class B:
#     def hi(self):
#         print('B_hi')
#
#
# class C:
#     def hi(self):
#         print('C_hi')
#
#
# class D(C, B):
#     def hi(self):
#         C.hi(self)
#         print('D_hi')
#
#
# d = D()
# d.hi()
# print(D.mro())  # метод "эм-эр-о" показывает иерархию классов

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep, color, width=1):  # можно одни переменные
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.__mro__)
# print(Point.__mro__)

# Миксин (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LongerMixin:
#     def log(self, massage, filename='logfile.txt'):
#         with open(filename, 'a') as fh:  # открывает имя файла в режиме дозаписи "а" в виде <fh>
#             fh.write(massage)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LongerMixin, Displayer):
#     def log(self, massage, filename=''):
#         super().log(massage, filename='subclasslog.txt')
#
#
# sub = MySubClass()
# sub.display('Строка будет отображаться в файле.  ')

# class Ecl:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#
# ex = Ecl()
# print(hasattr(ex, 'b'))
# print(hasattr(ex, 'a'))
# print(hasattr(Ecl, 'b'))
# print(hasattr(Ecl, 'a'))

# try:
#     i = int('Hello !')
# except Exception as e:
#     print(e)
#     print(e.__str__())

# def printExcTree(thisclass, nest=0):
#     if nest > 1:
#         print('  |' * (nest - 1), end='')
#     if nest > 0:
#         print('  +---', end='')
#     print(thisclass.__name__)
#
#     for subclass in thisclass.__subclasses__():
#         printExcTree(subclass, nest + 1)
#
# printExcTree(BaseException)

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()  # инициализатор из MixinLog
#         print('Init Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight} кг, {self.price} руб')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init MixinLog')
#         # self.ID += 1
#         MixinLog.ID += 1  # так будет прибавлять к любому экземпляру
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()

# Перезагрузка операторов

# 24 * 60 * 60 = 86400
#
# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('секунда - целое число')
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'  # get_form это стат.метод
#         # return f'{h}:{m}:{s} '  # первая запись
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен типом Clock")
#         return Clock(self.sec % other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __eq__(self, other):
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec  # то же самое, но короче
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         return self.sec >= other.sec
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c1 += c2
# print(c1.get_format_time())
# if c1 == c2:
#     print("время одно")
# else:
#     print("время разное")

# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('индекс - целое неотрицательное число')
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # если ключ > длины строки
#             self.marks.extend([None] * off)  # вместо None может быть 0, или что-то другое
#         self.marks[key] = value  # сначала добавили все None, и последний None заменили на value
#
#     def __delitem__(self, key):  # для удаления по индексу
#         if not isinstance(key, int):
#             raise TypeError('индекс это - целое число')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', [5, 5, 3, 4, 5])
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

#
# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('ключ => строка')
#
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         elif item == 'min':
#             return (self.sec // 60) % 60
#         elif item == 'sec':
#             return self.sec % 60
#
#         return 'неверный ключ'
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError('ключ => строка')
#
#         if not isinstance(value, int):
#             raise ValueError('значение => число')
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600  # всё в сек. т.к. как в экземпляр передаются секунды
#         elif key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1['hour'] = 10
# c1['min'] = 20
# print(c1['hour'], ':', c1['min1'], ":", c1['sec'], sep='')
# print(c1['hour'], c1['min'],  c1['sec'])
# print(c1.get_format_time())


import random


class Dog:
    a = ['m', 'f']
    s = random.choice(a)
    b = int(random.choice([x for x in range(6)]))

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        if sex == 'm':
            print(f'{self.name} is good boy')
        elif sex == 'f':
            print(f'{self.name} is good girl')
        else:
            print('Определитесь с полом собаки')

    def check(self, name, age, sex):
        if not isinstance(name, str):
            print('Имя должно быть строкой')

        if not isinstance(age, float):
            print('возраст - это число')

        if not isinstance(sex, str):
            print('Пол собаки определяется строкой')

        if self.sex == sex:
            print('У них не может быть щенков')
        else:
            sob = str((Dog(name='No name', age=0, sex=self.s))) * self.b
            return sob

    # def __str__(self):
    #     return

    def __add__(self, other):
        if not isinstance(other, Dog):
            print('должны быть экземпляры класса')
        else:
            return Dog(name="No name", age=0, sex=self.s)


d1 = Dog('Archi', 3, 'm')
d2 = Dog('Dezzi', 5, 'f')
d3 = d1 + d2

print(d3.check)

# +++++++++++++++++++++++++++++++++ Полиморфизм +++++++++++++++++++++++++++++++

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
# if isinstance(g, Rectangle):  # что бы не добавлять тре-ник, сделаем одно название методов
#     print(g.get_per_rect(), end=' ')
# else:
#     print(g.get_per_sq(), end=' ')


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('Python')
# print(t1.total('35'))
# print(t2.total(35))

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}. ')
#
#     def zv(self):
#         print(f'Я {self.name} и я лаю: гав-гав')
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кошка. Меня зовут {self.name}. Мой возраст {self.age}. ')
#
#     def zv(self):
#         print(f'Я {self.name} и я мяукаю: мяу-мяу')
#
#
# d = Dog('Бобик', 4)
# c = Cat('Мурка', 2)
# animals = [d, c]
# for i in animals:
#     i.info()
#     i.zv()


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print("\n", self.surname, self.name, self.age, end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, v1, group, ball):
#         self.v1 = v1
#         self.group = group
#         self.ball = ball
#         super().__init__(surname, name, age)
#
#     def info(self):
#         super().info()
#         print(self.v1, self.group, self.ball, end=' ')
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, sub, rating):
#         self.sub = sub
#         self.rating = rating
#         super().__init__(surname, name, age)
#
#     def info(self):
#         super().info()
#         print(self.sub, self.rating, end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, v1, group, ball, top):
#         self.top = top
#         super().__init__(surname, name, age, v1, group, ball)
#
#     def info(self):
#         super().info()
#         print(self.top, end=' ')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):  # работает почти как __str__, но почти
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return (f'{self.name} ') * 3
#
#
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):  # вычисляет длину списка, объекта и др.
#         return len(self.__coord)
#
#
# p = Point(5, 7, 8)
# print(len(p))

# import math
#
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')  # разрешает иметь только это количество аргументов
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)  # sqrt это квадратный корень.Здесь length-метод
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(1, 2)
# # p.z = 3
# print(p.length)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())
# # Если нет __slots__, то к классу можно добавлять сколько угодно свойств
# # и занимает почти в 4 раза больше памяти, чем со __slots__
# # так как у __slots__ отсутствует __dict__


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',  # запятая показывает что это кортеж
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# # print(pt3.__dict__)

# Функторы -=-=--=-=-=-=-==-=-=-==-=-=-=-=-=-===-=-==-=---=-=-=-=-=-

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c2 = Counter()
# c1()
# c2()
# c1()
# c1()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):  # функтор
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return args[0].strip(self.__chars)  # удаляем символы слева и справа
#
#
# s1 = StripChars("?:!.; ")  # набор символов, которые будем убирать из строки
# print(s1('Hello World!'))
#
#
# def strip_chars(chars):
#     def wrap(*args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент это строка')
#
#         return args[0].strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars("?:!.; ")
# print(s2(" !?:Hello World!; "))

# for i in range(9):
#     print(' ' * (9 - 1 - i) + "*" * (1 + i * 2))

#   def draw_line(self):
# #         raise NotImplementedError("В дочернем классе должен быть определён метод draw() ")


# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     def perimetr(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод perimetr() ")
#
#     def area(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод area() ")
#
#     def drawing(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод drawing() ")
#
#     def print_info(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метод print_info() ")
#
#
# class Square(Shape):
#     def __init__(self, color, side):
#         self.side = side
#         super().__init__(color)
#
#     def perimetr(self):
#         return 4 * self.side
#
#     def area(self):
#         return self.side ** 2
#
#     def print_info(self):
#         print(f"Сторона: {self.side} единиц \nЦвет: {self.color}"
#               f" \nПлощадь: {Square.area(self)} единиц ^2\n"
#               f"Периметр: {Square.perimetr(self)} единиц\nВид фигуры:")
#
#     def drawing(self):
#         for i in range(self.side):
#             print('*' * self.side)
#
#
# class Rectangle(Shape):
#     def __init__(self, color, side1, side2):
#         self.side1 = side1
#         self.side2 = side2
#         super().__init__(color)
#
#     def perimetr(self):
#         return 2 * (self.side1 + self.side2)
#
#     def area(self):
#         return self.side1 * self.side2
#
#     def print_info(self):
#         print(f"\nПрямоугольник\nСторона 1: {self.side1} единиц \nСторона 2: {self.side2} единиц\n"
#               f"Цвет: {self.color} \n"
#               f"Площадь: {Rectangle.area(self)} единиц ^2\n"
#               f"Периметр: {Rectangle.perimetr(self)} единиц\nВид фигуры:")
#
#     def drawing(self):
#         for j in range(self.side1):
#             print('*' * self.side2)
#
#
# class Triangle(Shape):
#     def __init__(self, color, s1, s2, s3):
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#         super().__init__(color)
#
#     def perimetr(self):
#         return self.s1 + self.s2 + self.s3
#
#     def area(self):
#         p = (self.s1 + self.s2 + self.s3) / 2
#         return (p * (p - self.s1) * (p - self.s2) * (p - self.s3)) ** 1 / 2
#
#     def print_info(self):
#         print(f"\nТреугольник\nСторона 1: {self.s1} единиц \n"
#               f"Сторона 2: {self.s2} единиц\nСторона 3: {self.s3} единиц\n"
#               f"Цвет: {self.color} \n"
#               f"Площадь: {Triangle.area(self)} единиц ^2\n"
#               f"Периметр: {Triangle.perimetr(self)} единиц\nВид фигуры")
#
#     def drawing(self):
#         for k in range(self.s2):
#             print(' ' * (self.s1 - 1 - k) + '*' * (1 + k * 2))
#
#
# sq = Square('red', 3)
# re = Rectangle('green', 3, 7)
# tr = Triangle('blue', 11, 6, 6)
# kop = (sq, re, tr)
# for i in kop:
#     i.print_info()
#     i.drawing()
