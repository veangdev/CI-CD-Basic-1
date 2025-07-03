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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
