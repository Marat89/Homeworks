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

"""crate user dictionary"""
for i in read_json('../3_test data/users.json'):
    user_dict.append(
        {'name': i['name'], 'gender': i['gender'], 'age': i['age'], 'address': i['address'], 'books': []})



"""create book dictionary"""
for i in read_csv('../3_test data/books.csv'):
    books_dict.append({'title': i['Title'], 'author': i['Author'], 'pages': i['Pages'], 'genre': i['Genre']})

"""books + users"""
print(type(user_dict[0]['books']))
num = len(user_dict)
x = 0
for book in books_dict:
    user_dict[x]["books"].append(book)
    x += 1
    if x >= num:
        x = 0

write(user_dict, '../3_test data/result.json')
