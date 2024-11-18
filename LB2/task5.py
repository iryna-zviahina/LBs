from flask import Flask, request, abort, jsonify
from datetime import datetime, timedelta
import requests

app = Flask(__name__)


@app.route('/currency', methods=['GET'])
def currency():
    day = request.args.get('date')
    date = 'N/A'

    if day not in ['today', 'yesterday']:
        abort(400, description="Invalid value for 'param'. Allowed values: 'today', 'yesterday'.")
    elif day == 'today':
        date = datetime.now().strftime('%Y%m%d')
    elif day == 'yesterday':
        date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

    response = requests.get(f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={date}&end={date}&valcode=USD&json")

    if not response:
        abort(404, description="No data found for the given date.")

    return jsonify(response)


if __name__ == "__main__":
    app.run(port=8000)