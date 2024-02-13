# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# age = input("Enter your age: ")
# print(f'Hello, {name.title()} {surname.title()}. Your age is: {age}')

# a = 3
# b = 4
# c = (a ** 2 + b ** 2) ** 0.5
# print(c)


# a = float(input('Katet1: '))
# b = float(input('Katet2: '))
# c = float(input('Gipotenu: '))
#
# if (a*a + b*b == c*c):
#     print("right triangle")
# else:
#     print("NOT right")


# list1 = input('ANYTHING: ').split(" ")
# for value in list1[::-1]:
#     print(value)

#
# t1 = (1, 2, 3, 5, 8)
# t2 = (8, 2, 5)
# # a = t1[:2] + t2 + t1[:2]
# # print(a)
#
# t1 = list(t1)
# for num in t2[::-1]:
#     t1.insert(2, num)
# a = tuple(t1)
# print(t1)


test = [1, 2, 3, 4, 7, 9, 9, 1, 2, 4, 6, 4, 6]
# max_count = 0
# result = []
# for num in test:
#     if test.count(num) > max_count:
#         max_count = test.count(num)
#         print(result)
# for num in test:
#     if test.count(num) == max_count:
#         result.append(num)
# result = list(set(result))
# print(result)
    # if test.count(num) > 1:
    #     print(num)
    #


# counts = {}
# result = []
# for num in test:
#     counts[num] = test.count(num)
# # print(counts)
# for key in counts:
#     if counts[key] == max(counts.values()):
#         if key not in result:
#             result.append(key)
# print(result)                                       #vqvodit max 4islo elementov
# print(counts.keys())
# print(counts.values())
# print(counts.items())

# seconds = 1234565
# days = seconds // (24 * 60 * 60)
# seconds %= 24 * 60 * 60
# hours = seconds // (60 * 60)
# seconds %= 60 * 60
# minutes = seconds // 60
# seconds %= 60
#
# print(f'{days}:{hours}:{minutes}:{seconds}')
