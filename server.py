from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"language": "python"})

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0')