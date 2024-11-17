from flask import Flask, request

app = Flask(__name__)


@app.route('/paint_price', methods=['GET'])
def get_price():
    color = request.args.get('color')
    company = request.args.get('company')
    if color and company:
        return 'Price: 230 UAH'
    else:
        return 'Not enough parameters in the request', 400


if __name__ == "__main__":
    app.run(port=8000)
