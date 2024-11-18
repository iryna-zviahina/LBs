from flask import Flask, request, jsonify

app = Flask('__name__')


@app.route('/', methods=['POST'])
def data():
    text = request.get_data(as_text=True)
    if not text:
        return jsonify({"error": "No text provided"}), 400
    with open('text_file.txt', 'a') as file:
        file.write(text + '\n')
    return jsonify(f'Message: {text} have been successfully posted!'), 200


if __name__ == "__main__":
    app.run(port=8000,
            debug=True)
    