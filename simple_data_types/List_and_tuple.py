# empty_list = []
# print(type(empty_list))
#
# empty_list = list()
# print(empty_list)
#
not_empty_list = [100, 1.123, True, 'Howdy', None, ['a, 12, 15']]
# print(not_empty_list)

                                #Broadcasting / list to variables
# var1, var2, var3 = [10, 20, 30]
# print(var1, var2, var3)
# x, y, z = 1, True, 'Howdy'
# print(x, y, z)
# a, b, c = [1000] * 3           #skolko objektov, stolko i peremennqx
# print(a, b, c)
# var1, var2, *var3 = [1, 2, 3, 4, 5]
# print(var1, var2, var3)         # gde* beret v arxiv vse neispolzumqe


                                                                                                         #INDEXING
# print(not_empty_list)
# print(not_empty_list[0])
# print(not_empty_list[-1])
# print(not_empty_list[-1][1])
# print(not_empty_list[:4:2])
# not_empty_list[3] = 'hi'
# print(not_empty_list)

# not_empty_list[1:4] = ['new', 'element']
# print(not_empty_list)
#                                                     # cifrq eto kakoi element brat
# not_empty_list[:3] = ['more', 'than', 3, 'elements']
# print(not_empty_list)

                                                                                                        #LIST METHODS
cities = ['Tallinn', 'London', 'Tokio', 'Paris']
numbers = [1, 4, -7, 12, 8, 17, -11]
        #adding elements
# cities.append('Oslo')       # dobavlaet v konec spiska, .append menjaet original
# print(cities)

# numbers.insert(2, 7)  # dobavlaet. pervaja cifra vqbiraet kakoi objekt
# print(numbers)

# numbers.extend([-9, 1, 0])
# print(numbers)                      #vstavlaet skolko ugodno objektov v konec

# part1 = numbers[:3]
# part1.extend([-9, 1, 0])
# numbers = part1 + numbers[3:]           #dobavit neskolko objektov kuda ugodno
# print(numbers)
#
# numbers.extend('numbers')
# print(numbers)                      #i stroki razbivaet v otdelnqe spiski

# print(cities + numbers)
# print(cities * 2)                   # mozno skladqvat


                                                                                                            #REMOVING
# cities.remove('Paris')
# print(cities)

# cities.pop()                #po defaultu udalaet last element
# print(cities)

# print(cities.pop())         # pokazet 4to udalil

# popped_item = cities.pop()
# print(cities, '\n', popped_item)

# cities.insert(1, cities.pop(2))
# print(cities)                 #menjaet mestami


                                                                                                    #SORTING METHODS
# cities.reverse()
# print(cities)           #perevora4ivaet

# print(numbers)
# numbers.sort()             #sortiruet na uveli4enie
# print(numbers)
# numbers.sort(reverse=True) #sortiruet na ubqvanie
# print(numbers)

# sorted(numbers)
# print(numbers)
# print(sorted(cities))

                                                                                                        #FIND METHODS
# print(cities)
# print(cities.index('Tokio'))  #poisk indexa, kakoi po s4ety
#
# print(cities.count('Paris'))    # kol-vo
# print(numbers.count(1))

                                                                                                     #STRING TO LIST
# text= 'These      elements will be the parts of the list soon!'
# print(text)
# lst = text.split()
# print(lst)
# new_text = ', '.join(lst)  #dobavlaet ", " mezdu elementami
# print(new_text)
# lst = new_text.split(', ')
# print(lst)
# lst = new_text.split(', ', maxsplit=3)      #delit na elimentq max 3, posle vse pod odnu
# print(lst)
# new_text.rsplit(3)                      # toze samoe, tolko sleva na pravo

                                                                                                        #COPY AND CLEAR
# lst.clear()
# print(lst)
#
# lst1 = [1, 2, 3]
# lst2 = lst1
# print(lst1)
# print(lst2)
#
# lst1[0] = 10
# lst2[-1] = -11
# print(lst1)
# print(lst2)
# print(id(lst1))
# print(id(lst2))
#
# lst2 = lst1.copy()                  # kopija lst1, a ne toze samoe
#
# lst2[-1] = -999
# print(lst1)
# print(lst2)
#
#                                                                                                 #STATISTICS FUNCTIONS
# print(numbers)
# print(min(numbers))         #minimalnij nomer
# print(max(numbers))         #max number
# print(sum(numbers))         #summa

#                                                                                                                 #TUPLE
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# # print(t1[1])
# # #t1[1] = 10                   #ne vozmozno menjat
# #
# print(t1 + t2)              # sumiruet, no delaet novqi tuple
