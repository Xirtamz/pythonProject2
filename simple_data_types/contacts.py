"""
'name': {'phone': *******, 'e-mail': ******* )
add_contact ( name phone email )
view contact (name)
update contact(name, phone, email )
delete contact (name)
contact_list


"""


# contact_book = {}       #dictionary
#
#
# def add_contact(name, phone, email, **kwargs):
#     if name not in contact_book:
#         contact_book[name] = {'phone': phone, 'email': email}
#         contact_book[name].update(kwargs)
#         print(f'Contact {name} was updated.')
#     else:
#         print(f'Contact {name} already exists')
#
#
# def view_contact(name):
#     if name in contact_book:
#         print(name)
#         for key, value in contact_book[name].items():
#             print(f'\t{key.title()}: {value}')
#     else:
#         print('This contact name does not exist!')
#
#
# def update_contact(name, phone=None, email=None, **kwargs):
#     if name in contact_book:
#         data = {**kwargs}
#         if phone is None:                                       # mozno bez None
#             data['phone'] = phone
#         if email:
#             data['email'] = email
#         contact_book[name].update(data)
#         print(f'Contact {name} was updated!')
#     else:
#         print(f'Contact {name} does not exist.')
#
#
# def delete_contact(name):
#     if name in contact_book:
#         del contact_book[name]
#         print(f'Contact {name} was deleted.')
#     else:
#         print(f'contacts {name} does not exist.')
#
#
# def list_contacts():
#     contact_list = list(contact_book.keys())                  #.keys vqzavaet keys, tak ze mozno values
#     contact_list.sort()
#     contact_list = enumerate(contact_list, 1)
#     for num, name in contact_list:
#         print(f'{num}.{name}')
#
#
# add_contact('Roman', '56925603', 'roman@example.com')
# add_contact('Jack', '56925603', 'roman@example.com')
# add_contact('Mary', '56925603', 'roman@example.com')
# add_contact('Bob', '56925603', 'roman@example.com')
# add_contact('rob', '56925603', 'roman@example.com')
# # print(contact_book)
# # view_contact('Roman')
# list_contacts()                                             #vqzqvaet funkciju