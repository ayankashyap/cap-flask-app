from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new')
def new():
    return render_template('user.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO users (username, email) VALUES (?,?)", (username, email))
                con.commit()
                msg = "Record added"
        except:
            con.rollback()
            msg = "Error in insertion"
        
        finally:
            return render_template("result.html", msg = msg)
            con.close()

@app.route('/disp')
def display():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from users")
   
    rows = cur.fetchall()
    return render_template("display.html",rows = rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5001, debug = True)