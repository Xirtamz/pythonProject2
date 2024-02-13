# years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
#
# for year in years_list:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print(year, 'Yes')
#         print(f'{"YES"}')
#     else:
#         print(year, 'No')

# var1 = True
# var2 = False
# var3 = True
# if var1 and var2 or var1 and var3 or var3 and var2:
#     print('True')

# user_input = input('Enter some text: ')
# unique = True
# for letter in user_input:
#     if user_input.count(letter) > 1:
#         unique = False
# if unique:
#     print('String has unique charecters only')
# else:
#     print('No unique')

# user_input = input('Enter some text: ')
# unique = True
# for letter in user_input:
#     if user_input.count(letter) > 1:
#         print('There are non uniq')
#         break
#     else:
#         print(letter, 'Is unique')
#

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ["name", "salary"]
#
# for key in keys:
#   if key in sample_dict:
#     del sample_dict[key]
# print(sample_dict)

# d = {'names': [], 'ages': []}
# s = {14, 27, 'Michel', 22, 'Helen', 'Adam', 48, 'Irma', 'Stefan', 19}
#
# for value in s:
#     if type(value) == str:
#         d['names'].append(value)            # gde d eto slovar
#     elif type (value) == int:
#         d['ages'].append(value)
#     else:
#         print('Dunno')
# print(d)

# x = {
#     'name': 'Jack',
#     'contacts': {
#         'emails': [
#             'jack@xample.com',
#             'John@company.com'
#         ],
#     },
#     'info': ['Brown eyes', '128cm tall', '80kg weight']
# }
#
# print(x['contacts']['emails'])
