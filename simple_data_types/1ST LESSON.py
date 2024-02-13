                                                                                                                #METODS
# print() # metodq iz skobok

                                                                                                        # WHILE CYCLE
# x = 0
# while x < 101:
#     x += 1
#     print(x ** 2)

# step = 0.65
# current_position = 0
# distance_to_target = float(input('Enter The Distance in m: '))
# total_steps = 0
#
# while current_position < distance_to_target:
#     current_position += step
#     total_steps += 1
# print(total_steps)

                                                                                                            #PROVERKI
# try:
#     user_num = float(input('Enter num: '))
#     # 100 / 0
# except ValueError:
#     print('Not a num!')
# except ZeroDivisionError:
#     print('no division by 0')
# else:
#     print(user_num ** 2)
# finally:
#     print('Good job!')


# for i in range(10):
#     if i == 7:
#         pass
#     else:
#         print(i)
# print('Next')

         #38803160272                                                                              #VALIDATOR ISIKUKOOD
while True:
    user_id = input('Enter your ID: ')
    try:
        int(user_id)
        if len(user_id) != 11:
            raise Exception                                         #samomu owibku vqzvat
    except ValueError:
        print('Code Is Not Numeric, Try Again!')
    except Exception:
        if len(user_id) > 11:
            print('Too Long')
        else:
            print('Too Short')
    else:
        while True:
            user_choise = input('1.Gender\n'
                                '2.Date of Birth\n'
                                '3.Region\n'
                                '4.Validate\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '-->')
            if user_choise == '1':
                first_num = int(user_id[0])
                for first_num in range(1, 9):
                    if first_num % 2 != 0:
                        print('You are a Woman!')
                    else:
                        print('You are a Man')
            elif user_choise == '2':  #DD.MM.YYYY
                pass
            elif user_choise == '3':    #Not in list( was not born in Estonia)
                pass
            elif user_choise == '4':
                pass
            elif user_choise == '5':
                break
            elif user_choise == '0':
                print('Goodbye')
                quit()
            else:
                print('Choice is out of range!')
