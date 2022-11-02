import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, rating, content) VALUES (?, ?, ?)",
            ('Welcome to the Stress Journal!', 0, 'To create a post, click the New Post tab on the navigation bar. Have fun!')
            )

connection.commit()
connection.close()