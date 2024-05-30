# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request 
import sqlite3 

app = Flask(__name__)


@app.route('/') 
def hello_world():
    return 'Jhaat barabar duniya!!!!!!!!!!!!'

@app.route('/home') 
def index(): 
    return render_template('index.html') 
  
  
connect = sqlite3.connect('sqlite_db.db') 
# connect.execute( 
#     'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, profession TEXT)'
# ) 
connect.execute(
    '''
    CREATE TABLE IF NOT EXISTS InventoryItem (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    '''
)  
  
@app.route('/form', methods=['GET', 'POST']) 
def form(): 
    if request.method == 'POST': 
        name = request.form['name'] 
        quantity = request.form['quantity'] 
        price = request.form['price'] 
        print("name :", name)
        print("quantity :", quantity)
        print("price :", price)
  
        with sqlite3.connect("sqlite_db.db") as users: 
            cursor = users.cursor() 
            cursor.execute(
                "INSERT INTO InventoryItem (name, quantity, price) VALUES (?, ?, ?)", 
                (name, quantity, price)
            )
            users.commit() 
        return render_template("index.html") 
    else: 
        return render_template('form.html') 
  
  
@app.route('/inventory') 
def inventory(): 
    connect = sqlite3.connect('sqlite_db.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM InventoryItem') 
  
    data = cursor.fetchall() 
    print("data :", data)
    return render_template("inventory.html", data=data) 
  
  
if __name__ == '__main__': 
    app.run(debug=False) 