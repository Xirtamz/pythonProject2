# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов
# 2. Кол-во уникальных (разных)
#
# Не влияет на уникальность:
# Заглавные и прописные буквы
# Знаки препинания: ',' '.' '!' '?'
#
# Сохраняет кол-ва в отдельный файл.
# Выписывает все уникальные слова в алфавитном порядке (по одному слову в строке).

# file = open('text_files/trimushketera.txt', 'r',  encoding='utf8')

# for line in file:
#     words += len(line.split())


# print("There are", words, 'words')


# def get_words(text):
#     with open('text_files/trimushketera.txt', 'r',  encoding='utf8') as file:
#         text = file.read()
#         text = text.replace("\n", " ")
#         text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
#         text = text.lower()
#         words = text.split()
#         words.sort()
#         return words
#
#
# def word_count(words):
#     words_dict = dict()
#
#     for word in words:
#         if word in words_dict:
#             words_dict[word] = words_dict[word] + 1
#         else:
#             words_dict[word] = 1
#     return words_dict
#
#
# words = get_words('text_files/trimushketera.txt')
# words_dict = word_count(words)
# print(f"There are: {len(words)} words")
# print(f"There are: {len(words_dict)} unique words")
# print("------------------------- \n-------------------")
# for word in words_dict:
#     print(word.ljust(20), words_dict[word])

# with open('text_files/trimushketera.txt', 'r', encoding='utf8')as file:
#     data = file.read()
#
#     data = data.lower().replace('.', '').replace('!', '')
#     words = data.split()
#     unique = list(set(words))
#     unique.sort()
#
# with open('text_files/trimushketera.txt', 'w', encoding='utf8') as file:
#     file.write(f'there are {len(words)} words.\n')
#     file.write(f'There are {len(unique)} unique words.\n')
#     for word in unique:
#         file.write(word + '\n')


order = {
    'small': {'height': 40, 'width': 60, 'qty': 30},
    'medium': {'height': 70, 'width': 90, 'qty': 54},
    'large': {'height': 90, 'width': 120, 'qty': 15}
}


def area(a, b):
    return a * b


def perimeter(a, b):
    return (a + b) / 2

def material_counter(amount, material_amount):
    return material_amount * amount

def single_size(unit):
    result = {
        'total_area': material_counter(unit['qty'], (unit['width'])),
        'total_perimeter': material_counter(unit['qty'], (unit['width'])),
    }
    return result


# print(single_size(order['smal']))


def total_material(order):
    result = {
        'total_carpet_material': 0,
        'total_edge_material': 0
    }
    for unit in order:
        unit_size = single_size(order[unit])
        result['total_edge_material'] += unit_size['total_perimeter']
        result['total_carpet_material'] += unit_size['total_area']
    return result

print(total_material(order))
print(single_size(order['small']))
print(single_size(order['medium']))
print(single_size(order['large']))

