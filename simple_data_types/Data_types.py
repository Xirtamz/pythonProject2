# # integer
# print(100)
# print(type(100))
#
# # float
# print(100.123)
# print(type(100.123))  # drobi
#
# # complex
# print(100j)
# print(type(100j))
#
# # string
# print('Hello "World"')
# print(type(''))  # stroka prosto
# print("how's your day'z")  # stroka
# print('''howdy''')  # multiline
# print("""he he
# prikolno""")  # multiline
#
# # none object
# print(None)
# print(type(None))
#
# # Boolean
# print(True, False)  # logika
# print(type(True))
#
# print(bool(12345))
#
# # ALWAYS FALSE
# print(bool(0), bool(''), bool(None), bool([]), bool(False), bool({}))  # pustqe
# print(bool(1.21314), bool('False'))  # vse ne pustoe

# Legal variable names:  -- peremennqe
myvar = 123
my_new_var = 1234 # snake case
myNewVar = 321 # camel case
_my_var = 'hi'
MYVAR = 1233 # dla konstant tipo menjat nelza
my1var2 = 'my man'
Myvar = 1000  # nazvanie klassov

# illegal var_names
# 1var = 123
# my-var = 1231
# my var = 2311

# # Arithmetics operator
# print(10 / 3)
# print(10 % 3)  # ostatok posle delenija na celqe
#
# # Floor devision
# print(10 // 2)
# print(11 // 2)  # sk mozno raz podelit
# print(11 / 2)  # float
#
# print(3 ** 2)  # stepen
# print(9 ** (1/2))  # koren kv
# print(8 ** (1/3))  # koren kub

# Assignment operators
# x = 5
# y = 2
# print(x ** y)

# x = 5  # vse po porjadku
# x = x + 5
# print(x)
#
# y = 5
# y += 5  # spkrawennqj varik "x = x + 5"
# print(y)

# # DATA TYPE CONVERSION
# print(1 + True + 2.5 + 3j + int('100'))  # int celoe 4islo
# print(float('10001'))  # drobi
#
# print(str(1000))
# print(str(print))
# print(str(bool))

# string concat
# print('Hello' + ' ' + 'world')

# print(1, 10021.2, None, False, 'string' + ' another string')

# print('word1', 'word2', 'word3', sep='***')  # kakie probelq
# print('word1', 'word2', 'word3', sep='&&&', end='***')  # kakoi konec
# print('Next print')

# Input
# num = input()
# print('Your input is', num)

# num = int(input('Please enter your num: '))
# print('your num is power of 3:', num ** 3)

your_year = float(input('Enter your Year of birth: '))
name = input('Entr your name: ')
age = int(2024 - your_year)
x = 152
y = 132
code_1 = '354'
code_2 = int(((x % y) * 13) ** 0.5)
code_3 = 132
print('Hello', name, '. You are ', age, ' years old.', 'Your secret code is', end=' ')
print(code_1, code_2, code_3, sep='-')
