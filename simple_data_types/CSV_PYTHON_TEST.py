import csv

# with open('text_files/test.csv', 'r', encoding='utf8') as file:
#
#     csv_data = csv.reader(file)
#
#     with open('csv_files/test_copy.csv', 'w', encoding='utf8') as wfile:
#         csv_writer = csv.writer(wfile, delimiter='.', lineterminator=':\n')
#
#         csv_writer.writerow(csv_data)
#         # for line in csv_data:
#         #     csv_writer.writerow(line)
#
#
# with open('text_files/test.csv', 'r', encoding='utf8') as file:
#     csv_data = csv.reader(file, delimiter='.')
#
#     for line in csv_data:
#         print(line)



# with open('text_files/test.csv', 'r', encoding='utf8') as file:
#     headers = ['N', 'D', 'T']
#     csv_reader = csv.DictReader(file)       # fieldnames=headers)
#
#     for line in csv_reader:
#         print(line)


with open('text_files/test.csv', 'r', encoding='utf8') as file:
    headers = ['N', 'D', 'T']
    csv_reader = csv.DictReader(file)

    with open('text_files/test.csv', 'w', encoding='utf8') as wfile:
        csv_writer = csv.DictReader(wfile, fieldnames=['Name', 'Date of birth', 'town'], lineterminator='\n')
        #csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)


