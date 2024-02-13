                                                                                                            # FUNCTIONS

# name = 'Jack'                                 # tak ne delat. nazqvat peremennuju i funkcuiju

# def say_hello(name, surname):
#     print(f'Hello, {name} {surname}!')
# #
# #
# # # say_hello('Remy', 'Sorokin')
# # print(say_hello('Jack', 'Pechkin'))
#
#
# def rectangle_area(a, b):
#     result = a * b
#     return result
#
#
# print((rectangle_area(60, 100) * 200) / 10000)


# print(rectangle_area(60, 70))
# area = rectangle_area(80, 90)
# print(area)
#
# def add_person(name):
#     people.append(name)
#
#
#
# people = []
# add_person('Bob')
# add_person('Roby')
# add_person('Mary')
#
# print(people)


# odds = []
# evens = []
#
#
# def sort_numbers(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)
#
# sort_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(odds)
# print(evens)


# odds = []
# evens = []
#
#
# def sort_numbers(num):
#
#     if num % 2 == 0:
#         return 'EVEN'
#     else:
#         return 'ODD'                                              # return ostanavlivaet funkciju
#     print('DONE')                                               #NE DOIDEM DAZE
#
#
# print(sort_numbers(10))


# def sum_three_or_two(a, b, c=100):                          # gde C=100 default meaning and goes to the end
#     return a + b + c
#
#
# print(sum_three_or_two(10, 20, 30))


# def say_hello(name=None, surname=None):
#     if name and surname:
#         print(f'Hello, {name} {surname}!')
#     elif name and not surname:
#         print(f"hello {name}")
#     elif not name and surname:
#         print(f'Hello mr/ms {surname}!')
#     else:
#         print(f'Hello stranger!')
#
#
# say_hello(surname='Sorokin', name='Remy')


# def many_arguments(a, b, c=100, *args, **kwargs):
#     # print(args)
#     for arg in args:
#         print(arg)                # arguments - tuple []
#     print(kwargs)                 # kwargs - dictionary {}
#
#
# many_arguments(10, 20, 1, 'asd', [1,2,3], 123, name='Jack', surname='Smith')


# x = [1, 2, 3]
# y = [0, *x, 4, 5, 6]                                                              # where *x objedenaet elementq
# print(y)


# a, b, c = 10, 20, 30
#
# def tester():
#     global a, b                                                                     # beret globalno
#     a = 1
#     b = 2
#
#     print(a, b, c)                                                                  # vidit togze globalno, tk
#
# tester()
# print(a, b, c)
#

# import my_functions                               #importiruet from another file
# print(my_functions.double(10))
# print(my_functions.triple(20))
# print(my_functions.name)

# from my_functions import triple, name               # imports only separate functions
# print(triple(10))
# print(name)


# def wrapper(func):
#     print('Start')
#     func()
#     print('End')
#
# def say_hello():
#     print('Hello world')
#
# wrapper(say_hello)
# print(say_hello)
#
# x = say_hello
# x()