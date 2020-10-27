from flask import Flask
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)


def display() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'mynewpassword',
        'host': 'db',
        'port': '3306',
        'database': 'userdata'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    results = [{username: email} for (username, email) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'userdata': display()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')