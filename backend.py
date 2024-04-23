import sqlite3

def connect():
    conn = sqlite3.connect("car_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY, car_code INT, model TEXT, manufacturer TEXT, year INTEGER, fuel_capacity INTEGER, mileage REAL, horsepower REAL, zero_to_60 REAL, top_speed REAL, price REAL)")
    conn.commit()
    conn.close()
    
def insert(car_code, model, manufacturer, year, fuel_capacity, mileage, horsepower, zero_to_60, top_speed, price):
    conn = sqlite3.connect("car_db.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO cars VALUES(NULL,?,?,?,?,?,?,?,?,?,?)",(car_code, model, manufacturer, year, fuel_capacity, mileage, horsepower, zero_to_60, top_speed, price))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("car_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars ")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("car_db.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM cars WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    
def search(car_code = "", model = "", manufacturer = "", year = "", fuel_capacity = "", mileage = "", horsepower = "", zero_to_60 = "", top_speed = "", price = ""):
    conn = sqlite3.connect("car_db.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars WHERE car_code = ? OR model = ? OR manufacturer = ? OR year = ? OR fuel_capacity = ? OR mileage = ? OR horsepower = ? OR zero_to_60 = ? OR top_speed = ? OR price = ?",(car_code, model, manufacturer, year, fuel_capacity, mileage, horsepower, zero_to_60, top_speed, price))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(id, car_code, model, manufacturer, year, fuel_capacity, mileage, horsepower, zero_to_60, top_speed, price):
    conn = sqlite3.connect("car_db.db")
    cur = conn.cursor()
    cur.execute("UPDATE cars SET car_code = ?, model = ?, manufacturer = ?, year = ?, fuel_capacity = ?, mileage = ?, horsepower = ?, zero_to_60 = ?, top_speed = ?, price = ? WHERE id = ?",(car_code, model, manufacturer, year, fuel_capacity, mileage, horsepower, zero_to_60, top_speed, price, id))
    conn.commit()
    conn.close()
    
    
connect()
#insert(112312, 'A7', 'Audi', 2019, 535, 13.88, 335, 4.9, 250, 90.50)
#update(1,'v', 'x', 1, 1, 1, 1, 1, 1, 1, 1)
#delete(2)
#print(view())
