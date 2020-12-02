from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/tweets")
def index():
    return jsonify({"status": "200"})

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0')