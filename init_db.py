import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, rating, content) VALUES (?, ?, ?)",
            ('First Post', 2, 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, rating, content) VALUES (?, ?, ?)",
            ('Second Post', 4, 'Content for the second post')
            )

connection.commit()
connection.close()