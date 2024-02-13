import csv

with open('text_files/2019.csv', 'r', encoding='utf8') as file:

    # csv_data = list(csv.reader(file))
    csv_data = csv.reader(file)
    headers = next(csv_data)

    for line in csv_data:
        print(str(line))




    # print(list(csv_data))

    # print(next(csv_data))

# x = iter([1, 2, 3, 4])
# print(x)
