from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_data():
    content_type = request.headers.get('Content-Type') #отримуємо значення парамтера заголовку тип змісту
    if content_type == 'application/json': #якщо json
        return jsonify({'currency': 'UAH', 'price': 250})
    elif content_type == 'application/xml': #якщо xml
        response = """
        <data>
            <currency>UAH</currency>
            <price>250</price>
        </data>"""
        return response, 200, {"Content-Type": "application/xml"}
    else: #в іншому разі
        return 'Currency: UAH, Price: 250', 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(port=8000)