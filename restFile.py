import sqlite3
from flask import jsonify, request, Response, abort, Flask
from utils import *
import logging

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db_conn = sqlite3.connect("db.sqlite")
c = db_conn.cursor()


def exec_query_sqlite(query):
    """ Execute SQLite db query. """
    logging.debug(query)
    cursor = db_conn.cursor()
    cursor.execute(query)
    db_conn.commit()
    ret = cursor.fetchall()
    if not ret:
        return None
    else:
        ret = map(lambda x: x[0] if len(x) < 2 else x, ret)
        return list(ret)


def find_activity_hint(activity_name):
    query = "SELECT name FROM activity WHERE name LIKE '%s' LIMIT 3" % (activity_name + "%")
    results_raw = exec_query_sqlite(query)
    results_list = []
    if results_raw:
        for activity in results_raw:
            results_list.append(activity)

    return results_list


@app.route('/get/<userId>', methods=['GET'])
def getUserById(userId):
    query = " SELECT * FROM USER WHERE id='$d'" % userId
    results_raw = exec_query_sqlite(query)
    return jsonify(
        results_raw
    )


@app.route('/add/', methods=['POST'])
def addOffert(offertJson):
query = "INSERT INTO OFFERTS "
    return


if __name__ == "__main__":
    app.run(debug=True)


