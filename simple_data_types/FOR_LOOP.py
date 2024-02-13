                                                                                                                #RANGE
# r = range(10)    # ot 0 do 9 vklu4aet v sebja
# print(r)
# print(*r)       # * eto universalnii operator raspokovki i upakovki
# print(*[1, 2, 3, 4, 5])     #delit na elementq
# lst = [*range(11)]
# print(lst)
# print(*range(-5, 6))
# print(*range(-10, 11, 2))   # s wagom, mozno i -wag( -1)
# lst = list(range(10))
# print(lst)


                                                                                                            #FOR LOOP
for num in range(1, 10):        # idet po o4eredi i po krugu      1, 2, 3, i td
    num **= 2           # num = num ** 2         # vozvodit v kvadrat vse objektq
    print(num)

# string = 'Hello World!'
# lst = []
#
# for ch in string:
#     lst.append(ch.encode('utf32'))
# print(lst)                                  # vqdaet vse bitq bukv
#
# text = ''
# for el in lst:
#     text = text +el.decode('utf32').upper()  #iz baitov v znaki perevodit
# print(text)

# courses = ['Math', 'Art', 'English', 'Physics', 'History']
# names = ['Remy', 'Bonja', 'Sam', 'Andrew']
# grades = ['A+', 'A', 'B', 'C']
#
# for course in courses:          #idet sna4ala
#     for name in names:          #tretij
#         for grade in grades:    #vtoroj
#             print(f'{name} got{grade} in {course} yesterday') #vse vozmoznqe variacii
#
# lst = ['A', 'B', 'C', 'D', 'E']
# for i in range(len(lst)):
#     print('Element', lst[i], 'has an index', i)