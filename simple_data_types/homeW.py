# You have given a Python list. Write a code to find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of an item.
# list1 = [5, 10, 15, 20, 25, 50, 20]

# list1[list1.index(20)] = [200]
# print(list1)

# Swap first and last elements in the given list
# lst =['first', 'a', 'b', 'c', 'd', 'last']
#
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)


# Concatenate two lists to get the new one: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# lst1 = ["Hello ", "take "]
# lst2 = ["Dear", "Sir"]
#
# for list in lst1:
#      for list2 in lst2:
#         print(f'{list}{list2}')

# Using for loop calculate the factorial of 11.
# Factorial of 11 (11!) is a product of 1 x 2 x 3 ... x 11

# number = 11
# factorial = 1
# for num in range(number, 0, -1):
#     factorial *= num
#     print(factorial)



# You have a text. Write a program to return a list of words of this text
# cleared of any punctuation, and capitalized.
# text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam consequat molestie sem, eu lacinia nisi hendrerit et. Maecenas risus ex, cursus ac tincidunt eu, porttitor ac diam. Morbi posuere laoreet ante, sed aliquam risus laoreet vel. Donec fringilla sollicitudin metus, quis finibus odio tincidunt quis. In a neque semper, sodales enim bibendum, sodales tellus. Sed eu efficitur metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse placerat tincidunt lectus, id commodo lacus sollicitudin ut. Aliquam sed consectetur sem. Nullam euismod magna vitae augue tristique interdum ac id dui. Nam neque libero, lacinia ut purus.')

# result = []
# for word in text.split():
#     result.append(word.strip('.,;:-?!').capitalize())
#     print(result)

# result = text.title().replace(',','').replace('.', '').replace(';', '').split()
# print(result)

# Add a list of elements to a set
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
#
# part1 = sample_set
# part1.update(sample_list)
# print(part1)

# Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set.intersection(set1, set2)
result = set1.intersection(set2)

print(result)

