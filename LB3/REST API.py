from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()


def init_db():
    with sqlite3.connect('catalog.db') as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                price FLOAT NOT NULL
            )''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )''')
        db.commit()


@auth.verify_password
def verify_password(username, password):
    db = sqlite3.connect('catalog.db')
    cursor = db.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    if user and user[0] == password:
        return True
    return False


@app.route('/books', methods=['GET', 'POST', 'DELETE'])
@auth.login_required
def books():
    db = sqlite3.connect('catalog.db')
    cursor = db.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM books')
        items = cursor.fetchall()
        return jsonify([{'id': row[0], 'name': row[1], 'author': row[2], 'genre': row[3], 'price': row[4]}
                        for row in items])
    elif request.method == 'POST':
        book = request.json
        cursor.execute('INSERT INTO books (name, author, genre, price) VALUES (?, ?, ?, ?)',
                       (book['name'], book['author'], book['genre'], book['price']))
        db.commit()
        return jsonify({'message': 'Item added successfully'}), 201
    elif request.method == 'DELETE':
        cursor.execute('DELETE FROM books')
        db.commit()
        return jsonify({'message': 'All items deleted successfully'}), 200
    db.close()


@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def specific_book(id):
    db = sqlite3.connect('catalog.db')
    cursor = db.cursor()
    if request.method == 'GET':
        cursor.execute('SELECT * FROM books WHERE id = ?', (id,))
        item = cursor.fetchone()
        if item:
            return jsonify({'id': item[0], 'name': item[1], 'author': item[2], 'genre': item[3], 'price': item[4]})
        return jsonify({'message': 'Item not found'}), 404
    elif request.method == 'PUT':
        book = request.json
        cursor.execute('UPDATE books SET name = ?, author = ?, genre = ?, price = ? WHERE id = ?',
                       (book['name'], book['author'], book['genre'], book['price'], id))
        db.commit()
        return jsonify({'message': 'Item updated successfully'})
    elif request.method == 'DELETE':
        cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        db.commit()
        return jsonify({'message': 'Item deleted successfully'})
    db.close()


@app.route('/init_user', methods=['POST'])
def init_user():
    data = request.json
    db = sqlite3.connect('catalog.db')
    cursor = db.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (data['username'], data['password']))
        db.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'User already exists'}), 400
    finally:
        db.close()


if __name__ == '__main__':
    init_db()
    app.run(port=8000, debug=True)
