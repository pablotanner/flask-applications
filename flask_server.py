import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home_page():
    return 'Server is running!'


@app.route('/logs/vehicle-errors', methods=['GET','POST'])
def get_vehicle_errors():
    conn = get_db_connection()
    if request.method == 'GET':
        # return all errors from the database (if GET)
        data = conn.execute('SELECT * FROM vehicle_errors').fetchall()
        # convert the data to a list of dictionaries
        data = [dict(i) for i in data]
        return {'vehicle_errors': data}
    else:
        # insert a new error into the database (if POST)
        id = request.json.get('id')
        vehicle_id = request.json.get('vehicle_id')
        error_code = request.json.get('error_code')
        error_message = request.json.get('error_message')
        conn.execute('INSERT INTO vehicle_errors (id, vehicle_id, error_code, error_message) VALUES (?, ?, ?, ?)',
                     (id, vehicle_id, error_code, error_message))
        return {'message': 'New error inserted into the database!'}





