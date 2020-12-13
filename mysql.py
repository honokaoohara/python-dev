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

@app.route("/tweets/like", methods=["POST"])
def like():
    id = request.json["id"]
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("update tweets set likes=likes+1 where id = %s", (id,))
    connection.commit()
    return jsonify({})

@app.route("/tweets/<int:id>", methods=["DELETE"])
def delete(id):
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("delete from tweets where id = %s", (id,))
    connection.commit()
    return jsonify({}), 204

@app.route("/tweets", methods=["POST"])
def post():
    tweet = request.json["tweet"]
    user = request.json["user"]
    if (tweet == '' or user == ''):
        return jsonify({"message": "tweet or username is empty"}), 400
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("insert into tweets (tweet, user) values (%s, %s)", (tweet, user,))
    connection.commit()
    return jsonify({})

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0')