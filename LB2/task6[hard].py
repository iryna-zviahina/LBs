from flask import Flask, request, jsonify
import sqlite3

app = Flask('__name__')


def init_db():
    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS data 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        content TEXT NOT NULL)
        """)
        db.commit()


@app.route('/', methods=['POST'])
def data():
    text = request.get_data(as_text=True)
    if not text:
        return jsonify({"error": "No text provided"}), 400

    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO data (content) VALUES (?)", (text,))
        db.commit()
    return jsonify(f'Message: {text} have been successfully posted!'), 200


if __name__ == "__main__":
    app.run(port=8000,
            debug=True)
