while True:
    user_id = input('Enter your ID: ')
    try:
        int(user_id)
        if len(user_id) != 11:
            raise Exception
    except ValueError:
        print('Code Is Not Numeric, Try Again!')
    except Exception:
        if len(user_id) > 11:
            print('Too Long')
        else:
            print('Too Short')
    else:
        while True:
            user_choice = input('1.Gender\n'
                                '2.Date of Birth\n'
                                '3.Region\n'
                                '4.Validate\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '-->')
            if user_choice == '1':

                if int(user_id[0]) % 2 == 0:
                    print(f'You are a Woman!')
                else:
                    print('You are a Man')
            elif user_choice == '2':  #DD.MM.YYYY
                if int(user_id[0]) <= 4:
                    print(f'You were born in {user_id[5:7]}.{user_id[3:5]}.19{user_id[1:3]}')
                else:
                    print(f'You were born in {user_id[5:7]}.{user_id[3:5]}.20{user_id[1:3]}')
            elif user_choice == '3':    #Not in list( was not born in Estonia)
                if 0o1 < int(user_id[7:10]) <= 0o10:
                    print('You were born in "Kuressaare haigla"')
                elif 0o11 < int(user_id[7:10]) <= 0o20:
                    print('Tartu Ülikooli Naistekliinik')
                elif 0o21 < int(user_id[7:10]) <= 150:
                    print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
                elif 151 < int(user_id[7:10]) <= 160:
                    print('Keila haigla')
                elif 161 < int(user_id[7:10]) <= 220:
                    print('Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
                elif 221 < int(user_id[7:10]) <= 270:
                    print('Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)')
                elif 271 < int(user_id[7:10]) <= 370:
                    print('Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
                elif 371 < int(user_id[7:10]) <= 420:
                    print('Narva haigla')
                elif 421 < int(user_id[7:10]) <= 470:
                    print('Pärnu haigla')
                elif 471 < int(user_id[7:10]) <= 490:
                    print('Haapsalu haigla')
                elif 491 < int(user_id[7:10]) <= 520:
                    print('Järvamaa haigla (Paide)')
                elif 521 < int(user_id[7:10]) <= 570:
                    print('Rakvere haigla, Tapa haigla')
                elif 571 < int(user_id[7:10]) <= 600:
                    print('Valga haigla')
                elif 601 < int(user_id[7:10]) <= 650:
                    print('Viljandi haigla')
                elif 651 < int(user_id[7:10]) <= 700:
                    print('Lõuna-Eesti haigla (Võru), Põlva haigla')
                else:
                    print('Was not born in Estonia')
            elif user_choice == '4':
                # control = user_id[0] * 1 + user_id[1] * 2 + user_id[2] * 3 + user_id[3] * 4 + user_id[4] * 5
                check1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                check2 = [user_id]
                result = 0
                for i in range(10):
                    result += int(user_id[i] * check1[i])
                if result % 11 == 10:
                    pass
                elif result % 11 == int(user_id[-1]):
                    print('valid id')
                else:
                    print('not valid')
            elif user_choice == '5':
                break
            elif user_choice == '0':
                print('Goodbye')
                quit()
            else:
                print('Choice is out of range!')


# user_id = "39005090241"
# validation1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# id_list = str(user_id[:10])
# output = list(map(int, str(id_list[:10])))
# res_list = [output[i] * validation1[i] for i in range(len(output))]
# print(str(res_list))
#
# val1 = sum(res_list) % 11
# print(val1)
