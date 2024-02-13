# string1 = 'Hello world'
# string2 = 'stArts with loWer leTTER'
# string3 = '$$$string with dollars$$$$'

# # String operations

# print(string1 + ' ' + string2)
# print(string1 * 3)              # odnu komandu 3 raza povtorjaet
# print((string1 + string2) * 2)


# Escape characters

# print(' I don\'t know')         # kommanda \ sledujuwii simvol ne javlaetsa sluzebnqm simvolom
# text = '\'\'\''
# print(text)
# #Vidq ekranirovanija
#
# print('Hello\nWorld')           # \n dla perenosa stroki
# print('First line', end='\n\n') # dva raza propuskaet stroku
# print('second line')


#Indexing and slicing

# print(len(string1))                # len - dlinna
# print(string1[0])                   # [0] dla vqzova pervogo zna4enija
# print(string1[-1])                  # [-1] s konca s4et
# print(string1[1:5])                 # [1:5] ot i do, gde poslednij ne vklu4aetsa
# print(string1[1:3] + string1[4:6])
# print(string1[:4])                  # :4 s na4ala i do...
# print(string1[:4] + string1[4:])
# print(string1[-4:])
# print(string1[4:-2])
# print(string1[-5:-2])
# print(string2[1:-1:3])              # gde :3 eto wag, kazdqj 3 simvol
# print(string2[4:-5:2])
# print(string2[::4])                 # gde :: vsa celikom s wagom v 4
# print(string2[::-1])                # gde -1 razvorot stroki s wagom
# print(string2[-1:-5:-1])            # s4itaet s konca
# print(string2[:3] + string3[:-4:-1])    # 4ast s na4ala i 4ast s konca


# #String methods

# print(string2.upper())              # .upper vse s zaglavnoj
# print(string2.lower())              # .lower vse s malenkoj
# print(string2[4:14].lower())        # ot i do malenkimi
# print(string2.casefold())           # .casefold vse stroki melkimi
# print(string2.capitalize())         # .capitalize pervaja bukva stroki budet zaglavnoi
# print(string2.title())              # .title pervaja bukva kazdogo slova zaglavnaja
# print(string2.swapcase())           # .swapcase menjaet zaglavnqe na malenkie i naoborot


# Find and Count

# print(string1.count('l'))           # .count s4itaet kol-vo 4ego-libo
# print(string1.count('l', 2, 6))   # mezdu 4em
# print(string1.find('l', 3))            # index, gde vstre4aetsa pervoe zna4enie( index pervogo vxozdenija
# print(string1.find('l', 4))         # s kakogo na4at s4itat
# print(string1.find('x'))                        # net ego i vqdaet -1
# print(string1.index('w'))                   #.index kak alternativa k .find no vqdaet error
# print(string1.index('x'))                   # nelza, owibka
# print(string1.startswith('He'))             # s 4ego na4inaetsa
# print(string1.endswith('ld'))             # zakan4ivaetsa


#CLEANING

# print(string3.strip('$'))               # udalaet simvol sleva i sprava
# print(string3.rstrip('$'))              # sprava 4istit .lstrip- sleva
# print(string3.strip())                  # 4istit probelq
# print('-*A&.*Hello --- world- *&&&*'.strip('&-A&.'))        # 4istit kazdqj simvol
# print(string1.replace('world', 'planet'))
# print(string1.replace('l', ''))     # zamena
# print('-*A&.*Hello --- world- *&&&*'.strip('-A&.').replace('*', '').replace('-', '')
#       .replace(' ', '', 1))


#IS METHODS

# print(string1.isalpha())                # proverka
# print(string1.isascii())
# print('23151'.isdigit())                # proverka cifr


#FORMAT

# text = 'This model of %s has max speed %s km/h' %('Toyota', 200) # gde %s peremennaja - old style
# print(text)


#FORMAT METHOD

# text = 'My name is {}. I am {} years old. My salary is {} dollars.'     # gde {} place holders
# print(text.format('Remy', '33', 'none'))        # po porjadku
#
# text = 'My name is {1}. I am {2} years old. My salary is {3} dollars.'      # cifrq - porjadok
# print(text.format('Remy', 33, 2000))
#
# text = 'My name is {name}. I am {age} years old. My salary is {salary} dollars.'
# print(text.format(salary=2314, name='Bob', age=33))

# x = 'Remy'
# y = '42'
# z = 10000
# print(text.format(salary=z, name=x, age=y))

# text = 'My name is {name}. I am {age} years old. My salary is {salary:,} dollars.' # v konce "salary:,"4erez zapjatuju
# print(text.format(name='Musk', age=50, salary=2312455))


# F-STRING

# name = 'Andrew'
# total = 21
# height = 186
# f_string = f'There are {total} students in the class. The highest is {name}. His height is {height}'
# print(f_string)

# leg1 = 4
# leg2 = 7
# triangle_str = (f'The square of Hypotenuse of the triangle with the legs: {leg1} and {leg2}'
#                 f' cm equals: {leg1**2 + leg2**2}')
# print(triangle_str)


# BYTE STRING

# print(string1)
# print(string1.encode())
# b = string1.encode()
# print(type(b))
# print(b.decode())
# byte_string = string1.encode('utf32')
# print(byte_string)
# print(byte_string.decode('utf32'))
#
# import charset_normalizer
# print(charset_normalizer.detct(byte_string))


string1 = "Hello bro"
string2 = "jack Is MY NAME"
string3 = "%-*Get rid of *junk* please*-L%*"
string4 = "hello my name is jack"
string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."


print(string1.replace('bro', 'Hero'))
print(string2.capitalize())
print(string3.strip('%-L*').replace("*", ''.replace(' ','', 1)))
print(string4.capitalize().replace('jack', 'Jack'))
print(string5.lower().count('estonia'))


var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
f_string = f'{var2.lower()}, {var3.upper()}, {var1.capitalize()}'
print(f_string)

byte_string = b"\316\273"
string = str(byte_string, encoding='utf-8')
print(string)