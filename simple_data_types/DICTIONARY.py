# empty_dict = {}
# print(type(empty_dict))

# d = dict(name='Adam', age=40)
# print(d)

# d = {'name': 'Joe', 'age': 30}
# print(d)

# different_dict = {1: 'int_value', 0.5: 'float_value', 'key': 'value', 'container': [1, 2, 3], (10, 20): 'tupple_value'}

employee = dict([('name', 'Sam'), ('age', 32), ('salary', 3000)])
# print(employee)
# print(employee['name'])

# print(employee.get('name'))
# print(employee.get('Lastname', 'No last name found'))

# employee['name'] = 'Maria'
# print(type(employee))
# print(employee)
#
# employee['last name'] = 'Gold'
# print(employee)
#
# name = employee.pop('name')
# print(name)
# print(employee)
#
employee.update({'name': 'Kate', 'telefnation': ' 55529990', 'days of vocation': 32})
# print(employee)

# print(employee.keys())
# print('---'.join(employee.keys()))
# print(list(employee.keys()))
# print(employee.values())

# for key in employee:
#     print(f'{key} has a value {employee[key]}')

for key, value in employee.items():
    print(f'{key} --- {value}')
