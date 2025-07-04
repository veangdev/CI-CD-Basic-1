from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Welcome to the CAWE Python API 🎉")

@app.route("/add", methods=["GET"])
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify(result=a + b)

@app.route("/list", method=["GET"])
def list():
    arrays = [
        {"id": "dol", "name": "Array 1", "size": 10},
        {"id": "sit", "name": "Array 2", "size": 20},
        {"id": "amet", "name": "Array 3", "size": 30}
    ]
    return jsonify(arrays)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
