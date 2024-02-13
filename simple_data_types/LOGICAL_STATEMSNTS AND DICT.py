                                                                                                #COMPARISON OPERATORS
# a = 7
# b = 10
# # print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)                               # strogoe ravno
# print(a != b)                               # ne ravno
# print(1 < 3 < 7 < 9)
# print(0 <= a <= 10)


                                                                                                #COMPARISOSN OF STRINGS
# print('a' < 'b')
# print('a' > 'A')
# print(ord('a'))                             #polu4it decimal number
# print(chr(97))                              # naoborot

# print('apple' == 'apple')
# print('applea' > 'apple')
# print('applea' > 'appleb')                  # sravnivaet po o4eredi

                                                                                                        #AND, OR, NOT
                                        #AND
# print(True and True)
# print(False and False)
# print(10 > 5 and 'hello'.isalpha())

                                        #OR
# print(True or True)
# print(True or False)
# print(False or False)
# print(10 > 5 or 'hello'.isalpha())

                                        #NOT
# print(not True)
# print(not False)
# print(not 5 > 6)
# print(not [])
# print(not (not 5) > (not 6))

# code = '39005090241'
#
# print(len(code) == 11 and 1 <= int(code[0]) <= 6 and 1 <= int(code[3:5]) <= 12 and (1 <= int(code[0]) <= 4 and
# int(code[1:3]) <= 99 or 1 <= int(code[0]) <= 5 and int(code[1:3]) <= 99))

                                                                                            #IF, ELIF,ELSE STATEMENTS

# code = '12345678910'
# if len(code) == 11:
#     print('Your id is:', code)
# elif len(code) < 11:
#     print('Your id is too short')
# else:
#     print('Your id is too long')

# code = '12345678910'
# if len(code) == 11:
#      print('Your id is:', code)
# if len(code) < 11:
#      print('Your id is too short')
# if len(code) > 11:
#      print('Your id is too long')

# rng = range(1, 16)
# result = []
# for num in rng:
#     if num % 2 == 0:
#         result.append(num ** 2)
#     elif num % 3 == 0:
#         result.append(num ** 3)
# print(result)
#
#         result.append(num ** 2)
#     if num % 3 == 0:
#         result.append(num ** 3)
# print(result)

age = int(input('Please enter your age: '))
# if 0 < age <= 12:
#     print('You are a child')
# elif 12 < age <= 18:
#     print('You are teen')
# elif 18 < age <= 65:
#     print('You are an adult')
# else:
#     print('you are a grand pa')
#

# code = '12345678910'
# if len(code) != 11:
#     if len(code) > 11:
#         print('Too long')
#     else:
#         print('Too short')
# else:
#     print('OK!')

# x = 9
# print('X more than 7') if x > 7 else print('X Less or equal to 7')

                                                                                                            #IN, NOT IN
# lst = [1, 2, 3, 4, 5, 'a', 'b', 'c']
# print(3 in lst)
# print(10 in lst)
# print(10 not in lst)
# print('ll' in 'Hello')
# print(5 in {2, 7, 9, 5})


                                                                                                            #IS, IS NOT
# x = 10
# y = 10
# print(x == y)   #ravenstvo peremennqx
# print(x is y)   #ravenstvo objektov
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)
# print(lst1 is lst2)
# print(lst1[0] is lst2[0])
# print(lst1 is not lst2)
# n = None
# print(n is None)


                                                                                                            #ANY, ALL
# lst = [-2, -1, 0, 1, 2]
# print(any(lst))
# print(all(lst))
# lst.remove(0)
# print(all(lst))


                            # number from 1 to 100
#if number % 3 == 0 - print number and FIZZ
#if number % 5 == 0 - print nember and BUZZ
#if number % 3 == 0 and % 5 == 0 - print and FIZZBUZZ

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FIZZBUZZ')
#     elif num % 3 == 0:
#         print(num, 'FIZZ')
#     else:
#         print(num, 'BUZZ')


# list1 = [5, 10, 15, 20, 25, 50, 20, 500, 900, 20, 31, 41, 20]
# for i in range(len(list1)):
#     if list1[i] == 20:
#         list1[i] = 200
# print(list1)

# string = 'she sells seashells be the seashore'
# for i in range(len(string)):
#     if string[i] == 's':
#         print(i, end=' ')


