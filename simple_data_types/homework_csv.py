import csv


with open('text_files/2019.csv', 'w', encoding='utf8') as file:
    csv_data = csv.reader(file)
    # with open('text_files/2019.csv', 'w', encoding='utf8') as wfile:
    #     csv_writer = csv.writer(wfile, delimiter='.', lineterminator=':\n')
     for line in csv_data:
         print(line)