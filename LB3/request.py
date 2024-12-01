import requests
from requests.auth import HTTPBasicAuth

URL = 'http://127.0.0.1:8000'
USERNAME = 'Irynka'
PASSWORD = 'VeryS4fe'


def get_books():
    response = requests.get(f'{URL}/books', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print('Catalog:')
        for item in response.json():
            print(item)
    else:
        print(f'Failed to retrieve catalog: {response.status_code}')


def add_book(name, author, genre, price):
    data = {'name': name, 'author': author, 'genre': genre, 'price': price}
    response = requests.post(f'{URL}/books', json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 201:
        print('Book added successfully.')
    else:
        print(f'Failed to add book: {response.status_code}')


def update_book(book_id, name, author, genre, price):
    data = {'name': name, 'author': author, 'genre': genre, 'price': price}
    response = requests.put(f'{URL}/books/{book_id}', json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print('Book updated successfully.')
    else:
        print(f'Failed to update book: {response.status_code}')


def delete_book(book_id):
    response = requests.delete(f'{URL}/books/{book_id}', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print('Book deleted successfully.')
    else:
        print(f'Failed to delete book: {response.status_code}')


def delete_all_books():
    response = requests.delete(f'{URL}/books', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code == 200:
        print('All books deleted successfully.')
    else:
        print(f'Failed to delete all books: {response.status_code}')


if __name__ == '__main__':
    add_book(name='Felix Austria', author='Sofiia Andrukhovych', genre='Novel', price=300)
    add_book(name='The Witch of Konotop', author='Hryhorii Kvitka-Osnovianenko', genre='Satirical fiction', price=250)
    get_books()
    update_book(book_id=28, name='Felix Austria', author='Sofiia Andrukhovych', genre='Novel', price=350)
    delete_book(book_id=28)
    delete_all_books()