print("Welcome")
height = int(input("What is your height?: "))
bill = 0
if height > 120:
    print("Go on")
    age = int(input('Your age?: '))
    bill = 5
    if age < 12:
        print('Child ticket $5')
    elif age <= 18:
        bill = 7
        print('youth tickets $7')
    elif age >= 45 and age <= 55:
      print("everything is ok")
    else:
        bill = 12
        print('Adult ticket 12$')
    want_pic = input('DO you want a pic?: ')
    if want_pic == "Y":
        bill += 3

    print(f'Your final ticket casts {bill}')
else:
    print('Grow up, man')


# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bmi = weight / height ** 2
# if bmi <= 18.5:
#     print('they are underweight')
# elif 25 >= bmi > 18.6:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif 30 >= bmi > 25:
#     print('Your BMI is' + str(bmi) + ', you are slightly overweight.')
# elif 35 >= bmi > 30:
#     print('Your BMI is' + str(bmi) + ', you are slightly overweight.')
# else:
#     print('clinically obese.')




