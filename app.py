from flask import Flask, jsonify, json

app = Flask(__name__)
@app.route('/')
def hello_world():
    with open("data.json", "r", encoding="utf-8") as json_file:
        files = json.load(json_file)
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True)