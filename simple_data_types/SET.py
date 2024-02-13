# empty_set = set()
# print(type(empty_set))

new_set = set('data')
print(new_set)

set1 = {'Estonia', 'Latvia', 'Litva', 'Poola'}
set2 = {'Estonia', 'Sweden', 'Poola', 'Finland'}    # ne povtorjaet
set1.add('Germany')                               #dobavlaet tolko unikalnqe
print(set2)
#
# # set1.pop()
# # print(set1)                                       #udalaet random
#
# set1.remove('Latvia')
# print(set1)                                       #udalaet konkretno
#
# set1.discard('Poola')
# print(set1)



                                                                                                        #SET OPERATIONS
# print(set1)
# print(set2)
# print(set1.intersection(set2))                  # perese4enie. vozvrawet poxozie elementq
# print(set1.difference(set2))                    #gde, kotorqx net
# print(set1.union(set2))                           #objedinaet, no ne povtoraet
# print(set1 & set2)                                # obwee