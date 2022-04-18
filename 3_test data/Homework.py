import csv
import json


def read_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file_json:
        return json.load(file_json)


def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file_csv:
        books = csv.DictReader(file_csv)
        books = [i for i in books]
        return books


def write(data, file_path):
    with open(file_path, "w", encoding='utf-8') as f2:
        json.dump(data, f2, indent=4)


user_dict = []
books_dict = []
n = 0
x = 0

"""crate user dictionary"""
for i in read_json('../3_test data/users.json'):
    user_dict.append(
        {'name': i['name'], 'gender': i['gender'], 'age': i['age'], 'address': i['address']})
    user_dict.append('books')

"""create book dictionary"""
for i in read_csv('../3_test data/books.csv'):
    books_dict.append({'title': i['Title'], 'author': i['Author'], 'pages': i['Pages'], 'genre': i['Genre']})

"""books + users"""
# w = list(user_dict[0].items())
# w.append(books_dict[0])
# w.append(books_dict[1])
# print(w)
# write(w, '../3_test data/result.json')


for books in books_dict:
    print(x)
    """Я понял, что  первый цикл проходит ноърмально, но на втором цикле на этой строке. он почему-то не берет новго пользователя,
     а обращается внутри выбранного пользователя к конкретной строке по индексу, не знаю как это обойти и почему вообще так. """
    new_user = user_dict[x]
    print(new_user)
    print(type(new_user))
    new_user.append(books_dict[n])
    print(type(new_user))
    new_user = list(new_user.items())
    print(new_user)
    print(type(new_user))
    new_user.append(books_dict[n])
    n += 1
    x += 1

    if x == 28:
        x = 0
write(new_user, '../3_test data/result.json')
