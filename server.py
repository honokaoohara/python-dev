from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "200"})

@app.route("/post", methods=['POST'])
def post():
    return jsonify({"status": "204"})

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0')