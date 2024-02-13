# 'r' - read
# 'w' - write
# 'x' - create
# 'a' - append
# 'r+' - read/write

# C:\Users\xirta\PycharmProjects\pythonProject2\simple_data_types\text_files\lorem.txt
# Absolute path

# simple_data_types/text_files/lorem.txt
#Relative path
# ../ - vqxod nazad po directorii


# file = open('text_files/lorem.txt', 'r',  encoding='utf8')
# # cp1257 - estonian language
# # print(file)
# # <_io.TextIOWrapper name='text_files/lorem.txt' mode='r' encoding='utf8'>
#
# print(file.closed)
# file.close()
# print(file.closed)


# with open('text_files/lorem.txt', 'r',  encoding='utf8') as file:           # works inside a funktion
# #     print(file.closed)
# print(file.closed)
#     data = file.read(10)                                                          # returns a string
#     data2 = file.read(10)                                                      # second time reads
#     data = file.read()                                                       # in bracets till index number
    # file.seek(0)                                                           # starts with index
    # data2 = file.read()
# print(type(data))
# print(data)                                                                 #opens file
# print(data2)                                                                # cant open 2 times
# #     data = file.readlines()                                                 # returns list
#     data = file.readline(11)
#     # data2 = file.readline()                                                     # returns a list () - wich line /n
#     file.write('Hello World!')
# print(data)
#

# with open('text_files/temp.txt', 'w', encoding='utf8') as file:
    # file.write('Hello World\n')
    # file.seek(0)
    # file.write('***')

# print(r'\t\n')                                                                          # *r* ignores any \n \t etc

# with open('text_files/temp.txt', 'w', encoding='utf8') as file:
#     data = file.read()
# with open('text_files/temp.txt', 'w', encoding='utf8') as file:
#     file.write(data.upper())

# with open('text_files/_117310488_16.jpg', 'rb') as file:                            #open jpg
#     with open('python_copy.png', 'wb') as wfile:
#         chunk_size = 4096
#         data = file.read(chunk_size)
#         while len(data) > 0:
#             wfile.write(data)


