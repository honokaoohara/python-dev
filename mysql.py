from flask import *
from flask_cors import CORS
import MySQLdb

app = Flask(__name__)
CORS(app)

connection = MySQLdb.connect(user='root', passwd='', host='localhost', db='app', charset="utf8")

@app.route("/tweets")
def index():
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from tweets")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0')