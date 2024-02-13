x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
# print(a, b)


# def odd(num):
#     if num % 2 == 0:
#         return False
#     return True
#
#
# y = filter(odd, x)
# print(list(y))

people = [
    {
        'name': 'Jack',
        'age': 15,
    },
    {
        'name': 'bob',
        'age': 21,
    },
    {
        'name': 'Kate',
        'age': 61,
    },
]


# def is_adult(person):
#     if person['age'] >= 18:
#         return True
#     return False
#
#
# adults = list(filter(is_adult, people))
# print(adults)


# def squares(num):
#     return {num: num ** 2}
#
#
# squares_lst = list(map(squares, x))
# print(squares_lst)


# def adult_or_teenager(person):
#     new_person = {
#         **person
#     }
#     if person['age'] >= 18:
#         new_person['status'] = 'adult'
#     else:
#         new_person['status'] = 'teen'
#     return new_person
#
#
# people_extended = list(map(adult_or_teenager, people))
# print(people_extended)


# test = lambda: print('Hello')
# print(test)

# res = list(filter(lambda num: num % 2 != 0, x))
# print(res)
