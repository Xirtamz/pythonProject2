string1 = "Hello bro"
string2 = "jack Is MY NAME"
string3 = "%-*Get rid of *junk* please*-L%*"
string4 = "hello my name is jack"
string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."



print(string1.replace('bro', 'Hero'))
print(string2.capitalize())
print(string3.strip('%-L*').replace("*", ''))
print(string4.capitalize().replace('jack', 'Jack'))
print(string5.lower().count('estonia'))


var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
f_string = f'{var2} {var3} {var1}'
print(f_string.replace("'", ""))
print(f'{var2.capitalize()} {var3.lower()} {var1.capitalize()}')
byte_string = b"\316\273"
string = str(byte_string, encoding='utf-8')
print(byte_string.decode())
print(byte_string.decode('uft16'))