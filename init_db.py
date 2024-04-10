import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO vehicle_errors (id, error_code, error_message, vehicle_id, timestamp) VALUES (1,'ERROR2392', 'Connection to vehicle was lost', '5', 1234567890)")

connection.commit()

connection.close()


